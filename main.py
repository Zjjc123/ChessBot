from selenium import webdriver 
from stockfish import Stockfish
import re

browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://www.chess.com/play/computer")

board = browser.find_element_by_xpath('//*[@id="chessboard_boardarea"]')

board_styles = board.get_attribute('style')
board_width = board_styles.split('width: ')[1].split('px')[0]
board_height = board_styles.split('height: ')[1].split('px')[0]

print("Board Dimension: " + board_width + "x" + board_height)

