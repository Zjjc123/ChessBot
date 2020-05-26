import numpy as np

piecesDictionary = {
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wp.png": "wp",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wr.png": "wr",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wn.png": "wn",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wb.png": "wb",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wq.png": "wq",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wk.png": "wk",

    "images.chesscomfiles.com/chess-themes/pieces/neo/150/bp.png": "bp",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/br.png": "br",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/bn.png": "bn",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/bb.png": "bb",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/bq.png": "bq",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/bk.png": "bk"
}


class Board:
    def __init__(self, pElement):
        boardState = np.full(fill_value="em", shape=(8, 8))
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

        print(self.state)


'''
def boardToFEN(board):
    fen = ""
    for piece in board:
'''
