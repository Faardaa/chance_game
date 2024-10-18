import numpy as np # Import numpy to perform array operations.
import pandas as pd # Import pandas for working with data sets.

class GameOfLuck:
    def __init__(self, initial_amount):
        self.amount = initial_amount

    # The main part of the game
    def game_inside(self):
        rows = range(1, 11)
        cols = range(1, 11)
        data = np.random.choice(['Win', 'Lose'], size=(10, 10)) # Creates a 10x10 list which contains 100 "Lose" or "Win" messages.
        random_df = pd.DataFrame(data, index = rows, columns = cols)

        while True:
            row, col = input("Choose a row between 1 to 10:"), input("Choose a column between 1 to 10:") # Get row and col
            if col.isdigit() and row.isdigit() and 1 <= int(col) <= 10 and 1 <= int(row) <= 10: # Check for miss values
                break
            print("You have to enter a number between 1 to 10 !!!")
        
        if self.win_or_not(random_df, int(row) - 1, int(col) - 1) : # Defines if user won or not 
            self.amount *= 2
            self.play_again()
            return
        else:
            # User looses the game so, reduce the amount
            self.amount /= 2
            self.play_again()
            return
            
    # Defines if user is won to the game or not
    def win_or_not(self, df, row, col):
        print(f"From this unique table: \n{df}")
        print(f"You {df.iloc[row, col]} 2x of the price... \nChoices ({row + 1}, {col + 1}) ")

        # If user wins the game function returns True otherwise False
        if df.iloc[row, col] == "Win":
            return True
        else:
            return False
        
    def play_again(self):
        print('Current amount:', self.amount)
        if self.amount < 1:
            print("Current amount is less than 1$ so Game is Over!!! : ")
            return

        # Asks user of he/she will play again
        while True:
            play_again = input(f"Play again for {self.amount * 2}$? (yes/no): ").lower()
            if play_again == 'yes':
                GameOfLuck.main(self.amount)
            elif play_again == 'no':
                print("Your money preparing, see you soon :)")
                break
            else:
                print('Only "yes" and "no" accepted.')

    @staticmethod
    def main(initial_amount = 0):
        if not initial_amount:
            print("***** Welcome to Game of Luck *****")
            initial_amount = int(input('Enter initial amount (No coins):')) # Provided by cash acceptor
        game = GameOfLuck(initial_amount)
        game.game_inside()
        

if __name__ == '__main__':
    GameOfLuck.main()
