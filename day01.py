# imports
import re

# file prep
file = open('input/data01.txt', 'r')
lines = file.readlines()

# definitions
total_sum = 0

# calculations
for line in lines:
    # replace all written numbers with digits
    for x in range(5):
        if 'one' in line:
            line = line.replace('one', 'o1e')
        if 'two' in line:
            line = line.replace('two', 't2o')
        if 'three' in line:
            line = line.replace('three', 't3e')
        if 'four' in line:
            line = line.replace('four', '4')
        if 'five' in line:
            line = line.replace('five', '5e')
        if 'six' in line:
            line = line.replace('six', '6')
        if 'seven' in line:
            line = line.replace('seven', '7n')
        if 'eight' in line:
            line = line.replace('eight', 'e8t')
        if 'nine' in line:
            line = line.replace('nine', 'n9e')

    match1 = re.search(r'\d+', line) # searches for the first digit

    if match1:
        first_num = match1.group()

    all_matches = re.findall(r'\d+', line)

    if len(all_matches) == 1:
        if all_matches[0] == first_num[0]:
            # in case there is only 1 digit
            last_num = first_num[0]
        else:
            i = len(first_num) - 1
            last_num = first_num[i]
    else:
        match2 = re.match('.+([0-9])[^0-9]*$', line) # searches for the last digit

        if match2:
            last_num = match2.group(1)

    converted = int(''.join([first_num[0], last_num]))

    total_sum = total_sum + converted

print(f'The total sum is: {total_sum}')
