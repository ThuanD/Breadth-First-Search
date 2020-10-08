import numpy as np
import collections

# read files
def readFile(testcase_file):
    matrix  = np.loadtxt(testcase_file, delimiter = " ", dtype = int)
    return matrix

# shortest path
def bfs(matrix, start, wall, goal):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if matrix[x][y] == goal:
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < len(matrix) and 0 <= y2 < len(matrix[0]) and matrix[x2][y2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    return path

# save files
def createResult(result_file, matrix, path):
    result = np.array(matrix, copy = True).astype(str)
    if result[path[-1]] == '2':
        for i in range(0, len(path) - 1):
            result[path[i]] = '-'
            np.savetxt(result_file, result, fmt = '%s')
    else:
        result = "None"
        open(result_file, 'w').write(result)
for i in range(1, 7):
    testcase_file = 'testcase{}.txt'.format(i)
    result_file = 'result{}.txt'.format(i)
    matrix = readFile(testcase_file)
    path = bfs(matrix, (0, 0), 0, 2)
    createResult(result_file, matrix, path)
