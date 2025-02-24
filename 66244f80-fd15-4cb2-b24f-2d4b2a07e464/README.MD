## Tic-Tac-Toe Game Application Documentation

This application provides a simple implementation of a Tic-Tac-Toe game using a Python server and a basic front-end written in HTML, CSS, and JavaScript. The server-side logic is controlled using Python's `http.server` and `socketserver` modules, while the front-end displays the game and handles user interactions.

### Features

- Play Tic-Tac-Toe in a web browser.
- Two players alternate turns, selecting cells on a 3x3 game board.
- Detects a win or a tie and provides immediate feedback.
- Offers a reset button to start a new game.
- Simple UI and intuitive controls.

### File Structure

- `server.py`: Contains the Python server logic and the game mechanics.
- `static/index.html`: The HTML file managing the game interface shown to users.
- `static/style.css`: Provides styling for making the game visually appealing.
- `static/script.js`: Manages the client-side interactions and communicates with the server via HTTP requests.

### Installation Requirements

Before running the application, ensure you have the following installed:

- Python 3.x
- A web browser
  
### Setup Instructions

1. **Clone the Repository**: Start by cloning the repository to your local machine.

   ```bash
   git clone https://github.com/your-username/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. **Navigate to the Application Directory**: Open the cloned directory in your terminal.

   ```bash
   cd tic-tac-toe
   ```

3. **Install Python**: Ensure Python 3.x is installed on your system. You can check the version by running:

   ```bash
   python --version
   ```

   If Python is not installed, you can download it from the [official website](https://www.python.org/downloads/).

4. **Run the Server**: Start the Python server using the terminal.

   ```bash
   python server.py
   ```

   This will start the server on `localhost` at port 8000. 

5. **Access the Game**: Open your web browser and visit `http://localhost:8000`. You should see the Tic-Tac-Toe game interface.

### How to Play

- The game board consists of 9 cells.
- Players take turns to place their markers ('X' or 'O') by clicking on an empty cell.
- The current player's turn is shown and updated after each valid move.
- The game ends when a player secures three of their marks in a row (horizontally, vertically, or diagonally) or when all cells are filled resulting in a tie.

### Resetting the Game

To restart the game, click the "Reset" button below the game board. This will clear all cells and allow a new game without needing to refresh the page.

### Conclusion

This project is a basic yet functional web-based Tic-Tac-Toe game that serves as an introduction to server-client communication and basic game logic implementation. Feel free to modify and enhance the project to add more features or improve the UI/UX.

For any questions or issues, please check out the repository's issue tracker or submit a new issue. 

Enjoy playing!