board = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]  

player = "X"

game = True

def main():
    while game:
        make_board(board)
        player_turn(player, board)
        next_player()
        is_draw(board)
        is_winner(board)
    make_board(board)
    print("Thanks for playing!")
    


def make_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def player_turn(player, board):
    choice = int(input(f"It's {player} your turn! Choose between 1-9: "))
    board[choice-1] = player
        
def next_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"
        
def horizontal(board):
    if board[0] == board[1] == board[2] and board[0]:
        return True
    elif board[3] == board[4] == board[5] and board[3]:
        return True
    elif board[6] == board[7] == board[8] and board[6]:
        return True

def vertical(board):
    if board[0] == board[3] == board[6] and board[0]:
        return True
    elif board[1] == board[4] == board[7] and board[1]:
        return True
    elif board[2] == board[5] == board[8] and board[2]:
        return True

def diagnol(board):
    if board[0] == board[4] == board[8] and board[0]:
        return True
    elif board[2] == board[4] == board[6] and board[2]:
        return True

def is_winner(board):
    global game
    if horizontal(board) or vertical(board) or diagnol(board):
        game = False

def is_draw(board):
    for i in range(9):
        global game
        if board[i] != "X" and board[i] != "O":
            # winner = None
            game = False
        game = True

# def is_draw(board): 
#     for i in range(9):
#         if board[i] != "X" and board[i] != "O":
#             return False
#     return True
    

if __name__ == "__main__":
    main()