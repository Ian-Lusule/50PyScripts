```python
"""
Tic-Tac-Toe game in Python.

This script implements a text-based Tic-Tac-Toe game for two players.
It handles player input, game logic, and win/draw conditions.
"""

def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

def check_win(board, player):
    """Checks if the given player has won the game."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_draw(board):
    """Checks if the game is a draw."""
    for row in board:
        if " " in row:
            return False
    return True

def get_player_move(board, player):
    """Gets a valid move from the player."""
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter your move (row, column) (1-3, 1-3): ").split(","))
            row -= 1
            col -= 1
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter row and column numbers separated by a comma.")


def play_tic_tac_toe():
    """Plays a game of Tic-Tac-Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_player_move(board, current_player)
        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_tic_tac_toe()

```