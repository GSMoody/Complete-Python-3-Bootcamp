"""
Spyder Editor

A TicTacToe python game
"""

# Empty dictionary to store position state
positions = {'1' : " ", '2' : " ", '3' : " ", '4' : " ", '5' : " ", '6' : " ", 
             '7' : " ",'8' : " ", '9' : " "}

# Function to display the board
def display_board():
    print("|"+positions['7']+"|"+positions['8']+"|"+positions['9']+"|\n|"\
        +positions['4']+"|"+positions['5']+"|"+positions['6']+"|\n|"\
            +positions['1']+"|"+positions['2']+"|"+positions['3']+"|")
        
# Function to validate user input
def validate_input(player):
    position = input("Select position (Enter number from 1 to 9)")
    while position not in positions.keys():
        position = input("Select position (Enter number from 1 to 9)")
        while positions[position] != ' ':
            print("You cannot choose a space which is already occupied! Please"\
                  " choose an empty space.")
            position = input("Select position (Enter number from 1 to 9)")
    positions[position] = player
    display_board()

# Function to check if the board contains a win or draw
def check_win():
    player1_positions = [i for i,j in positions.items() if j == player1]
    player2_positions = [i for i,j in positions.items() if j == player2]
    win_combinations = [['7','8','9'], ['4','5','6'], ['1','2','3'], \
                        ['7','4','1'], ['8','5','2'], ['9','6','3'], \
                        ['1','5','9'], ['7','5','3']]
    for win_combination in win_combinations:
        if set(win_combination).issubset(player1_positions):
            print("Player 1 wins!")
            return True
        elif set(win_combination).issubset(player2_positions):
            print("Player 2 wins!")
            return True
    if " " not in list(positions.values()):
        print("All positions taken! It's a draw")
        return True
    return False

# Function to run game
def run_game():   
    while True:
        validate_input(player1)
        if check_win():
            break
        else:
            validate_input(player2)
        if check_win():
            break

player1 = input("Player 1: Do you want to be 'O' or 'X'?")
while player1 not in ["o","O","x","X"]:
    player1 = input("Player 1: Do you want to be 'O' or 'X'?")
player1 = player1.upper()
if player1 == 'X':
    player2 = 'O'
else:
    player2 = 'X'
print(f"Player 1 is '{player1}' and Player 2 is '{player2}'. \nCommence game!!")
    
while True:
    run_game()
    if input("Do you want to play again? Enter (y/Y) or (n/N)") not in ['Y', 'y']:
        break
    