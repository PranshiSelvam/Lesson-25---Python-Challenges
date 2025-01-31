board= {'7': ' ','8': ' ','9': ' ', 
        '4': ' ','5': ' ','6': ' ', 
        '1': ' ','2': ' ','3': ' ', }
board_keys = []
for key in board: 
    board_keys.append(key)

def printboard(board): 
    print(board['7'] + '|' + board['8'] + '|' + board['9'] )
    print("-+-+-")
    print(board['4'] + '|' + board['5'] + '|' + board['6'] )
    print("-+-+-")
    print(board['1'] + '|' + board['2'] + '|' + board['3'] )

def game(): 
    turn = 'X'
    count = 0

    for i in range(10): 
        printboard(board)
        print("It's your turn, " + turn + " which place would you like to move?")
        move = input()

        if board[move] == ' ': 
            board[move] = turn
            count += 1 
        else: 
            print("That place is already filled. Move to another place. ")
            continue 
        if count >= 5: 
            if board['7'] == board['8'] == board['9'] != ' ': 
                printboard(board)
                print("\n Game is over \n")
                print("~~~~" + turn + " Won. ~~~~")
                break 
            elif board['4'] == board['5'] == board['6'] != ' ': 
                printboard(board)
                print("\n Game is over \n")
                print("~~~~" + turn + " Won. ~~~~")
                break 
            elif board['1'] == board['2'] == board['3'] != ' ': 
                printboard(board)
                print("\n Game is over \n")
                print("~~~~" + turn + " Won. ~~~~")
                break 
            elif board['7'] == board['4'] == board['1'] != ' ': 
                printboard(board)
                print("\n Game is over \n")
                print("~~~~" + turn + " Won. ~~~~")
                break 
            elif board['8'] == board['5'] == board['2'] != ' ': 
                printboard(board)
                print("\n Game is over \n")
                print("~~~~" + turn + " Won. ~~~~")
                break 
            elif board['9'] == board['6'] == board['3'] != ' ': 
                printboard(board)
                print("\n Game is over \n")
                print("~~~~" + turn + " Won. ~~~~")
                break 
            elif board['9'] == board['5'] == board['1'] != ' ': 
                printboard(board)
                print("\n Game is over \n")
                print("~~~~" + turn + " Won. ~~~~")
                break 
            elif board['7'] == board['5'] == board['3'] != ' ': 
                printboard(board)
                print("\n Game is over \n")
                print("~~~~" + turn + " Won. ~~~~")
                break 
        if count == 9: 
            print("\n It's a tie \n")

        if turn == 'X': 
            turn = 'O'
        else: 
            turn = "X"

    restart = input("Do you want to play again? (Yes / No)")
    if restart == "Yes" or restart == "yes" or restart == "YES": 
        for key in board_keys: 
            board[key] = " "

        game()
if __name__ == "__main__": 
    game()



    
    