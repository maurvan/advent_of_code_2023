# file prep
file = open('input/data06.txt', 'r')
lines = file.readlines()

# definitions
button = 0
i = 0
win = 0
win_amount = []

# calculations
time = lines[0].split() # make into list
distance = lines[1].split()

time.pop(0) # remove the first element
distance.pop(0)

time = list(map(int, time)) # convert elements to integer
distance = list(map(int, distance))

for races in time:
    while button < time[i]:
        travel = (time[i] - button) * button
        if travel > distance[i]: # check if the distance travelled is greater than the record
            win += 1
        button += 1
    button = 0 # reinitialize
    i += 1
    print(win)
    win_amount.append(win)
    win = 0

total = win_amount[0] * win_amount[1] * win_amount[2] * win_amount[3]

print(total)