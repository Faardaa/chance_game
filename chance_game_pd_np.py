import random
import numpy as np # Import numpy to perform array operations.
import pandas as pd # Import pandas for working with data sets.

class GameOfLuck:
    def __init__(self, initial_amount):
        self.initial_amount = initial_amount
        self.amount = initial_amount

    # The main part of the game
    def game_inside(self):
        random_list = [random.choice(["Lose", "Win"]) for _ in range(100)] # Creates a list which contains 100 "Lose" or "Win" messages.
        random_2d_list = np.reshape(random_list, (10, 10)) # Turnes random_list into a (10, 10) 2D list to create a dataframe  
        random_df = pd.DataFrame(random_2d_list, columns = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]) # Creates data frame by using random_2d_list
        random_df.index = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] #type: ignore # Give names to the indexes of the data frame
        
        while True:
            row, col = input("Choose a row between 1 to 10:"), input("Choose a column between 1 to 10:") # Get row and col
            if col.isdigit() and row.isdigit() and 1 <= int(col) <= 10 and 1 <= int(row) <= 10: # Check for miss values
                break
            print("You have to enter a number between 1 to 10 !!!")
        
        if self.win_or_not(random_df, row, col) : # Defines if user won or not 
            self.amount *= 2
            self.play_again()
        else:
            # User looses the game so, reduce the amount
            self.amount /= 2
            self.play_again()
            
    # Defines if user is won to the game or not
    def win_or_not(self, df, row, col):
        print(f"From this unique table: \n{df}")
        print(f"You {df.loc[row, col]} the price... \nChoices ({row}, {col}) ")

        # If user wins the game function returns True otherwise False
        if df.loc[row, col] == "Win":
            return True
        else:
            return False
        
    def play_again(self):
        print('Initial amount:', self.initial_amount)
        print('Current amount:', self.amount)
        if self.amount < 1:
            print("Game over!!!\n(Current amount is less than 1$): ")
            return

        # Asks user of he/she will play again
        play_again = input(f"Play again for {self.amount * 2}$? (yes/no): ").lower()
        if play_again == 'yes':
            self.game_inside()
        else:
            print("Your money preparing, see you soon :)")
            return

    @staticmethod
    def main():
        print("***** Welcome to Game of Luck *****")
        initial_amount = int(input('Enter initial amount (No coins):')) # Provided by money taking device
        if initial_amount < 1:
            initial_amount += int(input('At least 1$ to play:'))
        game = GameOfLuck(initial_amount)
        game.game_inside()
        

if __name__ == '__main__':
    GameOfLuck.main()
