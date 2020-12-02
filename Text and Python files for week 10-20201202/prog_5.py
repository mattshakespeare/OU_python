#!/usr/bin/env python3

""" Data analysis program 5
"""

# 06/02/2017
from table_utils import *
import csv

file = open('happ_1.txt', 'r')
table =[]
reader = csv.reader(file)
for row in reader:
    table.append(row)
    print(row)
print(table)
table2 = rows(table,1,11)
table3 = cols(table2,1,4)
table4 = flip(table3)
table5 = to_float(table4)
print(table5)






