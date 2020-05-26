import numpy as np

piecesDictionary = {
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wp.png": "whitePawn",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wr.png": "whiteRook",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wn.png": "whiteKnight",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wb.png": "whiteBishop",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wq.png": "whiteQueen",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/wk.png": "whiteKing",

    "images.chesscomfiles.com/chess-themes/pieces/neo/150/bp.png": "blackPawn",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/br.png": "blackRook",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/bn.png": "blackKnight",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/bb.png": "blackBishop",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/bq.png": "blackQueen",
    "images.chesscomfiles.com/chess-themes/pieces/neo/150/bk.png": "blackKing"
}

def getBoardState(pElement):
    boardState = np.zeros(dtype="S12", shape=(8, 8))
    pieces = pElement.find_elements_by_xpath(".//*")

    for piece in pieces:
        image = piece.get_attribute('style')
        imageURL = image.split('//')[1].split('")')[0]
        position = piece.get_attribute('class').split('square-')[1]

        # print(piecesDictionary[imageURL] + ": " + position[1] + ',' + position[3])

        x = int(position[1])
        y = int(position[3])

        boardState[y - 1][x - 1] = piecesDictionary[imageURL]

    print(boardState)

