from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
db = SQLAlchemy(app)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    ties = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Player {self.name}>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/leaderboard')
def leaderboard():
    players = Player.query.order_by(Player.wins.desc()).all()
    return jsonify([{'name': player.name, 'wins': player.wins, 'losses': player.losses, 'ties': player.ties} for player in players])

@app.route('/api/player', methods=['POST'])
def add_player():
    name = request.json['name']
    if Player.query.filter_by(name=name).first() is None:
        new_player = Player(name=name)
        db.session.add(new_player)
        db.session.commit()
        return jsonify({'message': 'Player added successfully'}), 201
    else:
        return jsonify({'message': 'Player already exists'}), 400

@app.route('/api/game_result', methods=['POST'])
def game_result():
    winner = request.json.get('winner')
    loser = request.json.get('loser')
    if winner:
        winner_player = Player.query.filter_by(name=winner).first()
        winner_player.wins += 1
    if loser:
        loser_player = Player.query.filter_by(name=loser).first()
        loser_player.losses += 1
    if winner and loser is None:
        winner_player = Player.query.filter_by(name=winner).first()
        winner_player.ties += 1
    db.session.commit()
    return jsonify({'message': 'Game result saved successfully'}), 200

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tic Tac Toe</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        #board { display: grid; grid-template-columns: repeat(3, 100px); grid-template-rows: repeat(3, 100px); gap: 5px; margin: 20px auto; }
        .cell { width: 100px; height: 100px; background-color: #f0f0f0; line-height: 100px; font-size: 2em; cursor: pointer; }
        #leaderboard { margin-top: 20px; }
        .player { margin: 5px 0; }
    </style>
</head>
<body>
    <h1>Tic Tac Toe</h1>
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
    <h2>Leaderboard</h2>
    <div id="leaderboard">
        <!-- Leaderboard will be populated here -->
    </div>
    <script>
        const cells = document.querySelectorAll('.cell');
        let board = Array(9).fill(null);
        let currentPlayer = 'X';
        let winner = null;

        const winningCombinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ];

        cells.forEach(cell => cell.addEventListener('click', handleClick));

        function handleClick(event) {
            const index = event.target.getAttribute('data-index');
            if (board[index] || winner) return;
            board[index] = currentPlayer;
            event.target.textContent = currentPlayer;
            if (checkWinner(currentPlayer)) {
                alert(`${currentPlayer} wins!`);
                winner = currentPlayer;
                saveGameResult();
            } else if (board.every(cell => cell)) {
                alert('Tie game!');
                saveGameResult(null, null);
            } else {
                currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
            }
        }

        function checkWinner(player) {
            return winningCombinations.some(combination => {
                return combination.every(index => {
                    return board[index] === player;
                });
            });
        }

        function saveGameResult(winner = currentPlayer, loser = currentPlayer === 'X' ? 'O' : 'X') {
            const result = { winner };
            if (!winner) result.winner = null;
            if (loser && winner !== null) result.loser = loser;
            fetch('/api/game_result', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(result)
            }).then(response => response.json()).then(data => {
                console.log(data.message);
                fetchLeaderboard();
            });
        }

        function fetchLeaderboard() {
            fetch('/api/leaderboard')
                .then(response => response.json())
                .then(data => {
                    const leaderboard = document.getElementById('leaderboard');
                    leaderboard.innerHTML = '';
                    data.forEach(player => {
                        const playerDiv = document.createElement('div');
                        playerDiv.classList.add('player');
                        playerDiv.textContent = `${player.name}: Wins ${player.wins} - Losses ${player.losses} - Ties ${player.ties}`;
                        leaderboard.appendChild(playerDiv);
                    });
                });
        }

        fetchLeaderboard();
    </script>
</body>
</html>
