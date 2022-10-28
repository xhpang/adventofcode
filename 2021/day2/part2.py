import os

def getPosistionMultiple2():
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    commands = open(input_path, 'r').read().split('\n')
    horizontal = 0
    depth = 0
    aim = 0
    for command in commands:
        if not command: continue
        cd = command.split(' ')
        x = int(cd[1])
        if cd[0] == 'forward':
            horizontal += x
            depth += aim * x
        elif cd[0] == 'down':
            aim += x
        elif cd[0] == 'up':
            aim -= x
    
    return horizontal * depth

print(getPosistionMultiple2())
