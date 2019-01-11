##TO RUN bag2daikon.py:
cd clean_bags
python bag2daikon.py demo1_2018-12-21-10-37-25.bag demo1_2018-12-21-10-37-25.xml


##TO RUN bag2daikon.py WITH PROFILING:
cd clean_bags
python -m cProfile -o prof.txt bag2daikon.py demo1_2018-12-21-10-37-25.bag demo1_2018-12-21-10-37-25.xml
python -m pstats prof.txt
help #will show list of available sorting commands


##TO GENERATE INVARIANTS WITH daikon INSTALLED:
java -cp $DAIKONDIR/daikon.jar daikon.Daikon --config_option daikon.derive.Derivation.disable_derived_variables=true demo1_2018-12-21-10-37-25.decls demo1_2018-12-21-10-37-25.dtrace
