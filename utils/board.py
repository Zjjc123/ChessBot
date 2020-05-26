import numpy as np

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


def boardToFEN(board, side):
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
