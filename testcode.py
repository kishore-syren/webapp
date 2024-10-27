from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize game board
board = [' ' for _ in range(9)]
current_player = 'X'


def check_winner(b, player):
    # Winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_combinations:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] == player:
            return True
    return False


@app.route("/", methods=["GET", "POST"])
def index():
    global board, current_player

    if request.method == "POST":
        position = int(request.form["position"])
        if board[position] == ' ':
            board[position] = current_player
            if check_winner(board, current_player):
                winner = current_player
                board = [' ' for _ in range(9)]
                return render_template("index.html", board=board, winner=winner)
            current_player = 'O' if current_player == 'X' else 'X'

        if ' ' not in board:
            board = [' ' for _ in range(9)]  # Reset board
            return render_template("index.html", board=board, winner="Draw")

    return render_template("index.html", board=board, winner=None)


if __name__ == "__main__":
    app.run(debug=True)
