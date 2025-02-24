## Solar System Simulation

This application simulates a simple solar system with planets, moons, and pseudo-planets. The simulation includes objects like the Sun, Earth, and its Moon, as well as a ring representing a pseudo-planetary object. These celestial bodies orbit around each other in a visually appealing manner, rendered through Pygame, a popular Python library for game development.

### Features

- **Planets and Pseudo-Planets**: Simulate celestial bodies with specified orbits and speeds.
- **Moons**: Enable the creation of satellite bodies with their respective primary planet.
- **Graphical Representation**: Use Pygame to visually depict the solar system and its movements.
- **Customizable Simulation**: Easily extend the simulation by adding more planets, moons, or other celestial objects.

### Installation Instructions

To run this application, you need Python installed on your system along with the `pygame` and `numpy` libraries. You can follow the instructions below to set up your environment:

1. **Install Python**: Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Pygame and Numpy**:
   You can install the required libraries using `pip` (Python's package installer). Open your terminal or command prompt and run the following commands:

   ```bash
   pip install pygame
   pip install numpy
   ```

3. **Prepare Image Resources**:
   Ensure the following image files are available in the same directory as your script:
   - `sun.png` for the Sun
   - `earth.png` for the Earth
   - `moon.png` for the Moon
   - `ring.png` for the pseudo-planetary object

   These images will be used to represent the respective celestial objects on the screen.

### How to Run

1. **Navigate to Project Directory**:
    Open your terminal or command prompt and navigate to the directory where your code and image files are located.

2. **Run the Application**:
   Execute the script using Python:

   ```bash
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the name of the Python script file.

3. **Exit the Simulation**:
   Close the simulation window or use the window's close (X) button to terminate the application.

### Customization

To expand the simulation:

- **Add New Planets/Moons**: Instantiate additional `Planet`, `Moon`, or `PseudoPlanet` objects with appropriate parameters.
- **Modify Speeds and Orbits**: Customize the orbital radius and angular speeds to create different orbital behaviors and scenarios.

### Code Overview

- **Planet, Moon, PseudoPlanet Classes**: These classes define the behavior and properties of the celestial bodies.
- **SolarSystem Class**: Manages the collection of planets, moons, and pseudo-planets and updates their states.
- **Visuals Class**: Handles drawing the celestial objects on the Pygame window.
- **Main Function**: Initializes Pygame, creates objects, updates the simulation in a loop, and renders the visuals.

This simulation provides a foundational framework for developing complex solar system models and serves as an educational tool for understanding orbital dynamics.