#!/bin/bash



#for D in `find . -type d`; do
#for D in './driving_sim/backtracking_10/S*/'; do
#alias daikon-print-xml='java -cp $DAIKONDIR/daikon.jar:${DAIKONDIR}/java/lib/*:${DAIKONDIR}/java daikon.PrintInvariants --wrap_xml'
for D in `find ./driving_sim/PreProcess/ -mindepth 1 -maxdepth 1 -type d`; do
	#echo ${D} "all files in D"
	if [ -d ${D} ]; then
		#echo $D "is directory"
		mkdir $D/new_inv.gz
		for D2 in "${D}"; do
			if [ -d ${D2} ]; then
				#echo $D2 "is directory"
				for filename in $D/decls/*; do
					#if [ -d ${filename} ]; then
						echo ""
						echo "Running diakon for "$filename"" #$filename "is directory"
						dtracefile="${filename//decls/dtrace}"
						outfilebase="${filename/decls/new_inv.gz}"
						txtfile="${outfilebase/decls/txt}"
						xmlfile="${outfilebase/decls/xml}"
						invfile="${outfilebase/decls/inv.gz}"
						#echo $outfile
						#java -cp $DAIKONDIR/daikon.jar:${DAIKONDIR}/java/lib/*:${DAIKONDIR}/java daikon.Daikon --config_option daikon.inv.Invariant.confidence_limit=0.95 --config_option daikon.inv.filter.UnjustifiedFilter.enabled=false --config_option daikon.inv.filter.OnlyConstantVariablesFilter.enabled=false --config_option daikon.inv.unary.scalar.UpperBound.maximal_interesting=10000 --config_option daikon.inv.unary.scalar.UpperBound.minimal_interesting=-10000 --config_option daikon.inv.unary.scalar.LowerBound.maximal_interesting=10000 --config_option daikon.inv.unary.scalar.LowerBound.minimal_interesting=-10000  --config_option daikon.derive.Derivation.disable_derived_variables=true --user-defined-invariant daikon.inv.unary.string.ProbabilisticString --user-defined-invariant daikon.inv.unary.scalar.ProbabilisticFloat --user-defined-invariant daikon.inv.unary.scalar.ProbabilisticScalar --user-defined-invariant daikon.inv.unary.stringsequence.ProbabilisticStringSequence  $filename $dtracefile -o $invfile #"$(basename "$filename" .txt).decls " "$filename"
						#echo "Printing TXT invariants for "$invfile"" #$filename "is directory"
						#echo $invfile
						#java -cp $DAIKONDIR/daikon.jar:${DAIKONDIR}/java/lib/*:${DAIKONDIR}/java daikon.PrintInvariants $invfile > $txtfile
						#echo $textout > $txtfile
						echo "Printing XML invariants for "$invfile"" #$filename "is directory"
						#daikon-print-xml $outfile > $xmlfile
						arg="--wrap_xml "$outfile
						java -cp $DAIKONDIR/daikon.jar:${DAIKONDIR}/java/lib/*:${DAIKONDIR}/java daikon.PrintInvariants --wrap_xml $invfile > $xmlfile
						#echo "${xmlout}" > $xmlfile
					#fi
				done
			fi
		done
	fi
done


