// Backend: Validate ship placement
function validateShipPlacement(grid, ship, row, col, direction) {
    if (direction === 'horizontal') {
        if (col + ship.size > grid[0].length) return false;
        for (let i = 0; i < ship.size; i++) {
            if (grid[row][col + i] !== 'empty') return false;
        }
    } else if (direction === 'vertical') {
        if (row + ship.size > grid.length) return false;
        for (let i = 0; i < ship.size; i++) {
            if (grid[row + i][col] !== 'empty') return false;
        }
    }
    return true;
}

// Backend: Track game state in the WebSocket server
let gameState = {
  players: [],
  turn: 'player1',
  status: 'waiting'
};

wss.on('connection', (ws) => {
  ws.on('message', (message) => {
    const data = JSON.parse(message);
    if (data.type === 'shot' && gameState.turn === data.player) {
        const result = processShot(data.row, data.col);
        gameState.turn = data.player === 'player1' ? 'player2' : 'player1';
        ws.send(JSON.stringify({ type: 'shotResult', result }));
    } else if (data.type==="join") {
     if(gameState.players.length<2){
      gameState.players.push(data.player);
      gameState.status="playing"
      if(gameState.players.length===2 ){
        gameState.turn="player1"
        gameState.status="playing"
        wss.broadcast(JSON.stringify({ type: 'gameStatus',gameState }))
      }
     }
    }
  });
});

// Backend: Define ship types
const ships = [
  { type: 'carrier', size: 5 },
  { type: 'battleship', size: 4 },
  { type: 'cruiser', size: 3 },
  { type: 'submarine', size: 3 },
  { type: 'destroyer', size: 2 },
];



// Backend: Check for game over condition after each shot
function checkGameOver(grid) {
  return grid.every(row => row.every(cell => cell !== 'ship'));
}

wss.on('connection', (ws) => {
  ws.on('message', (message) => {
    const data = JSON.parse(message);
    if (data.type === 'shot') {
      const result = processShot(data.row, data.col);
      if (checkGameOver(opponentGrid)) {
        gameState.status = 'finished';
        ws.send(JSON.stringify({ type: 'gameOver', winner: data.player }));
      }
    }
  });
});

// Frontend: Update the placeShip function
const placeShip = (row, col, direction) => {
  const selectedShip = ships[0];
  if (validateShipPlacement(playerGrid, selectedShip, row, col, direction)) {
    setPlayerGrid((prevGrid) => {
      for (let i = 0; i < selectedShip.size; i++) {
        prevGrid[row + (direction === 'vertical' ? i : 0)][col + (direction === 'horizontal' ? i : 0)] = 'ship';
      }
      return [...prevGrid];
    });
  }
};

// Frontend: Update the turn and game state based on server responses
const [gameState, setGameState] = useState('waiting');

useEffect(() => {
  socket.onmessage = (event) => {
    const message = JSON.parse(event.data);
    if (message.type === 'shotResult') {
      setGameState((prev) => ({
        ...prev,
        turn: prev.turn === 'player' ? 'opponent' : 'player',
      }));
    }
  };
  socket.send(JSON.stringify({ type: 'join',player:"player1" }))

}, []);

// Frontend: Display game over screen
const [winner, setWinner] = useState(null);

useEffect(() => {
  socket.onmessage = (event) => {
    const message = JSON.parse(event.data);
    if (message.type === 'gameOver') {
      setWinner(message.winner);
      setGameState('finished');
    }
  };
}, []);

return (
  <div className="App">
    {gameState === 'finished' ? (
      <div>
        <h1>Game Over</h1>
        <p>{winner} Wins!</p>
      </div>
    ) : (
      // Render the game grid and controls
    )}
  </div>
);


javascript
// Frontend: Form for selecting ship types

const ShipSelector = ({ onSelect }) => {
  const handleChange = (event) => {
    onSelect(event.target.value);
  };

  return (
    <select onChange={handleChange}>
      {ships.map((ship, index) => (
        <option key={index} value={index}>
          {ship.type}
        </option>
      ))}
    </select>
  );
};
