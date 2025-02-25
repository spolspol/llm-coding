import randomimport tkinter as tk
from tkinter import messagebox

class Game:
    def __init__(self):
        self.guesses = 10
        self.grid_size = 10
        self.ships = [[0, 1], [2, 3], [5, 6]]  # example ship locations
        self.grid = [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def create_gui(self):
        self.root = tk.Tk()
        self.root.title("Guess the Ship")

        self.label_guesses = tk.Label(self.root, text=f"Guesses left: {self.guesses}")
        self.label_guesses.pack()

        self.canvas = tk.Canvas(self.root, width=self.grid_size*20, height=self.grid_size*20)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.canvas_click)
        self.draw_grid()

    def draw_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                x1 = j * 20
                y1 = i * 20
                x2 = (j + 1) * 20
                y2 = (i + 1) * 20
                self.canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='black')

    def update_guesses(self):
        self.label_guesses.config(text=f"Guesses left: {self.guesses}")

    def guess(self, i, j):
        if [i, j] in self.ships:
            messagebox.showinfo("Hit", "You hit a ship!")
            self.ships.remove([i, j])
            self.canvas.create_oval(j*20+5, i*20+5, (j+1)*20-5, (i+1)*20-5, fill='red')
            if not self.ships:
                messagebox.showinfo("Game Over", "You won!")
                self.root.quit()
        else:
            messagebox.showinfo("Miss", "You missed!")
            self.canvas.create_oval(j*20+5, i*20+5, (j+1)*20-5, (i+1)*20-5, fill='grey')
            self.guesses -= 1
            self.update_guesses()
            if self.guesses == 0:
                messagebox.showinfo("Game Over", "You lost!")
                self.root.quit()

    def canvas_click(self, event):
        i = event.y // 20
        j = event.x // 20
        self.guess(i, j)

    def play(self):
        self.create_gui()
        self.root.mainloop()

if __name__ == "__main__":
    game = Game()
    game.play()