import daikon.PptMap;
import daikon.PptTopLevel;
import daikon.*;
import daikon.FileIO;
import daikon.inv.Invariant;
import daikon.inv.unary.OneOf;
import java.io.*;
import java.io.ObjectInputStream;
import java.util.*;
import java.util.ArrayList;

/**
 * Postprocessing of invariants for temporal invariant generation
 *
 */


public class bag2daikon_postprocess {

	public static PptMap pptmap;

	public static void createSerializable(String filename) throws IOException {
		FileOutputStream fileout =  new FileOutputStream(filename);
		ObjectOutputStream out =  new ObjectOutputStream(fileout);
		out.writeObject(pptmap);
		out.flush();
		out.close();
	}

	public static void readInSerializable(String filename) throws IOException {
		File input_file = new File (filename);
		FileInputStream filein = new FileInputStream(input_file);
		ObjectInputStream in = new ObjectInputStream(filein);
		try { 
			ArrayList file_collection = new ArrayList();
			file_collection.add(input_file);
			pptmap = FileIO.read_serialized_pptmap(input_file, true);
			System.out.println("pptmap slices: "+pptmap.countSlices());
			System.out.println("pptmap tostring: "+pptmap.toString());
			for(Iterator<PptTopLevel> iter = pptmap.ppt_all_iterator(); iter.hasNext(); ){
				PptTopLevel pptTopLevel = iter.next();
				System.out.println("\n"+pptTopLevel.toString());
				
				
				ArrayList invs = new ArrayList(pptTopLevel.getInvariants());
				for(Iterator<Invariant> i = invs.listIterator(); i.hasNext(); ){
					Invariant inv = i.next();
					if(inv instanceof OneOf) {
					System.out.println("\t"+inv.toString());
					System.out.println("\t\t"+inv.varNames());
					}
				}

			}

		} catch (IOException exc) {
			System.out.println("IOException on readInSerializable("+filename+")");
			exc.printStackTrace();
		} /*catch (ClassNotFoundException exc) {
			System.out.println("ClassNotFoundException on readInSerializable("+filename+")");
			exc.printStackTrace();
		}*/
	}

	public static void main(String[] args){
		try{
			readInSerializable("demo2_2018-12-21-11-10-07.inv");
		} catch(IOException e) {
			e.printStackTrace();
		}
	}

}
