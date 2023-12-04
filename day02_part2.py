# imports
import re

# file prep
file = open('input/data02.txt', 'r')
lines = file.read().strip().split('\n')

# definitions
highestRed = 1
highestGreen = 1
highestBlue = 1
total = 0

# calculations
for line in lines:
    chunks = re.split(r'[:;,]', line)

    for chunk in chunks:

        if 'Game' in chunk:
            newList = [] # creates new list for each game

            # reset
            highestRed = 1
            highestGreen = 1
            highestBlue = 1
        else:         
            newList.append(chunk)

            for elem in newList:
                if 'red' in elem:
                    item = elem.strip().split()
                    if highestRed < int(item[0]):
                        highestRed = int(item[0])
                    else:
                        continue
                if 'green' in elem:
                    item = elem.strip().split()
                    if highestGreen < int(item[0]):
                        highestGreen = int(item[0])
                    else:
                        continue
                if 'blue' in elem:
                    item = elem.strip().split()
                    if highestBlue < int(item[0]):
                        highestBlue = int(item[0])
                    else:
                        continue
    
    pwr = highestRed * highestGreen * highestBlue
    total = total + pwr

print(total)
