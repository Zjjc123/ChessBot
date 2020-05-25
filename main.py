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

time.sleep(2)
browser.find_element_by_xpath('//*[@id="board-layout-sidebar"]/div/div[1]/ul/li[2]').click()

browser.find_element_by_name('//*[@id="board-layout-sidebar"]/div/div[1]/div[1]/div[2]/a[2]').click()

time.sleep(1)

vsBot = browser.find_element_by_xpath('//*[@id="board-layout-sidebar"]/div/div[1]/div[1]/div/a[88]').click()

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