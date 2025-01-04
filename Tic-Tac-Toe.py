import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        self.board = [None] * 9
        self.current_player = "X"

        self.buttons = []
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2, 
            command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] is not None or self.check_winner() is not None:
            return
    
        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)
        
        winner = self.check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            self.reset_game()
        elif all(self.board):  # Check for a draw
            messagebox.showinfo("Game Over", "It's a Draw!")
            self.reset_game()
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6] 
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] is not None:
                return self.board[combo[0]]
        return None
    
    def reset_game(self):
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"

root = tk.Tk()

game = TicTacToe(root)

root.mainloop()
