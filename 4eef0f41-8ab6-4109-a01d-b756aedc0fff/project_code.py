import tkinter as tk
from tkinter import messagebox
import random

class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Game")
        self.geometry("400x300")
        self.player_score = 0
        self.target_score = 10
        self.leaderboard = []

        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(self, text="Your Score: 0", font=("Arial", 16))
        self.label.pack(pady=20)

        self.button = tk.Button(self, text="Click Me!", font=("Arial", 14), command=self.update_score)
        self.button.pack(pady=10)

        self.leaderboard_button = tk.Button(self, text="View Leaderboard", font=("Arial", 14), command=self.view_leaderboard)
        self.leaderboard_button.pack(pady=10)

    def update_score(self):
        self.player_score += random.randint(1, 3)
        self.label.config(text=f"Your Score: {self.player_score}")

        if self.player_score >= self.target_score:
            self.game_over()

    def game_over(self):
        messagebox.showinfo("Game Over", f"You've reached the target score of {self.target_score}!")
        self.leaderboard.append(self.player_score)
        self.player_score = 0
        self.label.config(text=f"Your Score: {self.player_score}")

    def view_leaderboard(self):
        leaderboard_text = "\n".join(f"Score: {score}" for score in sorted(self.leaderboard, reverse=True))
        messagebox.showinfo("Leaderboard", leaderboard_text)

if __name__ == "__main__":
    game = Game()
    game.mainloop()
