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

##################################
# NOTE: USE WELL-FORMED XML
# I.E. MUST HAVE A ROOT ELEMENT
# ################################


testing=True

MY_MACRO = """
if testing:
	print(test_output)
"""

def test_print(test_output):
	exec MY_MACRO in globals(), locals()


def strip_xml_of_boring_stuff(xml_tree):
	root = xml_tree.getroot()
	spinfo_string = ""
	test_print(str(root.tag)+"="+str(root.attrib)+str(root.text))
	for child in root.iter("PPT"):
		for invinfo in child.iter("INVINFO"):
			if("header.seq" in invinfo.find("INV").text or "header.stamp.nsecs" in invinfo.find("INV").text):
				print("removing invariant "+invinfo.find("INV").text)
				child.remove(invinfo)
			if("condition =" in child.find("PPTNAME").text):
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
	return xml_tree


def get_condition(ppt_name):
	#test_print("\nget condition for ppt_name: "+ppt_name)
	ppt_name_split = ppt_name.split("condition=")
	condition = ppt_name_split[len(ppt_name_split)-1]
	#test_print(condition)
	if("not" in condition):
		negation = condition.replace("not(", "")
		negation = negation.replace(")", "")
	else:
		negation = "\"not("+condition.replace("\"", "")+")\""
	#print("condition and negation: "+condition+"       "+negation)
	#print("condition and negation: "+ppt_name_split[0]+"condition="+condition+"       "+ppt_name_split[0]+"condition="+negation)
	return [ppt_name_split[0]+"condition="+condition, ppt_name_split[0]+"condition="+negation]


def strip_xml_of_repeats(xml_tree):
	root = xml_tree.getroot()
	spinfo_string = ""
	test_print(str(root.tag)+"="+str(root.attrib)+str(root.text))
	for ppt in root.iter("PPT"):
		#test_print("\n")
		if("condition=" in ppt.find("PPTNAME").text):
			#get negation ppt
			condition = get_condition(ppt.find("PPTNAME").text)
			negation = condition[1]
			for ppt2 in root.iter("PPT"):
				if (negation in ppt2.find("PPTNAME").text):
					print("negation found for "+condition[0])
					#find repeated invariants and get rid of them
					for invinfo1 in ppt.iter("INVINFO"):
						for invinfo2 in ppt2.iter("INVINFO"):
							if (invinfo1 == invinfo2):
								print("removing invariant "+invinfo1.find("INV").text)
								ppt.remove(invinfo1)
								ppt2.remove(invinfo2)
					#exit()
					#break
			
			negation_ppt = ppt.findtext("PPTNAME")
			#print("find negation: "+str(negation_ppt))

		for invinfo in ppt.iter("INVINFO"):
			if("condition =" in ppt.find("PPTNAME").text):
				test_print("\n"+ppt.find("PPTNAME").text)
				test_print("\t"*1 + str(invinfo.tag)+"="+str(invinfo.attrib))
				test_print("\t"*2+"PARENT="+invinfo.find("PARENT").text)
				test_print("\t"*2+"INV="+invinfo.find("INV").text)
				test_print("\t"*2+"SAMPLES="+invinfo.find("SAMPLES").text)
				test_print("\t"*2+"DAIKON="+invinfo.find("DAIKON").text)
				test_print("\t"*2+"DAIKONCLASS="+invinfo.find("DAIKONCLASS").text)
				test_print("\t"*2+"METHOD="+invinfo.find("METHOD").text)
				if("one of" in invinfo.find("INV").text):
					ppt_name = ppt.find("PPTNAME").text.split(":")[0].split("(")[0]
					test_print("ppt_name "+str(ppt_name))
	return xml_tree


def main():
	global testing, topics, message_types, message_fields, bag_info
	global comparability_map, comparability_count
	start_time = time.time()

	#handle CL args
	output_filename=sys.argv[1].split(".")
	xml_filehead=output_filename[0]
	print(xml_filehead)

	#separate split invariants file into repeated and nonrepeated conditional invs
	xml_tree = ET.parse(sys.argv[1])
	interesting_xml_tree = strip_xml_of_boring_stuff(xml_tree)
	nonrepeated_xml_tree = strip_xml_of_repeats(interesting_xml_tree)


if __name__ == "__main__":
    # execute only if run as a script
    main()
