import numpy as np # Import numpy to perform array operations.
import pandas as pd # Import pandas for working with data sets.

class GameOfLuck:
    def __init__(self, initial_amount):
        self.amount = initial_amount

    # Generating game requirements
    def game_inside(self):
        rows = range(1, 11)
        cols = range(1, 11)
        data = np.random.choice(['x3', 'x2', '=1', '/2', '/3', '/4'], size=(10, 10)) # Generates a 10x10 array filled with random selections from the specified list of outcomes.
        random_df = pd.DataFrame(data, index = rows, columns = cols)

        while True:
            row, col = input("Choose a row between 1 to 10:"), input("Choose a column between 1 to 10:") # Get row and col
            if col.isdigit() and row.isdigit() and 1 <= int(col) <= 10 and 1 <= int(row) <= 10: # Check for miss values
                break
            print("You have to enter a number between 1 to 10 !!!")
        
        self.amount_counter(random_df, int(row) - 1, int(col) - 1)
            
    # Defines if user is won to the game or not
    def amount_counter(self, df, row, col):
        print(f"\nFrom this unique table: \n{df}")
        print(f"Your choices: ({row + 1}, {col + 1})\nYou got {df.iloc[row, col]} of your money...")

        # If user wins the game function returns True otherwise False
        gain = df.iloc[row, col]
        if gain[0] == "x":
            self.amount *= int(gain[1])
        elif gain[0] == "/":
            self.amount /= int(gain[1])
        
    # Root function for the game.
    def play_game(self):
        # Main loop of the game.
        while True:
            self.game_inside() 
            print('Current amount:', self.amount)
            if self.amount < 1:
                print("Current amount is less than 1$ so Game is Over!!!")
                return

            # Asks user of he/she will play again
            while True:
                play_again = input(f"Play again? (yes/no): ").lower()
                if play_again == 'yes':
                    break
                elif play_again == 'no':
                    print("Your money preparing, see you soon :)")
                    return
                else:
                    print('Only "yes" and "no" accepted.')

    @staticmethod
    def main():
        print("~~~~~~~~~~~~~~~~ Welcome to Game of Luck ~~~~~~~~~~~~~~~~")
        initial_amount = int(input('Enter initial amount (No coins):')) # Provided by cash acceptor tool (no need to error handling)
        game = GameOfLuck(initial_amount)
        game.play_game()
        

if __name__ == '__main__':
    GameOfLuck.main()
