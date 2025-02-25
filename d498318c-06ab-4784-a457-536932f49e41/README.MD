## Game Description
The game is a simple implementation of a Battleship game using Python's tkinter library for the graphical user interface. The game generates a grid of size 10x10, places three random ships on the grid, and allows the player to guess the locations of the ships. The player has 10 guesses to sink all the ships.

## Installation and Configuration
To run the game, you will need to have Python and tkinter installed on your system. Here are the steps to install and configure the environment:

1. **Install Python**: Download and install Python from the official Python website if it's not already installed on your system.
2. **Install tkinter**: tkinter is a built-in Python library, but you may need to install additional packages depending on your operating system.
	* **Windows**: tkinter is included in the Python installation package.
	* **macOS**: You can install tkinter using Homebrew by running the command `brew install python-tk`.
	* **Linux**: You can install tkinter using your distribution's package manager. For example, on Ubuntu-based systems, run `sudo apt-get install python3-tk`.
3. **Clone the repository**: Clone the repository containing the game code.
4. **Run the game**: Navigate to the directory containing the game code and run the game using Python: `python game.py`.

## Running the Game
To run the game, simply execute the Python script. The game will launch a window with a 10x10 grid, and you can start guessing the locations of the ships by clicking on the grid cells.

## Game Rules
* The player has 10 guesses to sink all the ships.
* If the player guesses a ship's location correctly, a red circle will be drawn on the grid cell, and the ship will be removed from the game.
* If the player guesses incorrectly, a grey circle will be drawn on the grid cell, and the number of guesses remaining will decrease.
* The game ends when the player has sunk all the ships or has used up all their guesses.

## Code Structure
The game code is structured into a single class `Game` that contains all the game logic and GUI-related methods. The game is launched by creating an instance of the `Game` class and calling the `play` method.

## Methods
* `create_gui`: Creates the game window and GUI elements.
* `draw_grid`: Draws the 10x10 grid on the canvas.
* `update_guesses`: Updates the label with the number of guesses remaining.
* `guess`: Handles the player's guess and updates the game state accordingly.
* `canvas_click`: Handles the player's mouse click on the grid cell and calls the `guess` method.
* `play`: Launches the game and starts the main event loop.