def display_board(board):
    list1 = ["|  ", board[7], "  |  ", board[8], "    |  ", board[9],"  |"]
    list3 = ["|  ",board[4], "  |  ",board[5], "    |  ",board[6],"  |"]
    list5 = ["|  ",board[1], "  |   ", board[2], "  |  ",board[3],"  |"]
    line1 = ''.join(list1)
    line2 = "------------------"
    line3 = ''.join(list3)
    line4 = "------------------"
    line5 = ''.join(list5)
    board2 = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5
    print(board2)


def players_symbols():
    player1choice=""
    while(player1choice!="X" or player1choice!="O"):
        player1choice=input("Player 1 Do you want to be X or O").upper()
        if (player1choice == "X"):
            return ("X","O")

        else:
            return ("O","X")



def insert_symbol(board,symbol,position):
    board[position]=symbol



def win_check(board,symbol):# check for rows coloumns and diagonals
    return((board[7]==symbol and board[8]==symbol and board[9]==symbol)or
           (board[4] == symbol and board[5] == symbol and board[6] == symbol)or
           (board[1] == symbol and board[2] == symbol and board[3] == symbol)or

           (board[7] == symbol and board[4] == symbol and board[1] == symbol)or
           (board[8] == symbol and board[5] == symbol and board[2] == symbol)or
           (board[9] == symbol and board[6] == symbol and board[3] == symbol)or

           (board[7] == symbol and board[5] == symbol and board[3] == symbol)or
           (board[9] == symbol and board[5] == symbol and board[1] == symbol)

    )



def space_check(board,position):
    return board[position]== ""



def full_board_check(board):
    boardfull=True
    for i in range(9):
        if (board[i]==""):
            boardfull=False
    return boardfull

def player_choice(board):
    position=0
    while ((position not in range(1,10)) or (not space_check(board, position))):
        position = int(input('Choose your next position: (1-9) '))
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

#
# test_board = ['#','','O','X','O','X','O','X','O','X']
# display_board(test_board)
#
# print(player_choice(test_board))

def main():
    firstboard="|  7 |  8 |  9 |"+"\n"+"----------------"+"\n"+"|  4 |  5 |  6 |"+"\n"+"----------------"+"\n"+"|  1 |  2 |  3 |"
    print('Welcome to Tic Tac Toe!')
    while True:
        playboard = ["#", "", "", "", "", "", "", "", "", ""]
        playerssymbols=players_symbols()
        player1symbol=playerssymbols[0]
        player2symbol=playerssymbols[1]
        playersready=input("Are you ready to play? Enter(Yes or No)").lower().startswith('y')
        print("Player 1 goes first.")
        print(firstboard)
        for i in range(9):
            if (i%2==0):
                insert_symbol(playboard,player1symbol,player_choice(playboard))

            elif (i%2==1):
                insert_symbol(playboard, player2symbol, player_choice(playboard))


            display_board(playboard)
            wincheck1=win_check(playboard, player1symbol)
            wincheck2=win_check(playboard, player2symbol)
            if(wincheck1):
                print("Player 1 has won!")
                break
            elif (wincheck2):
                print("Player 2 has won!")
                break
            elif(full_board_check(playboard)):
                print("The game has been a Tie!")
                break
        if not replay():
            break



main()

