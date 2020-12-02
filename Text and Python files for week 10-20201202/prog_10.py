#!/usr/bin/env python3

""" Data analysis program 10
"""

# 18/02/2017

from table_utils import *

# Load geog_1.txt data into table1
table1 = load('geog_1.txt')

table2 = filter_by('.92',0,table1)

table3 = to_float(table2)

table4 = sort_by(8,table3)
print(table4)



