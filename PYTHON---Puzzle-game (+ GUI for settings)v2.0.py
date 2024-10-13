import tkinter as tk
import random
from tkinter import messagebox

class PuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Puzzle Game")
        
        self.grid_size = 3  # Default puzzle size (3x3)
        self.board = []
        
        # Frame for puzzle grid
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)
        
        # Create settings button
        settings_btn = tk.Button(self.root, text="Settings", command=self.open_settings)
        settings_btn.pack(pady=10)
        
        # Create reset button
        reset_btn = tk.Button(self.root, text="Reset", command=self.reset_game)
        reset_btn.pack(pady=5)
        
        self.create_board()
    
    def create_board(self):
        self.buttons = []
        numbers = list(range(1, self.grid_size**2)) + [0]
        random.shuffle(numbers)
        self.board = [numbers[i * self.grid_size:(i + 1) * self.grid_size] for i in range(self.grid_size)]
        
        for row in range(self.grid_size):
            button_row = []
            for col in range(self.grid_size):
                value = self.board[row][col]
                btn = tk.Button(self.frame, text=str(value) if value != 0 else ' ', font=("Arial", 20), width=4, height=2, command=lambda r=row, c=col: self.move_tile(r, c))
                btn.grid(row=row, column=col)
                button_row.append(btn)
            self.buttons.append(button_row)
    
    def move_tile(self, row, col):
        # Find the position of the empty space (0)
        empty_row, empty_col = None, None
        for i in range(self.grid_size):
            if 0 in self.board[i]:
                empty_row, empty_col = i, self.board[i].index(0)
                break
        
        # Check if the move is valid (adjacent to the empty space)
        if abs(empty_row - row) + abs(empty_col - col) == 1:
            # Swap the clicked tile with the empty space
            self.board[empty_row][empty_col], self.board[row][col] = self.board[row][col], self.board[empty_row][empty_col]
            self.update_buttons()
        
        # Check if the puzzle is solved
        if self.is_solved():
            messagebox.showinfo("Puzzle Solved", "Congratulations! You solved the puzzle!")
    
    def update_buttons(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                value = self.board[row][col]
                self.buttons[row][col].config(text=str(value) if value != 0 else ' ')
    
    def is_solved(self):
        target = list(range(1, self.grid_size**2)) + [0]
        return all(self.board[i // self.grid_size][i % self.grid_size] == target[i] for i in range(self.grid_size**2))
    
    def reset_game(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.create_board()
    
    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        
        tk.Label(settings_window, text="Choose puzzle size:").pack(pady=10)
        
        size_var = tk.IntVar(value=self.grid_size)
        
        size3x3 = tk.Radiobutton(settings_window, text="3x3", variable=size_var, value=3)
        size3x3.pack(anchor=tk.W)
        
        size4x4 = tk.Radiobutton(settings_window, text="4x4", variable=size_var, value=4)
        size4x4.pack(anchor=tk.W)
        
        size5x5 = tk.Radiobutton(settings_window, text="5x5", variable=size_var, value=5)
        size5x5.pack(anchor=tk.W)
        
        save_btn = tk.Button(settings_window, text="Save", command=lambda: self.apply_settings(size_var.get(), settings_window))
        save_btn.pack(pady=10)
    
    def apply_settings(self, size, window):
        self.grid_size = size
        self.reset_game()  # Recreate the board with new size
        window.destroy()

# Main function to run
