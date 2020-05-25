def getBoardDimensions(board):
    board_styles = board.get_attribute('style')
    board_width = board_styles.split('width: ')[1].split('px')[0]
    board_height = board_styles.split('height: ')[1].split('px')[0]

    return board_width, board_height


