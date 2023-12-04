# file prep
file = open('input/data02.txt', 'r')
lines = file.readlines()

# definitions
groups = []
all_numbers = []
np = 'PASS'
total = 0
count = 0

# calculations
for line in lines:
    chunks = line.split() # split into separate chunks
    games = line.split('Game ') # splits every line into a list
    count += 1

    for i in range(0, len(chunks), 2):
        groups.append(chunks[i:i+2]) # group 2 chunks together so we get "[amount, type]"

        for x in range(len(groups)):
            if groups[x][0] == 'Game':
                continue # skip if it says game
            elif ':' in groups[x][0]:
                continue # skip if it's game number
            else:
                all_numbers = groups[x][0] # store all the rest
                
        for number in all_numbers:
            if len(all_numbers) == 2:
                if 'red' in groups[x][1] and groups[x][0] > '12':
                    games.append(np) # adds PASS at the end of group where red has more than 12 cubes
                if 'green' in groups[x][1] and groups[x][0] > '13':
                    games.append(np) # adds PASS at the end of group where green has more than 13 cubes
                if 'blue' in groups[x][1] and groups[x][0] > '14':
                    games.append(np) # adds PASS at the end of group where blue has more than 14 cubes
    
    if 'PASS' in games:
        continue # skip games with too many cubes

    if count == 100:
        total = total + int(games[1][:3])
    else:
        total = total + int(games[1][:2])

print(f'The total sum of possible games is: {total}')
