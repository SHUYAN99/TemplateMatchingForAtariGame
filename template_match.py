import cv2
import numpy as np

findCar = {
    (26, 26, 167) : 1,
    (101, 208, 158) : 2,
    (15, 105, 105) : 3,
    (128, 128, 240) : 4,
    (167, 26, 24) : 5,
    (33, 98, 162) : 6,
    (213, 92, 127) : 7,
    (50, 50, 184) : 8,
    (84, 183, 135) : 9,
    (64, 210, 210) : 10,
    (84, 252, 252) : 11,
}

#f= open("result.txt","a+")

#for num in range(1, 5):
    #img = cv2.imread('RZ_2464601_' + str(num) + '.png')
    img = cv2.imread('RZ_2464601_4667.png')

    height = img.shape[0]
    width = img.shape[1]

    # for bounding box
    startEndPair = [[0, 0, 0, 0],
    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    visited = [False, False, False, False, False,
                False, False, False, False, False]

    for i in range(height):
        for j in range(width):
            blue = img.item(i, j, 0)
            green = img.item(i, j, 1)
            red = img.item(i, j, 2)
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

    f.write(str(startEndPair) + '\n')

    img2 = img.copy()
    for pair in startEndPair:
        img2 = cv2.rectangle(img2, (pair[1],pair[0]), (pair[3], pair[2]), (255, 255, 255), 1)

    cv2.imwrite('result.png', img2)

#f.close()