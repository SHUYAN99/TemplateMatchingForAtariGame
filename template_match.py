#!/usr/bin/env python
# coding: utf-8

# In[85]:


import cv2
import numpy as np

findCar = {
    (26, 26, 167) : 1,
    (117, 231, 180) : 2,
    (15, 105, 105) : 3,
    (128, 128, 240) : 4,
    (167, 26, 24) : 5,
    (33, 98, 162) : 6,
    (213, 92, 127) : 7,
    (50, 50, 184) : 8,
    (84, 183, 135) : 9,
    (64, 210, 210) : 10,
}

img = cv2.imread('RZ_2464601_1.png')

#get out the two dashed lines in the center
lines = cv2.inRange(img, np.array([84, 252, 252]), np.array([84, 252, 252]))

#real on-going game image
imgR = cv2.imread('RZ_2464601_4625.png')

# for bounding box
startEndPair = [[0, 0, 0, 0],
[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# last one in above array for chicken
visited = [False, False, False, False, False,
            False, False, False, False, False]

#get out the two dashed lines + chicken in the center
lineAndChicken = cv2.inRange(imgR, np.array([84, 252, 252]), np.array([84, 252, 252]))

#get the chicken
chicken = cv2.subtract(lineAndChicken, lines)
#chicken = lineAndChicken - lines

#find chicken coordinates
chickenPos = cv2.findNonZero(chicken)
startEndPair[10][0] = chickenPos[0][0][1]
startEndPair[10][1] = chickenPos[0][0][0]
startEndPair[10][2] = chickenPos[0][0][1]
startEndPair[10][3] = chickenPos[0][0][0]
for i in range(len(chickenPos)):
    if (chickenPos[i][0][1] < 187):
        if (chickenPos[i][0][0] < startEndPair[10][1]):
            startEndPair[10][1] = chickenPos[i][0][0]
        if (chickenPos[i][0][1] > startEndPair[10][2]):
            startEndPair[10][2] = chickenPos[i][0][1]
        if (chickenPos[i][0][0] > startEndPair[10][3]):
            startEndPair[10][3] = chickenPos[i][0][0]


height = imgR.shape[0]
width = imgR.shape[1]

for i in range(height):
    for j in range(width):
        blue = imgR.item(i, j, 0)
        green = imgR.item(i, j, 1)
        red = imgR.item(i, j, 2)
        BGR = (blue, green, red)
        if BGR in findCar:
            carNum = findCar[BGR]
            if (visited[carNum - 1] == False):
                startEndPair[carNum - 1][0] = i
                startEndPair[carNum - 1][1] = j
                visited[carNum - 1] = True
            else:
                startEndPair[carNum - 1][2] = i
                startEndPair[carNum - 1][3] = j
        else:
            # key is not present
            pass

for i in range(len(visited)):
    if (visited[i] == False):
        startEndPair[i] = [-1, -1, -1, -1]

#f.write(str(startEndPair) + '\n')

img2 = imgR.copy()
for pair in startEndPair:
    img2 = cv2.rectangle(img2, (pair[1]-1,pair[0]-1), (pair[3]+1, pair[2]+1), (255, 255, 255), 1)
print(startEndPair)
cv2.imwrite('RESULT_4625.png', img2)
#f.close()
