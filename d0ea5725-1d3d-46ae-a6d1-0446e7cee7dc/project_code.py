# src/game.py
class Game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.check_win(square, letter):
                self.current_winner = letter
            return True
        return False

    def check_win(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

    def is_draw(self):
        return not self.empty_squares() and not self.current_winner

# src/server.py
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from game import Game
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

game = Game()
lock = threading.Lock()
players = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    with lock:
        if len(players) < 2:
            players.append(request.sid)
            if len(players) == 2:
                emit('start_game', broadcast=True)
        else:
            disconnect()

@socketio.on('disconnect')
def handle_disconnect():
    with lock:
        if request.sid in players:
            players.remove(request.sid)
            game.reset()
            emit('reset_game', broadcast=True)

@socketio.on('make_move')
def handle_make_move(data):
    with lock:
        square = data['square']
        letter = data['letter']
        if game.make_move(square, letter):
            emit('update_board', {'square': square, 'letter': letter}, broadcast=True)
            if game.current_winner:
                emit('game_won', {'letter': game.current_winner}, broadcast=True)
                game.reset()
            elif game.is_draw():
                emit('game_draw', broadcast=True)
                game.reset()
        else:
            emit('invalid_move', broadcast=True)

@socketio.on('reset_game')
def handle_reset_game():
    with lock:
        game.reset()
        emit('reset_game', broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)

# static/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tic-Tac-Toe</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="game-container">
        <h1>Tic-Tac-Toe</h1>
        <div class="board">
            <div class="cell" data-index="0"></div>
            <div class="cell" data-index="1"></div>
            <div class="cell" data-index="2"></div>
            <div class="cell" data-index="3"></div>
            <div class="cell" data-index="4"></div>
            <div class="cell" data-index="5"></div>
            <div class="cell" data-index="6"></div>
            <div class="cell" data-index="7"></div>
            <div class="cell" data-index="8"></div>
        </div>
        <div class="status" id="status"></div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <script src="script.js"></script>
</body>
</html>

// static/styles.css
body {
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f0f0f0;
    margin: 0;
}

.game-container {
    text-align: center;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.board {
    display: grid;
    grid-template-columns: repeat(3, 100px);
    grid-template-rows: repeat(3, 100px);
    gap: 5px;
    margin: 20px 0;
}

.cell {
    width: 100px;
    height: 100px;
    background-color: #e0e0e0;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2em;
    cursor: pointer;
    transition: background-color 0.2s;
}

.cell:hover {
    background-color: #d0d0d0;
}

.status {
    font-size: 1.2em;
    color: #555;
}

// static/script.js
document.addEventListener('DOMContentLoaded', () => {
    const socket = io();
    const cells = document.querySelectorAll('.cell');
    const status = document.getElementById('status');
    let letter = '';
    let isTurn = false;

    socket.on('start_game', () => {
        letter = players.length === 1 ? 'X' : 'O';
        isTurn = letter === 'X';
        updateStatus();
    });

    socket.on('reset_game', () => {
        cells.forEach(cell => cell.textContent = '');
        game.current_winner = null;
        isTurn = letter === 'X';
        updateStatus();
    });

    socket.on('update_board', data => {
        cells[data.square].textContent = data.letter;
        if (data.letter === letter) {
            isTurn = false;
        } else {
            isTurn = true;
        }
        updateStatus();
    });

    socket.on('game_won', data => {
        status.textContent = `Player ${data.letter.toUpperCase()} wins!`;
        isTurn = false;
    });

    socket.on('game_draw', () => {
        status.textContent = 'Game over! It\'s a draw!';
        isTurn = false;
    });

    socket.on('invalid_move', () => {
        alert('Invalid move! Try again.');
    });

    cells.forEach(cell => cell.addEventListener('click', () => {
        const index = cell.getAttribute('data-index');
        if (cell.textContent === '' && isTurn) {
            socket.emit('make_move', { square: parseInt(index), letter: letter });
        }
    }));

    function updateStatus() {
        if (isTurn) {
            status.textContent = `Your turn (${letter.toUpperCase()})`;
        } else {
            status.textContent = `Waiting for opponent (${letter === 'X' ? 'O' : 'X'})`;
        }
    }
});

# README.md
# Tic-Tac-Toe Game with WebSockets

## Introduction
This project implements a Tic-Tac-Toe game using Python with Flask and Flask-SocketIO for handling WebSocket connections. The application is structured using the Model-View-Controller (MVC) pattern.

## Project Structure
- **static/**: Contains the HTML, CSS, and JavaScript files for the client-side.
- **src/**: Contains the Python source files for the server-side.
- **README.md**: This documentation file.

## How to Run the Application

1. **Install Dependencies**
   bash
   pip install flask flask-socketio
   

2. **Run the Server**
   bash
   python src/server.py
   

3. **Access the Game**
   Open a web browser and navigate to `http://localhost:5000`. Open another browser tab or window to play with another player.

## Game Logic
The `Game` class handles the game logic, including initializing the board, making moves, checking for wins, and resetting the game.

## WebSockets
The server provides WebSocket connections facilitated by Flask-SocketIO to handle real-time interactions between clients.

## User Interface
The user interface is built using HTML, CSS, and JavaScript. It includes a grid layout for the Tic-Tac-Toe board and buttons for each cell to make moves.

## Testing
The application should be tested for unit tests on the `Game` class and integration tests for the WebSocket server.

## Deployment
The application can be deployed on a platform like Heroku or DigitalOcean that supports Python applications.

## Documentation
- **User Documentation**: Instructions for installation, running, and playing the game.
- **Developer Documentation**: Explains the project structure, code architecture, and potential enhancements.

## Future Enhancements
- Score tracking
- Player authentication
- Improved user interface
- Add multiplayer lobby

## License
MIT License
