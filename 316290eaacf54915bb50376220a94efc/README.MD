# Backend Functionality

## Validate Ship Placement

The `validateShipPlacement` function checks if a ship can be placed on the grid without overlapping existing ships or going out of bounds. It takes the grid, ship object, row, column, and direction as parameters.

- **Parameters**:
  - `grid`: A 2D array representing the game board.
  - `ship`: An object containing the ship's type and size.
  - `row`: The starting row index for the ship placement.
  - `col`: The starting column index for the ship placement.
  - `direction`: A string indicating the direction ('horizontal' or 'vertical').

- **Returns**: A boolean value indicating whether the ship can be placed.

## Track Game State

The `gameState` object tracks the current state of the game, including players, whose turn it is, and the game status. The WebSocket server (`wss`) listens for connections and messages to update the game state.

- **Properties**:
  - `players`: An array of player names.
  - `turn`: A string indicating whose turn it is ('player1' or 'player2').
  - `status`: A string indicating the game status ('waiting', 'playing', 'finished').

## Define Ship Types

The `ships` array defines the types of ships available in the game, including their names and sizes.

- **Elements**:
  - `type`: A string representing the ship type.
  - `size`: An integer representing the ship size.

## Check Game Over Condition

The `checkGameOver` function checks if the game is over by verifying if all cells in the grid are not 'ship'.

- **Parameters**:
  - `grid`: A 2D array representing the game board.

- **Returns**: A boolean value indicating whether the game is over.

## WebSocket Connection Handling

The WebSocket server listens for connections and messages. It processes messages of type 'shot' and 'join', updating the game state accordingly.

## Frontend Functionality

## Place Ship

The `placeShip` function places a ship on the player's grid if the placement is valid.

- **Parameters**:
  - `row`: The starting row index for the ship placement.
  - `col`: The starting column index for the ship placement.
  - `direction`: A string indicating the direction ('horizontal' or 'vertical').

## Update Turn and Game State

The frontend uses a React state hook (`useState`) to manage the game state. It updates the turn and game state based on server responses.

## Display Game Over Screen

The frontend displays a game over screen when the game is finished, showing the winner.

## Ship Selector

The `ShipSelector` component allows players to select a ship type from a dropdown menu.

- **Props**:
  - `onSelect`: A callback function that is called when a ship type is selected.

- **Returns**: A JSX element representing a dropdown menu with ship types.