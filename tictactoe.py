import random

board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

players = {
    "X": "Player 1",
    "O": "Computer"
}

winning_combinations = (
    (0, 1, 2), (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6), (1, 4, 7),
    (2, 5, 8), (0, 4, 8),
    (2, 4, 6)
)

occupied = set()


def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(symbol):
    for combination in winning_combinations:
        if all(board[position] == symbol for position in combination):
            return True
    return False


def make_player_move():
    while True:
        choice = input("Player 1 (X), choose a position (1-9): ")

        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        position = int(choice) - 1

        if position < 0 or position > 8:
            print("Please choose a position between 1 and 9.")
            continue

        if position in occupied:
            print("This position is already occupied.")
            continue

        board[position] = "X"
        occupied.add(position)
        break


def make_computer_move():
    available_positions = [
        position for position in range(9)
        if position not in occupied
    ]

    position = random.choice(available_positions)

    board[position] = "O"
    occupied.add(position)

    print("Computer chose position", position + 1)


print("Welcome to Tic-Tac-Toe!")
print("You are X. The computer is O.")

while True:
    # Player 1's turn
    display_board()
    make_player_move()

    if check_winner("X"):
        display_board()
        print("Player 1 wins!")
        break

    if len(occupied) == 9:
        display_board()
        print("It's a draw!")
        break

    # Computer's turn
    display_board()
    make_computer_move()

    if check_winner("O"):
        display_board()
        print("Computer wins!")
        break

    if len(occupied) == 9:
        display_board()
        print("It's a draw!")
        break

print("\nThanks for playing!")
