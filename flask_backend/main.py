import flask
from flask import request
import numpy as np
import json

app = flask.Flask("__main__")


def make_move(player, col, board):
    # for easy column handling
    print(col)
    updated = False
    np_board = np.array(board)
    selected_col = np_board[:, col]
    print(selected_col)
    for i in range(len(selected_col) - 1):
        if selected_col[-1] == 0:
            selected_col[-1] = player
            updated = True
            break
        elif selected_col[i] == 0 and selected_col[i+1] != 0:
            selected_col[i] = player
            updated = True
            break

    np_board[:, col] = selected_col
    return np_board.tolist(), updated


def checkWinner(board, player):

    # boardHeight = len(board)
    # boardWidth = len(board[0])

    # check horizontal spaces
    for row in [0, 1, 2, 3, 4, 5]:
        for col in [0, 1, 2, 3]:
            if board[row][col] != 0 and \
               board[row][col] == board[row][col+1] and \
               board[row][col] == board[row][col+2] and \
               board[row][col] == board[row][col+3]:
                return True

    # check vertical spaces
    for row in [0, 1, 2]:
        for col in [0, 1, 2, 3, 4, 5, 6]:
            if board[row][col] != 0 and \
               board[row][col] == board[row+1][col] and \
               board[row][col] == board[row+2][col] and \
               board[row][col] == board[row+3][col]:
                return True

    # check diagonal spaces
    for row in [0, 1, 2]:
        for col in [0, 1, 2, 3]:
            if board[row][col] != 0 and \
               board[row][col] == board[row+1][col+1] and \
               board[row][col] == board[row+2][col+2] and \
               board[row][col] == board[row+3][col+3]:
                return True

    for row in [3, 4, 5]:
        for col in [0, 1, 2, 3]:
            if board[row][col] != 0 and \
               board[row][col] == board[row-1][col+1] and \
               board[row][col] == board[row-2][col+2] and \
               board[row][col] == board[row-3][col+3]:
                return True

    return False


@app.route('/evaluate_board_state', methods=['POST'])
def update_board():
    if not request.json:
        return {"error": "no request body"}

    data = request.json
    currentBoard = data['currentBoard']
    clickedColumn = data['column']
    player = data['player']
    new_board, updated = make_move(player, clickedColumn, currentBoard)
    winner = checkWinner(new_board, player)

    if winner:
        message = "Winner is Player {}".format(player)
    else:
        message = ""

    if player == "1":
        if updated:
            player = "2"
    elif player == "2":
        if updated:
            player = "1"

    compiled_results = {"board": new_board, "player": player, "winner": winner, "message": message}
    print(compiled_results)
    return json.dumps(compiled_results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
