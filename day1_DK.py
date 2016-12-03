doc_from_elves = 'L1, L3, L5, L3, R1, L4, L5, R1, R3, L5, R1, L3, L2, L3, R2, R2, L3, L3, R1, L2, R1, L3, L2, R4, R2, L5, R4, L5, R4, L2, R3, L2, R4, R1, L5, L4, R1, L2, R3, R1, R2, L4, R1, L2, R3, L2, L3, R5, L192, R4, L5, R4, L1, R4, L4, R2, L5, R45, L2, L5, R4, R5, L3, R5, R77, R2, R5, L5, R1, R4, L4, L4, R2, L4, L1, R191, R1, L1, L2, L2, L4, L3, R1, L3, R1, R5, R3, L1, L4, L2, L3, L1, L1, R5, L4, R1, L3, R1, L2, R1, R4, R5, L4, L2, R4, R5, L1, L2, R3, L4, R2, R2, R3, L2, L3, L5, R3, R1, L4, L3, R4, R2, R2, R2, R1, L4, R4, R1, R2, R1, L2, L2, R4, L1, L2, R3, L3, L5, L4, R4, L3, L1, L5, L3, L5, R5, L5, L4, L2, R1, L2, L4, L2, L4, L1, R4, R4, R5, R1, L4, R2, L4, L2, L4, R2, L4, L1, L2, R1, R4, R3, R2, R2, R5, L1, L2'
data = doc_from_elves.split(sep=', ')

# global constant for keeping track of heading, clockwise
compass = ('N', 'E', 'S', 'W')

def change_heading(current_heading, turn):
    """returns new heading after turn L or R"""
    heading_index = compass.index(current_heading)
    if turn == 'L':
        new_bearing = compass[heading_index - 1] if heading_index > 0 else 'W'
    if turn == 'R':
        new_bearing = compass[heading_index + 1] if heading_index < 3 else 'N'
    return new_bearing


def calculate_waypoint(current_point, heading, steps):
    """Calculates waypoint in x,y coordinates, with x+ being N and y+ being E"""
    if heading == 'N':
        return(current_point[0] + steps, current_point[1])
    if heading == 'E':
        return(current_point[0], current_point[1] + steps)
    if heading == 'S':
        return(current_point[0] - steps, current_point[1])
    if heading == 'W':
        return(current_point[0], current_point[1] - steps)


current_heading = 'N'
manhattan = [0,0,0,0]
waypoints = [[0,0]]

for step in data:
    current_heading = change_heading(current_heading, step[0])
    for l in range(int(step[1:])):
        waypoints.append(calculate_waypoint(waypoints[-1], current_heading, 1))
    manhattan[compass.index(current_heading)] += int(step[1:])


blocks = abs(manhattan[0]-manhattan[2]) + abs(manhattan[1]-manhattan[3])

print(manhattan)
print('Number of blocks: {}'.format(blocks))

already_passed = []
for n in range(len(waypoints)):
    for m in range(n):
        if waypoints[m] == waypoints[n]:
            already_passed.append(waypoints[m])

print('Bunny HQ is at {} and {} blocks aways'.format(already_passed[0], (abs(already_passed[0][0]) + abs(already_passed[0][1]))))


