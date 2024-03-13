#Project02_Q01
 
import random

#fill game board with pairs od cards randomly 
def fill_board(cards):
    random.shuffle(cards)
    board = []
    #randomly stuffled cards to repersent the game board
    for i in range(0, len(cards), 4):
        row = cards[i:i + 4]
        board.append(row)
    return board

#play the memory game.
def play_game(cards):
    board = fill_board(cards)
    up = []
    for _ in range(4):
        up.append([False] * 4)
    # Continue playing until all cards are revealed.
    while not all(all(cell for cell in row) for row in up):
        show_board(board, up)
        
        # Get first card pos from the user, check if it is up, if up- print an error message and prompt again.
        pos_1 = card_position()
        while up[pos_1[0]][pos_1[1]]:
            print("Card at this position already faced up. Select position again.")
            pos_1 = card_position()
        
        # Mark the first card as up and display the updated board.
        up[pos_1[0]][pos_1[1]] = True
        show_board(board, up)
        
        # Get second card pos from the user, check if it is up, if up- print an error message and prompt again.
        pos_2 = card_position()
        while up[pos_2[0]][pos_2[1]]:
            print("Card at this position already faced up. Select position again.")
            pos_2 = card_position()
        
        # Mark the second card as up and display the updated board.
        up[pos_2[0]][pos_2[1]] = True
        show_board(board, up)

     # Check if the two revealed cards form a matching pair or not
        if board[pos_1[0]][pos_1[1]] != board[pos_2[0]][pos_2[1]]:
            print("Pair do not match. Select again!")
            up[pos_1[0]][pos_1[1]] = False
            up[pos_2[0]][pos_2[1]] = False
        else:
            print("Pair match ")
            up[pos_1[0]][pos_1[1]] = True
            up[pos_2[0]][pos_2[1]] = True

#get the user's input for the card position
def card_position():
    while True:
        try:
            #prompt the user for row and col and check if it is in valid range 
            row, col = map(int, input("Enter the row (1 to 4) and col (1 to 4) position of the pair: ").split())
            if 1 <= row <= 4 and 1 <= col <= 4:
                return row - 1, col - 1
            else:
                print("Invalid position. ")
        except ValueError:
            print("Invalid input. Please enter two integers.")

#display the game board and show the cards 
def show_board(board, up):
    # loop though the row and col of the board
    # if card is faced up- print the number , if not - print *
    for row in range(4):
        for col in range(4):
            if up[row][col]:
                print(f"   {board[row][col]}", end=" ")
            else:
                print("   *", end=" ")
        print()


def main():
    while True:
        # list of cards from 1 to 8 ech cards are twice
        cards = list(range(1, 9)) * 2
        play_game(cards)
        

        # Ask if the user wants to play again
        play_again = input("Enter key to continue...(Yes/No): ").lower()
        if play_again == 'no':
            break 

if __name__ == "__main__":
    main()
