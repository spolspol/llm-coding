# server.py
import http.server
import socketserver
import json

PORT = 8000

class Game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def make_move(self, cell):
        if self.board[cell] == ' ':
            self.board[cell] = self.current_player
            winner = self.check_winner()
            if winner:
                return {'status': 'won', 'winner': winner}
            if ' ' not in self.board:
                return {'status': 'tie'}
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return {'status': 'next_turn', 'board': self.board}
        return {'status': 'invalid', 'message': 'Cell is already taken'}

    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]
        return None

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'static/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        move = data.get('move')
        game_response = game.make_move(move)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(game_response).encode('utf-8'))

game = Game()
with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

html
<!-- static/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Tic-Tac-Toe</title>
</head>
<body>
    <div id="game">
        <div id="board">
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
        <div id="message"></div>
        <button id="reset">Reset</button>
    </div>
    <script src="script.js"></script>
</body>
</html>

css
/* static/style.css */
body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

#game {
    text-align: center;
}

#board {
    display: grid;
    grid-template-columns: repeat(3, 100px);
    grid-template-rows: repeat(3, 100px);
    gap: 10px;
    margin-bottom: 20px;
}

.cell {
    width: 100px;
    height: 100px;
    background-color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2em;
    border: 2px solid #000;
    cursor: pointer;
}

#message {
    font-size: 1.5em;
    margin-bottom: 20px;
}

button {
    padding: 10px 20px;
    font-size: 1em;
}

javascript
// static/script.js
document.addEventListener('DOMContentLoaded', () => {
    const cells = document.querySelectorAll('.cell');
    const message = document.getElementById('message');
    const resetButton = document.getElementById('reset');

    cells.forEach(cell => cell.addEventListener('click', () => {
        if (cell.textContent === '') {
            makeMove(cell.dataset.index);
        }
    }));

    resetButton.addEventListener('click', resetGame);

    function makeMove(index) {
        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ move: parseInt(index) })
        }).then(response => response.json())
          .then(data => {
              if (data.status === 'won') {
                  message.textContent = `Player ${data.winner} wins!`;
                  disableBoard();
              } else if (data.status === 'tie') {
                  message.textContent = 'It\'s a tie!';
                  disableBoard();
              } else if (data.status === 'next_turn') {
                  message.textContent = `Player ${data.board.includes('X') ? 'O' : 'X'}\'s turn`;
                  updateBoard(data.board);
              } else if (data.status === 'invalid') {
                  message.textContent = data.message;
              }
          })
          .catch(error => console.error('Error:', error));
    }

    function updateBoard(board) {
        cells.forEach((cell, index) => cell.textContent = board[index]);
    }

    function resetGame() {
        cells.forEach(cell => cell.textContent = '');
        message.textContent = '';
        cells.forEach(cell => cell.style.pointerEvents = 'auto');
    }

    function disableBoard() {
        cells.forEach(cell => cell.style.pointerEvents = 'none');
    }

    message.textContent = 'Player X\'s turn';
});
