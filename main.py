from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from stockfish import Stockfish

from utils import board, turn

import re
import time

browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://www.chess.com/live")

usernameField = browser.find_element_by_xpath('//*[@id="username"]')
passwordField = browser.find_element_by_xpath('//*[@id="password"]')

f = open('login.txt')

username = f.readline().rstrip()
password = f.readline().rstrip()


usernameField.send_keys(username)
passwordField.send_keys(password)
passwordField.send_keys(Keys.ENTER)

time.sleep(0.5)

# Play Tab
browser.find_element_by_css_selector('li[data-tab="challenge"]').click()

time.sleep(0.5)

# Vs Computer
challengeMenu = browser.find_elements_by_class_name("challenge-menu-item")
for menu in challengeMenu:
    if (menu.text.rstrip() == "vs Computer"):
        menu.click()
        break

time.sleep(0.5)

# Vs Stocfish
botMenu = browser.find_elements_by_class_name("vs-computer-row")
for menu in botMenu:
    bot = menu.find_elements_by_class_name("user-tagline-username")
    if (bot[0].text == "stockfish"):
        menu.click()
        break

# Play Button
browser.find_element_by_xpath('//*[@id="board-layout-sidebar"]/div/div[1]/div[1]/div[2]/button').click()

boardElement = browser.find_element_by_xpath('//*[@id="game-board"]')
width, height = board.getBoardDimensions(boardElement)

print("Board Dimension: " + width + "x" + height)

while (True):
    WebDriverWait(browser, 100).until(turn.waitContains('//*[@id="board-layout-player-bottom"]/div/div[3]', 'class', 'clock-playerTurn'))

    print('Player Turn')


'''
stockfish = Stockfish("stockfish.exe")

print(stockfish.get_best_move())

stockfish.set_position(["e3"])

print(stockfish.get_best_move())
'''