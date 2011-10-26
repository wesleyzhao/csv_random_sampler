#!/usr/bin/env python
import random
import csv
import sys

IN_FILE_PATH = "example_files/d3schools.csv"
SAMPLE_OUT_PATH = "example_files/sample_out.csv"
REST_OUT_PATH = "example_files/rest_out.csv"
SAMPLE_SIZE = 40
SPORTS = ["Men's Baseball",
          "Men's Basketball",
          "Men's Cross Country",
          "Men's Football",
          "Men's Golf",
          "Men's Lacrosse",
          "Men's Rowing/Crew",
          "Men's Swim & Dive",
          "Men's Tennis",
          "Men's Track & Field",
          "Men's Wrestling",
          "Women's Basketball",
          "Women's Cross Country",
          "Women's Field Hockey",
          "Women's Golf",
          "Women's Gymnastics",
          "Women's Lacrosse",
          "Women's Rowing/Crew",
          "Women's Soccer",
          "Women's Softball",
          "Women's Swim & Dive",
          "Women's Tennis",
          "Women's Track & Field",
          "Women's Volleyball"]

def main():
    """
    Take an input csv file with anything in the rows, and outputs two new
    csv files with a random sample in one file, and the remainder in the
    other file

    Syntax: 
    >> python sampler.py sample_num /path/to/input.csv /path/to/sample_out.csv /path/to/rest_out.csv
    
    Otherwise, the default value of the sample size is SAMPLE_SIZE, and the
    output file defaults are SAMPLE_OUT_PATH and REST_OUT_PATH.
    """
    try:
        # try to get the sample size/file input/file output from sys.argv
        SAMPLE_SIZE = int(sys.argv[1]) # first arg is the sample size
        IN_FILE_PATH = sys.argv[2] # second arg is the input file path
        SAMPLE_OUT_PATH = sys.argv[3] # third arg is the output file path for the random sample
        REST_OUT_PATH = sys.argv[4] # fourth arg is the output filepath for the rest after random sample is taken
    except IndexError:
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

def randomize_sheet(in_file, out_file):
    rows = get_rows_from_csv(in_file)
    writer = csv.writer(open(out_file, "wb"))
    rand_nums = get_random_sample_indexes(len(rows), len(rows))
    for num in rand_nums:
        writer.writerow(rows[num])

def make_sports_sheet(in_file, out_file, column_num = 2):
    # column_num is after which column you want to add the sports in
    # default is after column 2 (columns start at 0). Use 0 if you want
    # it to be the first column
    if column_num < 0:
        raise Exception("column_num cannot be less than 0")

    rows = get_rows_from_csv(in_file)
    writer = csv.writer(open(out_file, "wb"))
    
    for row in rows[0:2]:
        for sport in SPORTS:
            sport_row = row[:] # have to return new row, otherwise editing sport_row will edit row... not good
            sport_row.insert(column_num, sport)
            print row, sport_row
            writer.writerow(sport_row)


if __name__ == "__main__":
    main()
