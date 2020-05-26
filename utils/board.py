import numpy as np
from selenium.webdriver.common.action_chains import ActionChains

piecesDictionary = {
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wp.png": "P",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wr.png": "R",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wn.png": "N",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wb.png": "B",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wq.png": "Q",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wk.png": "K",

    "images.chesscomfiles.com/chess-themes/pieces/neo/150/bp.png": "p",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/br.png": "r",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/bn.png": "n",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/bb.png": "b",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/bq.png": "q",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/bk.png": "k"
}

whiteCoordinate = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "e" : 5,
    "f" : 6,
    "g" : 7,
    "h" : 8,
}

blackCoordinate = {
    "a" : 8,
    "b" : 7,
    "c" : 6,
    "d" : 5,
    "e" : 4,
    "f" : 3,
    "g" : 2,
    "h" : 1,
}


class Board:
    def __init__(self, pElement):
        boardState = np.full(fill_value="_", shape=(8, 8))
        pieces = pElement.find_elements_by_xpath(".//*")

        for piece in pieces:
            image = piece.get_attribute('style')
            imageURL = image.split('//')[1].split('")')[0]
            position = piece.get_attribute('class').split('square-')[1]

            # print(piecesDictionary[imageURL] + ": " + position[1] + ',' + position[3])

            x = int(position[1])
            y = int(position[3])

            boardState[y - 1][x - 1] = piecesDictionary[imageURL]
        self.state = boardState
        self.count = len(pieces)

def getBoardDimensions(board):
    board_styles = board.get_attribute('style')
    board_size = board_styles.split('width: ')[1].split('px')[0]

    return int(board_size)

def getFENPosition(board, side):
    fen = ""
    emptyCount = 0
    for row in reversed(board.state):
        for piece in row:
            # if piece is not empty
            if (piece != '_'):
                # add the number empty and reset counter
                if (emptyCount > 0):
                    fen += str(emptyCount)
                    emptyCount = 0
                # add the piece
                fen += piece
            else:
                emptyCount += 1
        if (emptyCount > 0):
            fen += str(emptyCount)
            emptyCount = 0
        fen += "/"
        # remove extra slash
    return fen[:-1] + ' ' + side + ' KQkq - 0 1'

def executeMove(move, side, driver):
    start = move[:2]
    end = move[2:]

    board = driver.find_element_by_xpath('//*[@id="game-board"]')

    size = getBoardDimensions(board)
    multiplier = size / 8

    action = ActionChains(driver)

    action.move_to_element_with_offset(board, 0, 0).perform()

    if (side == 'w'):
        # Calculate start coordinate
        xStart = whiteCoordinate[start[0]] * multiplier - multiplier/2
        yStart = (9 - int(start[1])) * multiplier - multiplier/2

        # Calculate end coordinate
        xEnd = whiteCoordinate[end[0]] * multiplier - multiplier/2
        yEnd = (9 - int(end[1])) * multiplier - multiplier/2

        # Grab
        action.move_by_offset(xStart, yStart).click().perform()
        # Reset to bottom left
        action.move_to_element_with_offset(board, 0, 0).perform()
        # Move and drop
        action.move_by_offset(xEnd, yEnd).click().perform()
    else:
        # Calculate start coordinate
        xStart = blackCoordinate[start[0]] * multiplier - multiplier/2
        yStart = int(start[1]) * multiplier - multiplier/2

        # Calculate end coordinate
        xEnd = blackCoordinate[end[0]] * multiplier - multiplier/2
        yEnd = int(end[1]) * multiplier - multiplier/2

        # Grab
        action.move_by_offset(xStart, yStart).click().perform()
        # Reset to bottom left
        action.move_to_element_with_offset(board, 0, 0).perform()
        # Move and drop
        action.move_by_offset(xEnd, yEnd).click().perform()

