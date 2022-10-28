import os

def getIncreasingMeasurements():
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    data = open(input_path, 'r').read().split('\n')
    depth_list = [int(i) for i in data if i]
    
    res = 0;
    for i in range(1, len(depth_list)):
        if depth_list[i] > depth_list[i - 1]:
            res += 1

    return res

print(getIncreasingMeasurements())