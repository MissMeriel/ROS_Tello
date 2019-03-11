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
from xml.dom import minidom


############################################
#
# Pass in: 	invariant xml
#		.inv
# Generating: 	HITL-grouped xml
#
# HITL groups:	h (human)
#		m (machine)
#		h2m (human to machine)
#		m2h (machine to human)
#		h&m
#		h&h2m
#		h&m2h
#		m&h2m
#		m&m2h
#		h2m&m2h
#		other (not compared -- user can determine dominant interactions)
#
############################################

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
typedict = {"h":Set(), "m":Set(), "h2m":Set(), "m2h":Set(), "other":Set(), "relations":Set()}
h  = "h"
m = "m"
h2m = "h2m"
m2h = "m2h"
h_m = "h_m"
h_h2m = "h_h2m"
h_m2h = "h_m2h"
m_h2m = "m_h2m"
m_m2h = "m_m2h"
m2h_h2m = "m2h_h2m"
other = "other"
relations = "relations"

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

def parse_typespace_xml(xml_tree):
	global typedict
	root = xml_tree.getroot()
	for elem in root.iter("root"):
		for child in elem.iter("h"):
			for var in child.iter("var"):
				#test_print(var.tag+": "+str(var.get("name")))
				typedict["h"].add(var.get("name"))
		for child in elem.iter("m"):
			for var in child.iter("var"):
				#test_print(var.tag+": "+str(var.get("name")))
				typedict["m"].add(var.get("name"))
		for child in elem.iter("h2m"):
			for var in child.iter("var"):
				#test_print(var.tag+": "+str(var.get("name")))
				typedict["h2m"].add(var.get("name"))
		for child in elem.iter("m2h"):
			for var in child.iter("var"):
				#test_print(var.tag+": "+str(var.get("name")))
				typedict["m2h"].add(var.get("name"))
		for child in elem.iter("other"):
			for var in child.iter("var"):
				#test_print(var.tag+": "+str(var.get("name")))
				typedict["other"].add(var.get("name"))
		for child in elem.iter("relations"):
			for var in child.iter("relate"):
				#test_print(var.tag+": "+str(var.get("name")))
				relations = var.get("types").replace(" ", "_")
				typedict["relations"].add(relations)
	print(str(typedict))


def restruct_xml(xml_tree):
	global typedict
	comment_div = "<!-- ================= %s ================= -->" % "other"
	new_tree = ET.ElementTree()
	new_root = ET.Element('root')
	new_tree._setroot(new_root)
	root = xml_tree.getroot()
	for child in root.iter("PPT"):
		ppt_name_elem = ET.SubElement(new_root, "PPT_NAME")
		ppt_name_elem.text = child.find("PPTNAME").text
		h_elem = ET.SubElement(ppt_name_elem, "h")
		m_elem = ET.SubElement(ppt_name_elem, "m")
		h2m_elem = ET.SubElement(ppt_name_elem, "h2m")
		m2h_elem = ET.SubElement(ppt_name_elem, "m2h")
		other_elem = ET.SubElement(ppt_name_elem, "other")
		for invinfo in child.iter("INVINFO"):
			if("Probabilistic" in invinfo.find("DAIKONCLASS").text and "one of" in invinfo.find("INV").text):
				for var in typedict["h"]:
					if(var in invinfo.find("INV").text):
						#print("inv of type h")
						inv_elem = invinfo.find("INV")
						#ppt_name_h_elem.append(inv_elem)
						#print(ET.tostring(inv_elem, encoding="us-ascii", method="xml"))
						#print(ET.tostring(h_elem))
						#print(var + " in " +child.find("PPTNAME").text)
						invtext = invinfo.find("INV").text
						inv_text_split = invtext.split("}")
						#print("inv_text_split: "+str(inv_text_split))
						oneof_elem = ET.SubElement(inv_elem, "ONEOF")
						oneof_elem.text = inv_text_split[0]+"}"
						print(ET.tostring(inv_elem))

						inv_text_split1 = inv_text_split[1].split("\n\t")

						vals = inv_text_split[1].split("\n\t")
						print(vals)
						for val in vals[1:len(vals)]:
							val_split = val.split("probability: ")
							print("val_split: "+ str(val_split))
							val0 = val_split[0].strip()
							prob = val_split[1].split("\tcount:")
							prob0 = prob[0].replace(" probability: ", "")
							count = prob[1].split(" total:")
							count0 = count[0]
							total0 = count[1].replace("\t", "")
							#total0 = total
							print("val:"+val0+" prob:"+prob0+" count:"+count0+" total:"+total0)
							val_elem = ET.SubElement(inv_elem, "VAL")
							val_elem.text = val0
							#print(ET.tostring(inv_elem))
							prob_elem = ET.SubElement(inv_elem, "PROBABILITY")
							prob_elem.text = prob0
							#print(ET.tostring(inv_elem))
							count_elem = ET.SubElement(val_elem, "COUNT")
							count_elem.text = count0
							#val_elem.append(count_elem)
							total_elem = ET.SubElement(val_elem, "TOTAL")
							total_elem.text = total0
							#val_elem.append(total_elem)
						h_elem.append(inv_elem)
				for var in typedict["m"]:
					if(var in child.find("PPTNAME").text):
						#print(var + " in " +child.find("PPTNAME").text)
						
						#print("inv of type h")
						inv_elem = invinfo.find("INV")
						#ppt_name_h_elem.append(inv_elem)
						#print(ET.tostring(inv_elem, encoding="us-ascii", method="xml"))
						#print(ET.tostring(h_elem))
						#print(var + " in " +child.find("PPTNAME").text)
						invtext = invinfo.find("INV").text
						inv_text_split = invtext.split("}")
						#print("inv_text_split: "+str(inv_text_split))
						oneof_elem = ET.SubElement(inv_elem, "ONEOF")
						oneof_elem.text = inv_text_split[0]+"}"
						print(ET.tostring(inv_elem))

						inv_text_split1 = inv_text_split[1].split("\n\t")

						vals = inv_text_split[1].split("\n\t")
						print(vals)
						for val in vals[1:len(vals)]:
							val_split = val.split("probability: ")
							print("val_split: "+ str(val_split))
							val0 = val_split[0].strip()
							prob = val_split[1].split("\tcount:")
							prob0 = prob[0].replace(" probability: ", "")
							print(prob)
							count = prob[1].split(" total:")
							count0 = count[0]
							total0 = count[1].replace("\t", "")
							#total0 = total
							print("val:"+val0+" prob:"+prob0+" count:"+count0+" total:"+total0)
							val_elem = ET.SubElement(inv_elem, "VAL")
							val_elem.text = val0
							#print(ET.tostring(inv_elem))
							prob_elem = ET.SubElement(inv_elem, "PROBABILITY")
							prob_elem.text = prob0
							#print(ET.tostring(inv_elem))
							count_elem = ET.SubElement(val_elem, "COUNT")
							count_elem.text = count0
							#val_elem.append(count_elem)
							total_elem = ET.SubElement(val_elem, "TOTAL")
							total_elem.text = total0
							#val_elem.append(total_elem)
						m_elem.append(inv_elem)
				'''for var in typedict["h2m"]:
					if(var in child.find("PPTNAME").text):
						#print(var + " in " +child.find("PPTNAME").text)
						h2m_elem.append(child)
				for var in typedict["m2h"]:
					if(var in child.find("PPTNAME").text):
						#print(var + " in " +child.find("PPTNAME").text)
						m2h_elem.append(child)
				for var in typedict["other"]:
					if(var in child.find("PPTNAME").text):
						#print(var + " in " +child.find("PPTNAME").text)
						other_elem.append(child)'''
		#h_elem.append(ppt_name_h_elem)
		#h_elem.append(ppt_name_m_elem)
		#break
			
	regrouped_xml = h + "\n" + m + "\n" + h2m + "\n" + m2h + "\n" + h_m + "\n" + h_h2m + "\n" + h_m2h + "\n" + m_h2m + "\n" + m_m2h + "\n" + m2h_h2m + "\n" + other
	#ET.dump(new_root)
	print(ET.tostring(new_root))
	print(type(new_root))
	return new_tree


def main():
	global testing, topics, message_types, message_fields, bag_info
	global comparability_map, comparability_count
	start_time = time.time()

	#first arg: property file
	# second arg: 
	output_filename=sys.argv[2].split(".")
	xml_filehead=output_filename[0]

	#handle CL args
	regrouped_filename=output_filename[0]+"_regrouped.xml"

	#process var typespace xml
	print("Parsing "+str(sys.argv[1]))
	typespace_xml_tree = ET.parse(sys.argv[1])
	parse_typespace_xml(typespace_xml_tree)

	#process .inv xml
	xml_tree = ET.parse(sys.argv[2])
	regrouped_xml_string = restruct_xml(xml_tree)
	root = regrouped_xml_string.getroot()
	print(type(regrouped_xml_string.getroot()))
	print(type(regrouped_xml_string))
	'''regrouped_xml_file = file(regrouped_filename, "w")
	regrouped_xml_file.write(regrouped_xml_string)
	regrouped_xml_file.close()'''
	#regrouped_xml_string.write(regrouped_filename, encoding="utf-8", pretty_print=True)

	xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
	with open(regrouped_filename, "w") as f:
		f.write(xmlstr)
	print("Regrouped .xml file: "+regrouped_filename)

	#generate FSMs
	

if __name__ == "__main__":
    # execute only if run as a script 
    main()
