#!/usr/bin/env python3

""" Data analysis program 2
"""

# 06/02/2017

book1 = [9, 27, 26, 19, 12, 7]
book2 = [4, 21, 30, 25, 18, 2]
books = (book1,book2)
for book in books:
    total = 0
    for rating in range(6):
       product = rating * book[rating]
       total = total + product
    average = total / 100
    print('average rating =', average)





