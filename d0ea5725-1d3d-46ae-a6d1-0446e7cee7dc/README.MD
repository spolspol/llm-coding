## Tic-Tac-Toe Game with WebSockets

### Introduction
This project is a simple Tic-Tac-Toe game implemented in Python using Flask and Flask-SocketIO to manage WebSocket connections for real-time game updates. The application is designed using the Model-View-Controller (MVC) pattern.

### Project Structure
- **`static/`**: Contains client-side resources - HTML, CSS, and JavaScript files.
- **`src/`**: Contains server-side code in Python.
- **`README.md`**: Comprehensive documentation for the project.

### Setting Up the Environment

#### Prerequisites
- Python 3.x installed on your machine.
- `pip` for package management.

#### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd tic-tac-toe-websockets
   ```

2. **Create and activate a virtual environment:**

   On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install project dependencies:**
   ```bash
   pip install flask flask-socketio
   ```

### Running the Application

1. **Start the server:**
   ```bash
   python src/server.py
   ```

2. **Access the game:**
   - Open a web browser and go to `http://localhost:5000`.
   - To play a multiplayer game, open the link in two separate browser windows or tabs.

### Game Features

- **Game Logic**: Managed by the `Game` class, including initialization, move handling, win detection, and game reset.
- **WebSockets**: Real-time updates through WebSocket connections powered by Flask-SocketIO.
- **User Interface**: Responsive UI with a grid-based board, built using HTML, CSS, and JavaScript.

### Testing and Deployment

- **Testing**: Implement unit tests for the `Game` class logic and integration tests for Flask-SocketIO server communications.
- **Deployment**: The application can be deployed on platforms like Heroku or DigitalOcean that support Python web applications.

### Documentation Overview

- **User Documentation**: Installation and usage instructions for end-users.
- **Developer Documentation**: Details on project structure, code architecture, and guidance on potential improvements.

### Future Enhancements

- Implement score tracking.
- Add player authentication.
- Design an improved user interface.
- Develop a multiplayer lobby system.

### License
This project is licensed under the MIT License.