#/usr/bin/python
import sys

def main():
	launch_filename=sys.argv[1]
	launch_file = open(launch_filename, 'w')
	print("Looking for nodes with "+launch_filename)


if __name__ == "__main__":
    # execute only if run as a script
    main()
