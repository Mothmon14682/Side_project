import cv2
import math
import os
import time
import os.path
from playsound import playsound
import threading

ascii_map = " .:-=+*#%@"
VIDEO_NAME = "BadApple"

def reduce_size(width, height):
    MAX_WIDTH = 50
    MAX_HEIGHT = 50
    if width > MAX_WIDTH:
        return (MAX_WIDTH, int((width * MAX_HEIGHT)/height))
    if height > MAX_HEIGHT:
        return (int((height * MAX_WIDTH)/width), MAX_HEIGHT)
    return (width, height)
    

def gray_to_ascii(grayscale):
    percent = math.ceil((grayscale/255)*100 / 10)-1
    if percent <= 0:
        return " "
    return ascii_map[percent]

def img_to_ascii(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    width, height = reduce_size(gray.shape[0], gray.shape[1])
    gray = cv2.resize(gray, (width, height), interpolation= cv2.INTER_LINEAR)

    text = ""
    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):
            text += (gray_to_ascii(gray[i][j]))
        text += "/"
    return text

def render():
    video = cv2.VideoCapture(f"{VIDEO_NAME}.mp4")
    frames = []
    while True:
        ret, frame = video.read()
        if ret == True:
            frames.append(img_to_ascii(frame))
        else:
            break
    video.release()
    return frames

if os.path.exists(f"./{VIDEO_NAME}.txt"):
    with open(f"./{VIDEO_NAME}.txt", "r") as file:
        threading.Thread(target = playsound, args = ("/home/mothmon/Code/Python/Side_project/ascii-art/BadApple.mp3",)).start()
        for i in file.readlines():
            print(i.replace("/", "\n"), end = "\r", flush = True)
            time.sleep(33.15/1000)
else:
    frames = render()
    os.system("rm -rf *.txt || del *.txt")
    with open(f"./{VIDEO_NAME}.txt", "a") as file:
        threading.Thread(target = playsound, args = ("/home/mothmon/Code/Python/Side_project/ascii-art/BadApple.mp3",)).start()
        for i in range(len(frames)):
            print(frames[i].replace("/" , "\n"), end="\r", flush = True)
            print("", flush = True)
            time.sleep(33.15/1000)
            file.write(frames[i])
            file.write("\n")
