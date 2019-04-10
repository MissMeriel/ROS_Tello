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

def determine(xml_tree):
	comment_div = "<!-- ================= %s ================= -->" % "other"
	new_tree = ET.ElementTree()
	new_root = ET.Element('root')
	new_tree._setroot(new_root)
	root = xml_tree.getroot()
	for child in root.iter("PPT"):
		print(child.find("PPTNAME").text)
		ans = raw_input("Useful? y/n: ")
		if('n' in ans):
			root.remove(child)
	return xml_tree

def main():
	#first arg: property file
	# second arg: 
	output_filename=sys.argv[1].split(".")
	xml_filehead=output_filename[0]

	#handle CL args
	regrouped_filename=xml_filehead+"_usefulppts.xml"

	#process .inv xml
	print("Parsing "+str(sys.argv[1]))
	xml_tree = ET.parse(sys.argv[1])
	regrouped_xml_tree = determine(xml_tree)
	root = regrouped_xml_tree.getroot()
	#regrouped_xml_string.write(regrouped_filename, encoding="utf-8", pretty_print=True)

	xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
	with open(regrouped_filename, "w") as f:
		f.write(xmlstr)
	print("Regrouped .xml file: "+regrouped_filename)

if __name__ == "__main__":
    # execute only if run as a script 
    main()
