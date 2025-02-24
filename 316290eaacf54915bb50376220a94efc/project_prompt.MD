### Project Overview

**Project Name:** BattleShips Game

**Purpose:** Develop a simple web-based Battleships game where two players can play against each other over the internet.

**Scope:**
- Basic single-player mode
- Online multiplayer mode (using WebSockets)
- User-friendly interface
- Responsive design for different screen sizes

### Project Requirements

1. **Backend:**
   - Implement a server to handle game logic and WebSocket communication.
   
2. **Frontend:**
   - Create a responsive user interface with two grids for each player to place ships and take turns shooting.
   - Display the game state, including hits, misses, and sunk ships.

### Code Architecture

**Pattern:** MVC (Model-View-Controller)

1. **Model:**
   - Game logic
   - Player data
   - Ship data

2. **View:**
   - HTML/CSS for the user interface
   - JavaScript to handle user interactions and update the UI

3. **Controller:**
   - WebSocket server logic
   - Event handling (e.g., button clicks, mouse movements)
   - Communication between Model and View

### Development Steps

#### Step 1: Project Setup

1. **Create Project Directory Structure:**
   ```
   battle-ships-game/
   ├── backend/
   │   ├── controllers/
   │   ├── models/
   │   ├── routes/
   │   └── server.js
   ├── frontend/
   │   ├── public/
   │   │   └── index.html
   │   ├── src/
   │   │   ├── components/
   │   │   ├── App.js
   │   │   └── styles.css
   │   ├── package.json
   │   └── webpack.config.js
   ├── .gitignore
   ├── package.json
   └── README.md
   ```

2. **Initialize Git Repository:**
   ```
   git init
   ```

#### Step 2: Backend Development

1. **Set Up Node.js Project:**
   ```
   cd backend
   npm init -y
   npm install express ws body-parser cors
   ```

2. **Create Server File (`server.js`):**
   ```javascript
   const express = require('express');
   const WebSocket = require('ws');
   const bodyParser = require('body-parser');
   const cors = require('cors');

   const app = express();
   const wss = new WebSocket.Server({ port: 3001 });

   // Middleware
   app.use(bodyParser.json());
   app.use(cors());

   // Routes
   app.get('/', (req, res) => {
     res.send('BattleShips Game Server');
   });

   // WebSocket connection handling
   wss.on('connection', (ws) => {
     ws.on('message', (message) => {
       console.log(`Received: ${message}`);
       // Broadcast to all connected clients except the sender
       wss.clients.forEach((client) => {
         if (client.readyState === WebSocket.OPEN && client !== ws) {
           client.send(message);
         }
       });
     });

     ws.on('close', () => {
       console.log('Client disconnected');
     });
   });

   app.listen(3000, () => {
     console.log('Server is running on port 3000');
   });
   ```

#### Step 3: Frontend Development

1. **Set Up React Project:**
   ```
   cd ../frontend
   npx create-react-app .
   npm install --save react-router-dom ws
   ```

2. **Create Basic Components:**

   - `App.js`: Main component to hold the game state and logic.
   - `Grid.js`: Component to display the game grid.
   - `Ship.js`: Component to represent individual ships on the grid.

3. **Implement Game Logic in `App.js`:**
   ```javascript
   import React, { useState, useEffect } from 'react';
   import Grid from './Grid';
   import Ship from './Ship';

   const App = () => {
     const [gridSize, setGridSize] = useState(10);
     const [playerGrid, setPlayerGrid] = useState([]);
     const [opponentGrid, setOpponentGrid] = useState([]);
     const [turn, setTurn] = useState('player');

     // Initialize grids
     useEffect(() => {
       const newPlayerGrid = Array.from({ length: gridSize }, () =>
         Array(gridSize).fill(null)
       );
       const newOpponentGrid = Array.from({ length: gridSize }, () =>
         Array(gridSize).fill(null)
       );

       setPlayerGrid(newPlayerGrid);
       setOpponentGrid(newOpponentGrid);
     }, [gridSize]);

     // Handle WebSocket connection
     useEffect(() => {
       const socket = new WebSocket('ws://localhost:3001');

       socket.onopen = () => {
         console.log('WebSocket connection established');
       };

       socket.onmessage = (event) => {
         const message = JSON.parse(event.data);
         if (message.type === 'opponentAction') {
           // Update opponent grid based on opponent's action
           setOpponentGrid((prevGrid) => {
             prevGrid[message.row][message.col] = message.result;
             return [...prevGrid];
           });
         }
       };

       socket.onclose = () => {
         console.log('WebSocket connection closed');
       };

       return () => {
         socket.close();
       };
     }, []);

     // Handle placing ships
     const placeShip = (row, col) => {
       setPlayerGrid((prevGrid) => {
         prevGrid[row][col] = 'ship';
         return [...prevGrid];
       });
     };

     // Handle shooting at opponent's grid
     const shoot = (row, col) => {
       if (turn === 'player') {
         socket.send(JSON.stringify({ type: 'opponentAction', row, col }));
         setTurn('opponent');
       }
     };

     return (
       <div className="App">
         <h1>BattleShips Game</h1>
         <Grid grid={playerGrid} onPlaceShip={placeShip} />
         <Grid grid={opponentGrid} onShoot={shoot} turn={turn} />
       </div>
     );
   };

   export default App;
   ```

4. **Create Grid Component (`Grid.js`):**
   ```javascript
   import React from 'react';

   const Grid = ({ grid, onPlaceShip, onShoot, turn }) => {
     return (
       <table>
         <tbody>
           {grid.map((row, rowIndex) => (
             <tr key={rowIndex}>
               {row.map((cell, colIndex) => (
                 <td
                   key={colIndex}
                   onClick={() =>
                     turn === 'player' && onShoot(rowIndex, colIndex)
                   }
                   style={{
                     width: '50px',
                     height: '50px',
                     border: '1px solid black',
                     background:
                       cell === 'ship'
                         ? 'blue'
                         : cell === 'hit'
                         ? 'red'
                         : cell === 'miss'
                         ? 'gray'
                         : 'white',
                   }}
                 >
                   {cell === 'ship' && <Ship />}
                 </td>
               ))}
             </tr>
           ))}
         </tbody>
       </table>
     );
   };

   export default Grid;
   ```

5. **Create Ship Component (`Ship.js`):**
   ```javascript
   import React from 'react';

   const Ship = () => {
     return <div style={{ width: '20px', height: '20px', backgroundColor: 'blue' }} />;
   };

   export default Ship;
   ```

#### Step 4: Testing and Deployment

1. **Run the Backend Server:**
   ```
   cd ../backend
   node server.js
   ```

2. **Start the Frontend Development Server:**
   ```
   cd ../frontend
   npm start
   ```

3. **Test the Game:**
   - Open two browser tabs to test the game.
   - Ensure that placing ships and shooting work as expected.

4. **Deploy to a Web Server:**
   - Build the frontend project for production:
     ```bash
     cd ../frontend
     npm run build
     ```
   - Deploy the `build` folder to your web server.

### Conclusion

This set of instructions provides a structured approach to developing a simple web-based Battleships game. The backend handles the game logic and WebSocket communication, while the frontend manages the user interface. Each component has been outlined for easy implementation, and testing and deployment steps are included to ensure a smooth development process.