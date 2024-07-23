from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Sele:
    def __init__(self, driver_path):
        chrome_service = webdriver.ChromeService(executable_path = driver_path)
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_experimental_option("detach", True)
        chrome_options.add_extension("./Extensions/gighmmpiobklfepjocnamgkkbiglidom.crx")
        self.__driver = webdriver.Chrome(service = chrome_service, options = chrome_options)
        self.__first_open = True

    def open(self, link):
        self.__driver.get(link)

    def search(self, video_name):
        search_bar = WebDriverWait(self.__driver, 20).until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )
        search_bar.send_keys(video_name)
        time.sleep(2)
        search_bar.send_keys(Keys.RETURN)

    def clearSearch(self):
        search_bar = WebDriverWait(self.__driver, 20).until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )
        time.sleep(1)
        search_bar.clear()

    def play_video(self, video_name):
        element = WebDriverWait(self.__driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[title = '{0}']".format(video_name)))
        )
        element.click()
        if self.__first_open == True:
            self.__first_open = False
            button = WebDriverWait(self.__driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-tooltip-target-id='ytp-autonav-toggle-button']"))
            )
            time.sleep(1)
            button.click()
        WebDriverWait(self.__driver, 20).until(
            EC.presence_of_element_located((By.ID, 'movie_player'))
        )
        while True:
            if self.__driver.execute_script("return document.getElementById('movie_player').getPlayerState()") == 0:
                return
            
    def getDriver(self):
        return self.__driver
    
    def quit(self):
        self.__driver.quit()

if __name__ == "__main__":
    Selenium = Sele(r"C:\Program Files (x86)\chromedriver.exe")
    Selenium.open("https://youtube.com")
    Selenium.search("The Amazing World Of Gumball - The Choices Song (Nicole Meets Richard)")
    Selenium.play_video("The Amazing World Of Gumball - The Choices Song (Nicole Meets Richard)")