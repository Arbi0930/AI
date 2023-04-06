import numpy as np

def euclidean_distance(x, y):
    return np.sqrt(np.sum(np.power((x-y), 2)))

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

distance = euclidean_distance(x, y)
print('Евклидийн алслал нь:', distance)