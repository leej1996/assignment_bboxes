import numpy as np
import cv2 as cv

# List of image names
img_list = ['000005.png','000009.png','000010.png','000011.png','000014.png']

# Create array from annotations.txt to keep information for drawing of rectangles
annotations = np.zeros((5,9))
i = 0
with open("annotations.txt", "r") as a_file:
    for line in a_file:
        # strip each line, remove name of image and then create an numpy array to store information
        stripped_line = line.strip()
        stripped_list = np.array(stripped_line.lstrip(img_list[i]).split())
        # Append zeros to end if size is too small (need size 9 array for each row)
        if stripped_list.size == 5:
            stripped_list = np.append(stripped_list,[0,0,0,0])
        annotations[i] = stripped_list
        i += 1

annotations = annotations.astype(np.int32)

# Iterate through all images, and draw rectangles based off of annotations.txt
i = 0
for name in img_list:
    img = cv.imread("images/" + name)
    # Check if we draw one or two rectangles, then draw them in green and red (for second one)
    if annotations[i][0] == 1:
        cv.rectangle(img,(annotations[i][1],annotations[i][2]),(annotations[i][3],annotations[i][4]),(0,255,0),3)
    else:
        cv.rectangle(img,(annotations[i][1],annotations[i][2]),(annotations[i][3],annotations[i][4]),(0,255,0),3)
        cv.rectangle(img,(annotations[i][5],annotations[i][6]),(annotations[i][7],annotations[i][8]),(255,0,0),3)
    cv.imshow(name,img)
    cv.waitKey(0)
    i += 1
