#!/bin/bash
rootdir='cleanbags_2_22'
demo='demo2'
for filename in $rootdir/*.bag; do
	echo "bag2daikon for "$filename
	python bag2daikon_compareunits.py $filename $demo/$demo'_user.xml'
	dtracefile="${filename//bag/dtrace}"
	declsfile="${filename//bag/decls}"
done
for filename in $rootdir/*.decls; do
	java -cp $DAIKONDIR/daikon.jar:${DAIKONDIR}/java/lib/*:${DAIKONDIR}/java daikon.Daikon --user-defined-invariant daikon.inv.unary.string.ProbabilisticString --user-defined-invariant daikon.inv.unary.scalar.ProbabilisticFloat --user-defined-invariant daikon.inv.unary.scalar.ProbabilisticScalar --user-defined-invariant daikon.inv.unary.stringsequence.ProbabilisticStringSequence $filename $rootdir/$demo*.dtrace -o $rootdir'/'$demo'_user_cleanbags_all.inv.gz'
	break
done
