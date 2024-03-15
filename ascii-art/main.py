import cv2
import math

MAX_WIDTH = 200
MAX_HEIGHT = 150
ascii_map = " .:-=+*#%@"

def reduce_size(width, height):
    if width > MAX_WIDTH:
        return (MAX_WIDTH, int((width * MAX_HEIGHT)/height))
    if height > MAX_HEIGHT:
        return (int((height * MAX_WIDTH)/width), MAX_HEIGHT)
    return (width, height)
    

def gray_to_ascii(grayscale):
    percent = math.ceil((grayscale/255)*100 / 10)-1
    return ascii_map[percent]

gray = cv2.cvtColor(cv2.imread("csc.jpg"), cv2.COLOR_BGR2GRAY)
width, height = reduce_size(gray.shape[0], gray.shape[1])
gray = cv2.resize(gray, (width, height), interpolation= cv2.INTER_LINEAR)

for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        print(gray_to_ascii(255 - gray[i][j]), end="")
    print()



cv2.imshow("Hello", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()