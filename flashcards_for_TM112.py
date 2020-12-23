'''flashcards_for_TM112.py
Flashcard program
 user selects a word from glossary
 outputs glossary definition'''

from random import *
import csv

def flashcard_function():
    show_flashcard = True
    while show_flashcard == True:
        user = input('Enter s to show flashcard q to quit: ')
        if user == 's':
            random_choice = choice(list(glossary))
            print(random_choice)
            input('Press enter to view definition:')
            print(glossary[random_choice])
        else:
            show_flashcard = False
def file_to_dictionary(filename):
    '''return a dictionary with the contents of a file
    '''
    file = open(filename,'r')
    reader = csv.reader(file)
    dictionary = {}
    for row in reader:
        dictionary[row[0]] = row[1]
    return dictionary

#initiate glossary as dictionary
glossary = file_to_dictionary('TM112_Glossary.txt')

#show flashcard
flashcard_function()





