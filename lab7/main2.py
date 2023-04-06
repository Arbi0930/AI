#Манхаттан алслал:
import numpy as np

def manhattan_distance(x, y):
    return np.sum(np.abs(x-y))

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

distance = manhattan_distance(x, y)
print('Манхаттан алслал нь:', distance)

