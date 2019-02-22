#!/bin/bash

rootdir='./driving_sim/PreProcess'
outfilebase=$rootdir/new_inv.gz/all/
echo $outfilebase
mkdir -p $outfilebase
for D in `find ${rootdir} -mindepth 1 -maxdepth 1 -type d`; do
	#echo ${D} "all files in D"
	if [ -d ${D} ]; then
		#echo $D "is directory"
		for D2 in "${D}"; do
			if [ -d ${D2} ]; then
				#echo $D2 "is directory"
				for filename in $D/decls/*; do
					#echo ""
					#echo "Running diakon for "$filename"" #$filename "is directory"
					dtracefile=$rootdir/S*/dtrace/*
					#outfilebase="${filename/decls/new_inv.gz\/all}"
					txtfile="${outfilebase/decls/txt}"
					xmlfile="${outfilebase/decls/xml}"
					decls_base=$(basename "$filename" )
					invfile=$outfilebase"${decls_base/decls/inv.gz}"
					#echo $invfile #$outfilebase $(basename "$filename" )
					java -cp $DAIKONDIR/daikon.jar:${DAIKONDIR}/java/lib/*:${DAIKONDIR}/java daikon.Daikon --config_option daikon.inv.Invariant.confidence_limit=0.95 --config_option daikon.inv.filter.UnjustifiedFilter.enabled=false --config_option daikon.inv.filter.OnlyConstantVariablesFilter.enabled=false --config_option daikon.inv.unary.scalar.UpperBound.maximal_interesting=10000 --config_option daikon.inv.unary.scalar.UpperBound.minimal_interesting=-10000 --config_option daikon.inv.unary.scalar.LowerBound.maximal_interesting=10000 --config_option daikon.inv.unary.scalar.LowerBound.minimal_interesting=-10000  --config_option daikon.derive.Derivation.disable_derived_variables=true --user-defined-invariant daikon.inv.unary.string.ProbabilisticString --user-defined-invariant daikon.inv.unary.scalar.ProbabilisticFloat --user-defined-invariant daikon.inv.unary.scalar.ProbabilisticScalar --user-defined-invariant daikon.inv.unary.stringsequence.ProbabilisticStringSequence  $filename $dtracefile -o $invfile #"$(basename "$filename" .txt).decls " "$filename"
					echo "Printing TXT invariants for $invfile" #$filename "is directory"
					#echo $invfile
					java -cp $DAIKONDIR/daikon.jar:${DAIKONDIR}/java/lib/*:${DAIKONDIR}/java daikon.PrintInvariants $invfile > $txtfile
					#echo $textout > $txtfile
					echo 'Printing XML invariants for '$invfile #$filename "is directory"
					java -cp $DAIKONDIR/daikon.jar:${DAIKONDIR}/java/lib/*:${DAIKONDIR}/java daikon.PrintInvariants --wrap_xml $invfile > $xmlfile
					#break	
				done
			fi
		done
	fi
done


