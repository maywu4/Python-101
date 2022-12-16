# Track The Robot
# A robot has been given a list of movement instructions. Each instruction is either left, right, up or down, followed by a distance to move. The robot starts at [0, 0]. You want to calculate where the robot will end up and return its final position as a list. For example, if the robot is given the instructions ["right 10", "up 50", "left 30", "down 10"], it will end up 20 left and 40 up from where it started, so you should return [-20, 40].

def track_robot(list):
    coordinates = [0,0]
    for step in list:
        stepLst = step.split(' ')
        direction, amount = stepLst
        if direction == 'right':
            coordinates[0] += int(amount)
        elif direction == 'left':
            coordinates[0] -= int(amount)
        elif direction == 'up':
            coordinates[1] += int(amount)
        elif direction == 'down':
            coordinates[1] -= int(amount)
    return coordinates


print(track_robot(["right 10", "up 50", "left 30", "down 10"]))
# Prints [-20, 40]

print(track_robot([]))
# Prints [0, 0]
# If there are no instructions, the robot doesn't move.

print(track_robot(["right 100", "right 100", "up 500", "up 10000"]))
# Prints [200, 10500]