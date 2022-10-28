import os

def getPositionMultiple():
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    commands = open(input_path, 'r').read().split('\n')
    horizontal = 0
    depth = 0
    for command in commands:
        if not command: continue
        cd = command.split(' ')
        if cd[0] == 'forward':
            horizontal += int(cd[1])
        elif cd[0] == 'down':
            depth += int(cd[1])
        elif cd[0] == 'up':
            depth -= int(cd[1])

    return horizontal * depth

print(getPositionMultiple())