# Game of Luck

The "Game of Luck" is a Python-based simulation designed to enhance programming skills in data manipulation and numerical operations using Pandas and NumPy. The game begins with an initial amount of money, and players can take part in simulated game events that modify this amount based on random outcomes.

## Features

- **Game Initialization:** The game starts with a specified initial amount of money.
- **Game Simulation:** A 10x10 grid is generated, where each cell contains a random outcome that affects the player's balance.
- **Outcome Modifiers:** Outcomes include multipliers (e.g., `x3`, `x2`) and divisors (e.g., `/2`, `/3`, `/4`), as well as neutral results (`=1`).
- **Array and DataFrame Operations:** Uses NumPy for array manipulation and Pandas for data handling.

## Installation

1. **Prerequisites:**
   - Python 3.x
   - NumPy library
   - Pandas library

2. **Installation Steps:**
   - Clone this repository or download the code file.
   - Install the required dependencies using:
     ```bash
     pip install numpy pandas
     ```

## Usage

1. **Initialize the Game:**
   - To start the game, create an instance of the `GameOfLuck` class with an initial amount.
     ```python
     from chance_game_pd_np import GameOfLuck
     
     game = GameOfLuck(initial_amount=1000)
     ```

2. **Run the Game:**
   - Call the game functions as required to simulate the game events.
     ```python
     game.game_inside()  # Generates a grid with random outcomes
     ```

## Project Structure

- **`chance_game_pd_np.py`**: The main game file containing the implementation of the Game of Luck.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.

## License

This project is licensed under the MIT License.

## Acknowledgments

- This project was created to enhance skills in working with Pandas and NumPy.
