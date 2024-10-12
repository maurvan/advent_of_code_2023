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

time = int(''.join(time)) # merge all elements into one
distance = int(''.join(distance))

while button < time:
    travel = (time - button) * button
    if travel > distance: # check if the distance travelled is greater than the record
        win += 1
    button += 1

print(win)
