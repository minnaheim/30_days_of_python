import numpy as np
print(type([0, 1, 2, 3, 4, 5]))
print(type({'name': 'Minna',
            'age': '22'}))
print(type((1, 4, 5, 6, 3)))
print(type(10))

'''
<class 'list'>
<class 'dict'>
<class 'tuple'>
<class 'int'>
'''

# find euclidian distance
dist_1 = np.linalg.norm(2-3)
dist_2 = np.linalg.norm(10-8)
print(dist_1, dist_2)
# 1.0 2.0
