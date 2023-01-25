"""
Batch Process - first transformation

Reads from a file, transform, write to a new file.

In this case, covert degree F to degree C.

Note: 

This is a batch process, but the file objects we use are 
also called 'file-like objects' or 'streams'.

What makes streaming different is the input data is unbounded.

"""

import csv

# Declare a variable to hold the input file name
input_file_name = "NetFlix-original.csv"

# Declare a variable to hold the output file name
output_file_name = "out9.txt"

# Create a file object for input (r = read access)
input_file = open(input_file_name, "r")

# Create a file object for output (w = write access)
# On Windows, without newline='', 
# we'll get an extra line after each record
output_file = open(output_file_name, "w", newline='')

# Create a csv reader for a comma delimited file
reader = csv.reader(input_file, delimiter=",")

# Create a csv writer for a comma delimited file
writer = csv.writer(output_file, delimiter=",")

# Our file has a header row, move to next to get to data
header = next(reader)

# Write the header row to the output file
header_list = ["Year","Month","Day","Time","TempC"]
writer.writerow(header_list)

# Then, for each data row in the reader
for row in reader:

    # set local variables for each column in the row
    # note: the order of the columns is important
    #       and must match the order in the input file
    # We really only care about the temperature column
    Year, Month, Day, Time, TempF = row

    # convert the temperature from F to C
    # use the built-in round() function to round to 2 decimal places
    # use the built-in float() function to 
    # convert the string (as read) 
    # to a float (a floating point number) or decimal
    TempC = round((float(TempF) - 32.0) * 5.0 / 9.0,2)

    # put the values in a list (see the square brackets)
    # and write the list of values to the output file
    writer.writerow([Year, Month, Day, Time, TempC])

# close the file objects to release the resources
# this is important
# if not closed from this process, 
# you may not be able to move or delete the file 
output_file.close()
input_file.close()
