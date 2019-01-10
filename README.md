##TO RUN bag2daikon.py WITH PROFILING:
python -m cProfile -o prof.txt bag2daikon.py demo1_2018-12-21-10-37-25.bag
python -m pstats prof.txt
help
