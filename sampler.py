#!/usr/bin/env python
import random
import csv
import sys

IN_FILE_PATH = "/home/wesley/Downloads/d3schools.csv"
SAMPLE_OUT_PATH = "/home/wesley/Downloads/sample_out.csv"
REST_OUT_PATH = "/home/wesley/Downloads/rest_out.csv"
SAMPLE_SIZE = 40

def main():
    """
    Take an input csv file with anything in the rows, and outputs two new
    csv files with a random sample in one file, and the remainder in the
    other file

    Syntax:
    >> python sampler.py sample_num /path/to/input.csv /path/to/sample_out.csv /path/to/rest_out.csv
    
    Otherwise, the default value of the sample size is SAMPLE_SIZE, and the
    output file defaults are SAMPLE_OUT_PATH and REST_OUT_PATH
    """
    try:
        # try to get the sample size/file input/file output from sys.argv
        SAMPLE_SIZE = int(sys.argv[1]) # first arg is the sample size
        IN_FILE_PATH = sys.argv[2] # second arg is the input file path
        SAMPLE_OUT_PATH = sys.argv[3] # third arg is the output file path for the random sample
        REST_OUT_PATH = sys.argv[4] # fourth arg is the output filepath for the rest after random sample is taken
    except KeyError:
        # if one or more of the argv's are missing
        print "To set your own arguments follow the syntax >> python sampler.py sample_num /path/to/input.csv /path/to/sample_out.csv /path/to/rest_out.csv"
    
    rows = get_rows_from_csv(IN_FILE_PATH)
    sample_indexes = get_random_sample_indexes(len(rows), SAMPLE_SIZE)
    write_sample_to_files(rows, SAMPLE_OUT_PATH, REST_OUT_PATH, sample_indexes)
    print "Done"
    
def get_rows_from_csv(file_path):
    reader = csv.reader(open(file_path, "rb"))
    rows = [row for row in reader]
    return rows

def get_random_sample_indexes(index_size, sample_size = SAMPLE_SIZE):
    print index_size, sample_size
    nums = random.sample(range(index_size), sample_size) 
    return nums

def write_sample_to_files(writable_rows, sample_file_path, rest_out_path, sample_indexes):
    sample_writer = csv.writer(open(sample_file_path, "wb"))
    rest_writer = csv.writer(open(rest_out_path, "wb"))
    for index in range(len(writable_rows)):
        if len(sample_indexes) == 0 or index not in sample_indexes:
            rest_writer.writerow(writable_rows[index])
            print "row %s written to REST" % str(index)
        else:
            sample_writer.writerow(writable_rows[index])
            sample_indexes.remove(index)
            print "row %s written to SAMPLE" % str(index)

if __name__ == "__main__":
    main()
