from tkinter import Tk, Button, Label, messagebox
import sqlite3

# Database setup
connection = sqlite3.connect('tic_tac_toe.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY, player1_id INTEGER, player2_id INTEGER, state TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS moves (id INTEGER PRIMARY KEY, game_id INTEGER, player_id INTEGER, move TEXT)''')
connection.commit()

# Game logic
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.state = {'board': [['' for _ in range(3)] for _ in range(3)], 'result': 'ongoing'}
        self.game_id = None

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(text='', font=('normal', 20), width=6, height=2,
                                          command=lambda i=i, j=j: self.next_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)

        self.label = Label(text=f"Player {self.current_player} turn", font=('normal', 15))
        self.label.grid(row=3, column=0, columnspan=3)

    def next_move(self, row, col):
        if self.state['board'][row][col] == '' and self.state['result'] == 'ongoing':
            self.state['board'][row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            self.update_status()
            if self.check_winner(row, col):
                self.state['result'] = f'Player {self.current_player} wins'
            elif all(self.state['board'][i][j] != '' for i in range(3) for j in range(3)):
                self.state['result'] = 'Draw'
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.label.config(text=f"Player {self.current_player} turn")

    def update_status(self):
        self.label.config(text=f"Player {self.current_player} turn")
        if self.state['result'] != 'ongoing':
            messagebox.showinfo("Game Over", self.state['result'])
            self.clear_board()

    def check_winner(self, last_row, last_col):
        # Check horizontal, vertical, and diagonal lines
        row = self.state['board'][last_row]
        if all([cell == self.current_player for cell in row]):
            return True

        col = [self.state['board'][i][last_col] for i in range(3)]
        if all([cell == self.current_player for cell in col]):
            return True

        if all([self.state['board'][i][i] == self.current_player for i in range(3)]) or \
           all([self.state['board'][i][2 - i] == self.current_player for i in range(3)]):
            return True

        return False

    def clear_board(self):
        self.state = {'board': [['' for _ in range(3)] for _ in range(3)], 'result': 'ongoing'}
        self.current_player = 'X'
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')
        self.label.config(text=f"Player {self.current_player} turn")

def main():
    root = Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
