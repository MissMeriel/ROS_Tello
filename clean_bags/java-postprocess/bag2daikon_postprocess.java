import daikon.PptMap;
import daikon.PptTopLevel;
import daikon.*;
import daikon.FileIO;
import daikon.inv.Invariant;
import daikon.inv.unary.OneOf;
import java.io.*;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.ObjectInputStream;
import java.util.*;
import java.util.ArrayList;
import com.github.swrirobotics.bags.reader.*;
import com.github.swrirobotics.bags.reader.records.*;
import com.github.swrirobotics.bags.reader.messages.serialization.MessageType;
import com.github.swrirobotics.bags.reader.messages.serialization.*;
import com.github.swrirobotics.bags.reader.BagFile;
import com.github.swrirobotics.bags.reader.exceptions.*;
import com.github.swrirobotics.bags.reader.exceptions.BagReaderException;

/**
 * Postprocessing of invariants for temporal invariant generation
 *
 */


public class bag2daikon_postprocess {

	public static PptMap pptmap;
	private static final String OUTPUT_FILE = "demo2_2018-12-21-11-10-07_postproc.txt";

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
		}
	}

	public static void main(String[] args) throws BagReaderException {
		
		try{
			String inv_file = "demo2_statestd_2019-01-29-10-53-10.inv"; //args[1];
			String bag_file = "demo2_statestd_2019-01-29-10-53-10.bag";
			readInSerializable(inv_file);
			OutputStream out = new FileOutputStream(OUTPUT_FILE);
			BagFile file = BagReader.readFile(bag_file);

			System.out.println("Topics:");
			//String[] topics = [];
			for (TopicInfo topic : file.getTopics()) {
			    System.out.println(topic.getName() + " \t\t" + topic.getMessageCount() +
					  " msgs \t: " + topic.getMessageType() + " \t" +
					  (topic.getConnectionCount() > 1 ? ("(" + topic.getConnectionCount() + " connections)") : ""));
			}

			/* sorted bag --> msg array w/ fuzzy chron compare across topics
			* 
			*/

			/*System.out.println("\n");
			file.forMessagesOfType("std_msgs/String", new MessageHandler() {
			    @Override
			    public boolean process(MessageType message, Connection conn) {
				try {
				    System.out.println(message.<StringType>getField("data").getValue());
				}
				catch (UninitializedFieldException e) {
				    System.err.println("Field was not initialized.");
				}
				return true;
			    }
			});*/
		 
		} catch(IOException e) {
			e.printStackTrace();
		}
	}

}
