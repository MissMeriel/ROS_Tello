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


def parse_xml(tree):
	global xml_topics
	root = tree.getroot()
	test_print("XML INFO")
	topics_in = []
	topics_out = []
	for child in root:
		#print(child.tag+"="+child.attrib)
		io_topics[child.attrib['name']] = child.attrib
		topics_in = filter(None, child.attrib['topics_in'].split(" "))
		xml_topics.update(topics_in)
		topics_out = filter(None, child.attrib['topics_out'].split(" "))
		xml_topics.update(topics_out)
		io_topics[child.attrib['name']]['topics_in'] = topics_in
		io_topics[child.attrib['name']]['topics_out'] = topics_out
	for t in xml_topics:
		node_lookup[t] = {'in': "", 'out': ""}
	test_print("BUILDING NODE LOOKUP")
	for node in io_topics:
		for ti in io_topics[node]['topics_in']:
			test_print("node: "+str(node)+"; ti: "+str(ti))
			node_lookup[ti]['in']=node
		for to in io_topics[node]['topics_out']:
			test_print("node: "+str(node)+"; to: "+str(to))
			node_lookup[to]['out']=node
		test_print(node_lookup)
	test_print("XML TOPICS: \n"+str(xml_topics))
	test_print("IO_TOPICS:")
	for t in io_topics:
		test_print(t+": "+str(io_topics[t]))
	test_print("NODE_LOOKUP:")
	for t in node_lookup:
		test_print(t+": "+str(node_lookup[t]))
	topics = []
	for t in xml_topics:
		if t != '':
			topics.append(t)


def parse_inv_xml(xml_tree):
	root = xml_tree.getroot()
	spinfo_string = ""
	test_print(str(root.tag)+"="+str(root.attrib)+str(root.text))
	for child in root.iter("PPT"):
		for invinfo in child.iter("INVINFO"):
			if("OneOf" in invinfo.find("DAIKONCLASS").text and "one of" in invinfo.find("INV").text):
				test_print(child.find("PPTNAME").text)
				test_print("\t"*1 + str(invinfo.tag)+"="+str(invinfo.attrib))
				test_print("\t"*2+"PARENT="+invinfo.find("PARENT").text)
				test_print("\t"*2+"INV="+invinfo.find("INV").text)
				test_print("\t"*2+"SAMPLES="+invinfo.find("SAMPLES").text)
				test_print("\t"*2+"DAIKON="+invinfo.find("DAIKON").text)
				test_print("\t"*2+"DAIKONCLASS="+invinfo.find("DAIKONCLASS").text)
				test_print("\t"*2+"METHOD="+invinfo.find("METHOD").text)
				if("one of" in invinfo.find("INV").text):
					ppt = child.find("PPTNAME").text.split(":")[0].split("(")[0]
					test_print("ppt "+str(ppt))
					spinfo_string += "PPT_NAME "+ ppt
					infosplit = invinfo.find("INV").text.split("one of")
					varname = infosplit[0]
					valsplit = infosplit[1].replace("{", "").strip("}")
					test_print(valsplit)
					vals = valsplit.split(",")
					for val in vals:
						spinfo_string += "\n"+varname+" == "+val
					spinfo_string += "\n\n"
	test_print("SPINFO_STRING:")
	test_print(spinfo_string)
	return spinfo_string


def strip_xml_of_repeats(tree):
	root = xml_tree.getroot()
	spinfo_string = ""
	test_print(str(root.tag)+"="+str(root.attrib)+str(root.text))
	for child in root.iter("PPT"):
		for invinfo in child.iter("INVINFO"):
			if("OneOf" in invinfo.find("DAIKONCLASS").text and "one of" in invinfo.find("INV").text):
				test_print(child.find("PPTNAME").text)
				test_print("\t"*1 + str(invinfo.tag)+"="+str(invinfo.attrib))
				test_print("\t"*2+"PARENT="+invinfo.find("PARENT").text)
				test_print("\t"*2+"INV="+invinfo.find("INV").text)
				test_print("\t"*2+"SAMPLES="+invinfo.find("SAMPLES").text)
				test_print("\t"*2+"DAIKON="+invinfo.find("DAIKON").text)
				test_print("\t"*2+"DAIKONCLASS="+invinfo.find("DAIKONCLASS").text)
				test_print("\t"*2+"METHOD="+invinfo.find("METHOD").text)
				if("one of" in invinfo.find("INV").text):
					ppt = child.find("PPTNAME").text.split(":")[0].split("(")[0]
					test_print("ppt "+str(ppt))
					spinfo_string += "PPT_NAME "+ ppt
					infosplit = invinfo.find("INV").text.split("one of")
					varname = infosplit[0]
					valsplit = infosplit[1].replace("{", "").strip("}")
					test_print(valsplit)
					vals = valsplit.split(",")
					for val in vals:
						spinfo_string += "\n"+varname+" == "+val
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
