#/usr/bin/python
from __future__ import print_function
import sys
import time
import rosbag
from sets import Set
import numpy as np
import subprocess, yaml
import os
import xml.etree.ElementTree as ET
import re

# Pass in: 	invariant xml
#		bagfile
# Generating: 	conditionals splitter file (.spinfo)
#		temporals .decls and .dtrace


topics = []
message_types = []
message_fields = {}
bag_info = {}
testing = False
want_fields = False
xml_topics = Set()
comparability_count = 1
comparability_map = {}
xml_file = ""


MY_MACRO = """
if testing:
	print(test_output)
"""

FIELD_MACRO = """
if want_fields:
	print(field_output)
"""

def print_fields(field_output):
	exec FIELD_MACRO in globals(),locals()


def test_print(test_output):
	exec MY_MACRO in globals(), locals()


def parse_inv_xml(xml_tree):
	root = xml_tree.getroot()
	spinfo_string = ""
	test_print(str(root.tag)+"="+str(root.attrib)+str(root.text))
	for child in root.iter("PPT"):
		#splitter_set = Set()
		splitter_set = []
		for invinfo in child.iter("INVINFO"):

			if(("OneOf" in invinfo.find("DAIKONCLASS").text or "Probabilistic" in invinfo.find("DAIKONCLASS").text) and "one of" in invinfo.find("INV").text and "rotation" not in invinfo.find("INV").text and "stamp" not in invinfo.find("INV").text and "header.seq" not in invinfo.find("INV").text):
				test_print(child.find("PPTNAME").text)
				test_print("\t"*1 + str(invinfo.tag)+"="+str(invinfo.attrib))
				test_print("\t"*2+"PARENT="+invinfo.find("PARENT").text)
				test_print("\t"*2+"INV="+invinfo.find("INV").text)
				test_print("\t"*2+"SAMPLES="+invinfo.find("SAMPLES").text)
				test_print("\t"*2+"DAIKON="+invinfo.find("DAIKON").text)
				test_print("\t"*2+"DAIKONCLASS="+invinfo.find("DAIKONCLASS").text)
				test_print("\t"*2+"METHOD="+invinfo.find("METHOD").text)
				ppt = child.find("PPTNAME").text.split(":")[0].split("(")[0]
				test_print("ppt "+str(ppt))
				#spinfo_string += "PPT_NAME "+ ppt
				if("Probabilistic" in invinfo.find("DAIKONCLASS").text):
					ppt = child.find("PPTNAME").text.split(":")[0].split("(")[0]
					#test_print("ppt "+str(ppt))
					#spinfo_string += "PPT_NAME "+ ppt
					infosplit = invinfo.find("INV").text.split("one of")
					varname = infosplit[0]
					valsplit = infosplit[1].replace("{", "").split("}")
					test_print(valsplit)
					vals = valsplit[0].split(",")
					for val in vals:
						#splitter_set.add(varname+" == "+val)
						if(str(varname+" == "+val) not in splitter_set):
							splitter_set.append(varname+" == "+val)
					#	spinfo_string += "\n"+varname+" == "+val
					#spinfo_string += "\n\n"
				elif("OneOf" in invinfo.find("DAIKONCLASS").text and "one of" in invinfo.find("INV").text):
					ppt = child.find("PPTNAME").text.split(":")[0].split("(")[0]
					test_print("ppt "+str(ppt))
					#spinfo_string += "PPT_NAME "+ ppt
					infosplit = invinfo.find("INV").text.split("one of")
					varname = infosplit[0]
					valsplit = infosplit[1].replace("{", "").strip("}")
					test_print(valsplit)
					vals = valsplit.split(",")
					for val in vals:
						#splitter_set.add(varname+" == "+val)
						if(str(varname+" == "+val) not in splitter_set):
							splitter_set.append(varname+" == "+val)
					#	spinfo_string += "\n"+varname+" == "+val
					#spinfo_string += "\n\n"
		if(len(splitter_set) > 0):
			ppt = child.find("PPTNAME").text.split(":")[0].split("(")[0]
			test_print("ppt "+str(ppt))
			spinfo_string += "PPT_NAME "+ ppt
			#print(splitter_set)
			for spl in splitter_set:
				spinfo_string += "\n"+spl
			spinfo_string += "\n\n"
	test_print("SPINFO_STRING:")
	test_print(spinfo_string)
	return spinfo_string


def main():
	global testing, topics, message_types, message_fields, bag_info
	global comparability_map, comparability_count
	start_time = time.time()

	output_filename=sys.argv[1].split(".")
	xml_filehead=output_filename[0]


	#handle CL args
	spinfo_filename=output_filename[0]+".spinfo"

	#process .inv xml
	xml_tree = ET.parse(sys.argv[1])
	#with open(sys.argv[1]) as f:
	#	xml = f.read()
	#xml_tree = ET.fromstring(re.sub(r"(<\?xml[^>]+\?>)", r"\1<root>", xml) + "</root>")
	spinfo_string = parse_inv_xml(xml_tree)
	spinfo_file = file(spinfo_filename, "w")
	spinfo_file.write(spinfo_string)
	spinfo_file.close()
	print("New .spinfo file: "+spinfo_filename)
	print("Run .spinfo file as: java -cp $DAIKONDIR/daikon.jar daikon.Daikon --config_option daikon.derive.Derivation.disable_derived_variables=true "+ output_filename[0]+".decls "+ output_filename[0]+".dtrace "+spinfo_filename)

	#java -cp $DAIKONDIR/daikon.jar:${DAIKONDIR}/java/lib/*:${DAIKONDIR}/java daikon.Daikon --user-defined-invariant daikon.inv.unary.string.ProbabilisticString --user-defined-invariant daikon.inv.unary.scalar.ProbabilisticFloat --user-defined-invariant daikon.inv.unary.scalar.ProbabilisticScalar --user-defined-invariant daikon.inv.unary.stringsequence.ProbabilisticStringSequence
	
	#print("Generating conditional invariants....")
	#os.system('java -cp $DAIKONDIR/daikon.jar:${DAIKONDIR}/java/lib/*:${DAIKONDIR}/java daikon.Daikon --user-defined-invariant daikon.inv.unary.string.ProbabilisticString --user-defined-invariant daikon.inv.unary.scalar.ProbabilisticFloat --user-defined-invariant daikon.inv.unary.scalar.ProbabilisticScalar --user-defined-invariant daikon.inv.unary.stringsequence.ProbabilisticStringSequence '+ output_filename[0]+".decls "+ output_filename[0]+".dtrace "+spinfo_filename)
	#print("Unzipping conditional invariants from "+output_filename[0]+".inv.gz...")
	#os.system('gunzip '+output_filename[0]+'.inv.gz')
	#print("Generating conditional invariant XML....")
	#os.system('java -cp $DAIKONDIR/daikon.jar:${DAIKONDIR}/java/lib/*:${DAIKONDIR}/java  daikon.PrintInvariants --wrap_xml '+output_filename[0]+'.inv > '+output_filename[0]+'_split.xml')
	#print("XML file generated: "+output_filename[0]+"_split.xml")

	#separate split invariants file into repeated and nonrepeated conditional invs
	#xml_tree = ET.parse(output_filename[0]+'_split.xml')
	#nonrepeated_invs = strip_xml_of_repeats(xml_tree)

	#generate FSMs
	

if __name__ == "__main__":
    # execute only if run as a script 
    main()
