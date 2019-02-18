
import numpy as np
import csv
import os

# Import data

def main():
    filenames_path = "./data"
    filenames = [os.path.join(filenames_path, filename) for filename in os.listdir(filenames_path) if filename.endswith(".csv")]

    rows = [row for filename in filenames for row in file_rows(filename)]

    durations = [int(row[0]) for row in rows]
    start_times = [parse_timestr(row[1]) for row in rows]
    end_times = [parse_timestr(row[2]) for row in rows]
    #count_multiday_trips(start_times, end_times)
    # In fact, many people check out bikes late at night one day
    # and bike until the next day begins

    start_stations = [int(row[3]) for row in rows]
    end_stations = [int(row[5]) for row in rows]
    # note that stations get added to the program over time
    # columns 4,6 contain text representation of the numbers in columns 3,5

    bike_numbers = [bike_num(row[7]) for row in rows]
    # Some are None, the data is messy
    #assert_bike_numbers(bike_numbers)

    # Every membertype is "member"
    #member_types = [row[8] for row in rows]
    #assert_member_types(member_types)

def bike_num(s):
    if s[0] == "W" or s[0] == "w":
        return int(s[1:])
    return None

def count_multiday_trips(start_times, end_times):
    num = 0
    for a,b in zip(start_times, end_times):
        if a[0] != b[0]:
            num += 1
    print("The proportion of trips which are multiday is", num/len(start_times))

def assert_member_types(member_types):
    for type in member_types:
        assert type == "Member"

def assert_bike_numbers(bike_numbers):
    for number in bike_numbers:
        assert int(str(number)) == number

# Returns 2: date (str), time as # absolute seconds since midnight (int)
def parse_timestr(instr):
    instrs = instr.split(' ')
    # datestr, timestr
    h, m, s = instrs[1].split(':')
    return instrs[0], int(h) * 3600 + int(m) * 60 + int(s)

def file_rows(filename):
    with open(filename) as csvfile:
        rows = [row for row in csv.reader(csvfile)]
    # keys = rows[0]
    print(rows[0:5])
    return rows[1:]

if __name__ == "__main__":
    main()
