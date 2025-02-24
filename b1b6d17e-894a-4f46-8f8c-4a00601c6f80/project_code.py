import pygame
import numpy as np

class Planet:
    def __init__(self, name, image, position, radius, angle, speed):
        self.name = name
        self.image = image
        self.position = position
        self.radius = radius
        self.angle = angle
        self.speed = speed

    def update(self, time_passed):
        self.angle += self.speed * time_passed
        x = int(self.position[0] + self.radius * np.cos(self.angle))
        y = int(self.position[1] + self.radius * np.sin(self.angle))
        self.position = (x, y)

class PseudoPlanet:
    def __init__(self, name, image, position, radius, angle, speed):
        self.name = name
        self.image = image
        self.position = position
        self.radius = radius
        self.angle = angle
        self.speed = speed

    def update(self, time_passed):
        self.angle += self.speed * time_passed
        x = int(self.position[0] + self.radius * np.cos(self.angle))
        y = int(self.position[1] + self.radius * np.sin(self.angle))
        self.position = (x, y)

class Moon:
    def __init__(self, name, image, parent_planet, distance, angle, speed):
        self.name = name
        self.image = image
        self.parent_planet = parent_planet
        self.distance = distance
        self.angle = angle
        self.speed = speed

    def update(self, time_passed):
        self.angle += self.speed * time_passed
        x = int(self.parent_planet.position[0] + self.distance * np.cos(self.angle))
        y = int(self.parent_planet.position[1] + self.distance * np.sin(self.angle))
        self.position = (x, y)

class SolarSystem:
    def __init__(self):
        self.planets = []
        self.moons = []
        self.pseudo_planets = []

    def add_planet(self, planet):
        self.planets.append(planet)

    def add_moon(self, moon):
        self.moons.append(moon)

    def add_pseudo_planet(self, pseudo_planet):
        self.pseudo_planets.append(pseudo_planet)

    def update(self, time_passed):
        for planet in self.planets:
            planet.update(time_passed)
        for moon in self.moons:
            moon.update(time_passed)
        for pseudo_planet in self.pseudo_planets:
            pseudo_planet.update(time_passed)

class Visuals:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, solar_system):
        self.screen.fill((0, 0, 0))  # Clear the screen with black
        self.draw_objects(solar_system.pseudo_planets)
        self.draw_objects(solar_system.planets)
        self.draw_objects(solar_system.moons)

    def draw_objects(self, objects):
        for obj in objects:
            self.screen.blit(obj.image, (obj.position[0] - obj.image.get_width() // 2, obj.position[1] - obj.image.get_height() // 2))

def main():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Solar System Simulation')
    clock = pygame.time.Clock()
    time_passed = 0

    visuals = Visuals(screen)
    solar_system = SolarSystem()

    # Load images
    sun_image = pygame.image.load('sun.png')
    earth_image = pygame.image.load('earth.png')
    moon_image = pygame.image.load('moon.png')
    ring_image = pygame.image.load('ring.png')

    # Create objects
    sun = Planet('Sun', sun_image, (screen_width // 2, screen_height // 2), 0, 0, 0)
    earth = Planet('Earth', earth_image, (screen_width // 2, screen_height // 2), 200, 0, 0.01)
    moon = Moon('Moon', moon_image, earth, 50, 0, 0.05)
    ring = PseudoPlanet('Ring', ring_image, (screen_width // 2, screen_height // 2), 210, 0, 0.01)

    # Add objects to the solar system
    solar_system.add_planet(sun)
    solar_system.add_planet(earth)
    solar_system.add_moon(moon)
    solar_system.add_pseudo_planet(ring)

    running = True
    while running:
        time_passed = clock.tick(60) / 1000.0
        solar_system.update(time_passed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        visuals.draw(solar_system)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
