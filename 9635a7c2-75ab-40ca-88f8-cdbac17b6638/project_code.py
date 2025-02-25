import tkinter as tkfrom random import randint

class Player:
    def __init__(self, name):
        self.name = name
        self.ships = []

class Ship:
    def __init__(self, length, x, y, orientation):
        self.length = length
        self.x = x
        self.y = y
        self.orientation = orientation
        self.hits = 0

class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Battleships")
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.grid_size = 10
        self.current_turn = 1
        self.game_over = False
        self.create_grids()

    def create_grids(self):
        self.grids = [[], []]
        for p in range(2):
            for i in range(self.grid_size):
                row = []
                for j in range(self.grid_size):
                    button = tk.Button(self.root, text=" ", command=lambda i=i, j=j: self.click(i, j, p), height=2, width=3)
                    button.grid(row=i, column=j + p * (self.grid_size + 2))
                    row.append(button)
                self.grids[p].append(row)

    def place_ships(self, player, ships):
        for ship in ships:
            placed = False
            while not placed:
                x = randint(0, self.grid_size - 1)
                y = randint(0, self.grid_size - 1)
                orientation = randint(0, 1)
                if orientation == 0 and x + ship[0] <= self.grid_size:
                    if all(self.is_valid(x + i, y) for i in range(ship[0])):
                        for i in range(ship[0]):
                            self.grids[player][x + i][y].config(bg="gray")
                        player.ships.append(Ship(ship[0], x, y, orientation))
                        placed = True
                elif orientation == 1 and y + ship[0] <= self.grid_size:
                    if all(self.is_valid(x, y + i) for i in range(ship[0])):
                        for i in range(ship[0]):
                            self.grids[player][x][y + i].config(bg="gray")
                        player.ships.append(Ship(ship[0], x, y, orientation))
                        placed = True

    def is_valid(self, x, y):
        return True

    def check_win(self, player):
        return all(ship.hits == ship.length for ship in player.ships)

    def click(self, i, j, player):
        if self.game_over or player == self.current_turn - 1:
            return
        target = self.player1 if player == 1 else self.player2
        for ship in target.ships:
            if ship.orientation == 0 and ship.x <= i < ship.x + ship.length and j == ship.y:
                ship.hits += 1
                self.grids[player][i][j].config(text="X", bg="red")
                break
            elif ship.orientation == 1 and ship.y <= j < ship.y + ship.length and i == ship.x:
                ship.hits += 1
                self.grids[player][i][j].config(text="X", bg="red")
                break
        else:
            self.grids[player][i][j].config(text="O", bg="blue")

        if self.check_win(target):
            self.game_over = True
            self.root.title(f"Game Over - Player {self.current_turn} wins!")
        else:
            self.current_turn = 3 - self.current_turn

    def start(self):
        ships = [(5, "A"), (4, "B"), (3, "C"), (3, "D"), (2, "E")]
        self.place_ships(self.player1, ships)
        self.place_ships(self.player2, ships)
        self.root.mainloop()

if __name__ == "__main__":
    game = Game()
    game.start()