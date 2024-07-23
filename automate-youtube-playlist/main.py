import sele
import random

Selenium = sele.Sele(r"C:\Program Files (x86)\chromedriver.exe")
Selenium.open("https://youtube.com")

videos = {}
nums_of_song = 0
with open("videos.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        line = line.replace("\n", "")
        nums_of_song += 1
        videos[line] = False

while nums_of_song > 0:
    choice = random.choice(list(videos.keys()))
    if videos[choice] == False:
        videos[choice] = True
        nums_of_song -= 1
        print(choice)
        Selenium.search(choice)
        Selenium.clearSearch()
        Selenium.play_video(choice)