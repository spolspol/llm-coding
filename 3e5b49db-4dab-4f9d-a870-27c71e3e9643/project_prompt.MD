### Instructions to Build a Solar System Simulation in Python

**Project Overview:**
Create a graphical simulation of the Solar System, featuring all major planets, pseudo-planets (like dwarf planets), and their moons. This simulation will use a graphical library for rendering and provide user interactions for navigation and information display.

---

### 1. Code Architecture

**Architecture Pattern:**
- Model-View-Controller (MVC) Pattern

**Components:**
1. **Model**: Represents the data & logic (planets, moons).
2. **View**: Responsible for the graphical representation of the solar system.
3. **Controller**: Handles user interaction and updates the model/view accordingly.

---

### 2. Functional Components

#### 2.1 Model

- **Planet Class**
  - Attributes: `name`, `diameter`, `distance_from_sun`, `orbital_period`, `moons`
  - Methods: `update_position()`

- **Moon Class**
  - Attributes: `name`, `diameter`, `orbital_period`
  - Methods: `update_position()`

- **SolarSystem Class**
  - Attributes: `planets` (list of Planet objects)
  - Methods: `add_planet()`, `remove_planet()`, `update()`

#### 2.2 View

- **Graphical Interface**
  - Initialize graphical window (using libraries like Pygame or Tkinter).
  - Draw the sun at the center.
  - Render planets based on their attributes (size, distance, position).
  - Draw moons in relation to their respective planets.
  - Implement background rendering and visual effects (like stars).

- **Information Display**
  - Show information about planets and moons when selected by the user.
  - Implement zoom in/out functionality for better visibility.

#### 2.3 Controller

- **Input Handling**
  - Capture keyboard and mouse inputs to navigate the simulation.
  - Implement functions for selecting planets/moons and displaying their info.
  
- **Updating Logic**
  - Create a game loop that updates the model and view continuously.
  - Synchronize the movement of planets and moons according to their orbital mechanics.

---

### 3. Implementation Steps

#### Step 1: Set Up Environment

- Install necessary libraries:
  - Graphical library (e.g., Pygame): `pip install pygame`
  - Other dependencies as needed.

#### Step 2: Develop the Model

1. **Create Planet and Moon Classes**:
   - Implement attributes and methods as specified.
2. **Implement SolarSystem Class**:
   - Include methods to manage planets and their interactions.

#### Step 3: Develop the View

1. **Initialize Graphical Window**:
   - Set up main window dimensions and title.
2. **Render Solar System**:
   - Create drawing functions for sun, planets, and moons.
3. **Information Display**:
   - Set up a mechanism to display details about selected celestial bodies.

#### Step 4: Develop the Controller

1. **Input Handling Logic**:
   - Capture user inputs for navigation and selection.
2. **Game Loop**:
   - Implement a loop that updates the model and redraws the view.

#### Step 5: Testing

- Perform unit tests on Model components (Planet and Moon classes).
- Conduct integration tests for the interaction between Model, View, and Controller.
- Test graphical rendering and user interactions to ensure functionality.

#### Step 6: Optimization

- Optimize the rendering performance for smoother animations.
- Adjust the calculations for planet orbits to reflect accurate positions over time.

#### Step 7: Documentation

- Create user documentation on how to run and interact with the simulation.
- Comment the code and create technical documentation for future development.

---

### 4. Final Considerations

- Specify the user interface design and any specific UX considerations.
- Consider further enhancements like sound effects or educational modes.

By following these structured instructions, you will be able to create a graphical simulation of the Solar System that is both interactive and educational.