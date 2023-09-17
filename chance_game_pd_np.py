import random
import numpy as np # Import numpy to perform array operations.
import pandas as pd # Import pandas for working with data sets.

earned_money = 1 # Starting money, and it will increase while the user is winning.

# Display a welcome message.
print("************************** Welcome to 50% luck game **************************")
money_entered = True # Indicates whether enought money has been entered or not.

# The main part of the game
def game_inside():
    # Creates a list which contains 100 "Missed" or "Won" messages.
    random_list = [random.choice(["Missed", "Won"]) for _ in range(100)]

    # Turnes random_list into a (10, 10) 2D list to create a dataframe  
    random_2d_list = np.reshape(random_list, (10, 10))

    # Creates data frame by using random_2d_list
    df = pd.DataFrame(random_2d_list, columns = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

    # Give names to the indexes of the data frame
    df.index = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] #type: ignore
    global earned_money 
    if win_or_not(df) : # Defines if user won or not 
        earned_money += 1
        
        # Asks if user will play again or not
        play_again = input(f"You won the game, would you play again with winner pride for {earned_money}$ \nor take your {earned_money - 1}$ and leave the game ? (yes/no): ").lower()4
        if play_again == 'yes':
            game_inside()
        else:
            print("Your money preparing, see you soon :)")
    else:
        # User looses the game so, reset the money
        earned_money = 0
        # Asks if user will play again or not
        play_again = input("You lost the game, would you play from zero till the hero? (yes/no): ").lower()
        if play_again == 'yes':
            game_inside()
        else:
            print("Alright then, see you soon :)")
# Gets the informatinon from user and defines he or she is won to the game or not
def win_or_not(df):
    col, row = input("Choose a column from 1 to 10: "), input("Choose a row from 1 to 10: ")

    # Checks for if user entered numbers in right way or not
    if not col.isdigit() or not row.isdigit() or int(col) < 1 or int(col) > 10 or int(row) < 1 or int(row) > 10:
        print("You have to enter a number between 1 to 10 !!!")
        raise ValueError
    print(f"You've choosed {col}. col and {row}. row and you've {df.loc[col, row]} the price...")
    print(f"From this unique table: \n{df}")

    # If user wins the game function returns True otherwise False
    if df.loc[col, row] == "Won":
        return True
    else:
        return False

# If enought money is entered the game starts.
if(money_entered):
    game_inside()