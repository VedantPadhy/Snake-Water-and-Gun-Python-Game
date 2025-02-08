# Snake, Water, Gun Game

This is a simple implementation of the "Snake, Water, Gun" game in Python. The game is similar to the classic "Rock, Paper, Scissors" game.

## How to Play

1. The computer randomly chooses one of the three options: snake, water, or gun.
2. The user is prompted to enter their choice.
3. The winner is determined based on the following rules:
   - Snake (1) drinks Water (-1): Snake wins
   - Water (-1) douses Gun (0): Water wins
   - Gun (0) shoots Snake (1): Gun wins
   - If both choices are the same, it's a tie.

## Code Explanation

The code uses the `random` module to allow the computer to make a random choice. The user's input is taken and mapped to a corresponding numerical value. The game logic is implemented using a series of `if-elif` statements to compare the choices and determine the winner.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository or download the script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the following command:
   ```sh
   python main.py
