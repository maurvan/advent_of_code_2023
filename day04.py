# imports
import re

# file prep
file = open('input/data04.txt', 'r')
lines = file.read().strip().split('\n')

# definitions
i = 0
bingo = []
total = 0

# calculations
for line in lines:
    # split every line into specific type
    cards = line[0:9]
    winning = line[10:39]
    numbers = line[42:]

    # splits into list
    winning_all = re.split(r' ', winning)
    numbers_all = re.split(r' ', numbers) 

    # removes empty strings from list
    winning_all = list(filter(None, winning_all)) 
    numbers_all = list(filter(None, numbers_all))

    # loop that checks if numbers match
    while i < len(winning_all):
        if winning_all[i] in numbers_all:
            bingo.append(winning_all[i]) # adds numbers that match into new list
        i += 1

    if len(bingo) == 0:
        points = 0
    elif len(bingo) == 1:
        points = 1
    else:
        points = 1 * (2 ** (len(bingo) - 1))

    total = total + points

    # reset everything
    bingo.clear()
    i = 0

print(total)
