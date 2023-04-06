#Косайн зай:

import numpy as np

def cosine_distance(x, y):
    numerator = np.dot(x, y)
    denominator = np.sqrt(np.dot(x, x)) * np.sqrt(np.dot(y, y))
    return 1 - (numerator / denominator)

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

distance = cosine_distance(x, y)
print('Косайн зай нь:', distance)