This Python script is a basic simulation of orbital mechanics using the Pygame library. It visualizes the gravitational interaction between the Sun and Earth and calculates their positions over time.

### Setting Up the Environment

To run this script, you need to have Python and Pygame installed on your system. Follow these steps to set up the environment:

1. **Install Python:**
   Make sure you have Python installed on your computer. You can download it from the official Python website [here](https://www.python.org/downloads/).

2. **Install Pygame:**
   Open a terminal or command prompt and run the following command to install Pygame using pip:

   ```bash
   pip install pygame
   ```

### Running the Simulation

1. **Copy and Save the Script:**
   Save the script provided in the Python code file, for instance, `solar_simulation.py`.

2. **Execute the Script:**
   Navigate to the directory where you saved the file and run the script using the following command in your terminal or command prompt:

   ```bash
   python solar_simulation.py
   ```

3. **View the Simulation:**
   A window will open displaying the simulation of the Sun and Earth. You can view the Earth's orbit around the Sun in real-time.

4. **Close the Simulation:**
   To exit the simulation, simply close the window or press the `QUIT` button on the simulation interface.

### Code Explanation

- **Constants:**
  - The script sets up the window size (`WIDTH`, `HEIGHT`) and color constants (`WHITE`, `BLACK`, `YELLOW`, `BLUE`) using RGB values.
  - It defines astronomical constants like the Astronomical Unit (AU) and gravitational constant (G).

- **Planet Class:**
  - Represents celestial bodies, defined with attributes such as position (`x`, `y`), velocity (`x_vel`, `y_vel`), and mass.
  - The `draw` method handles rendering the planets and their orbits.
  - The `attraction` method computes gravitational forces between planets.
  - The `update_position` method updates a planet's position based on gravitational interactions with other bodies.

- **Main Loop:**
  - Initializes the `Planet` objects for the Sun and Earth.
  - Continuously updates and renders their positions on the display window until the simulation is terminated by the user.

This simulation is a simple approximation of a two-body system, illustrating basic principles of gravitational attraction and orbital mechanics. It can be expanded to include additional planets or more detailed physics modeling.