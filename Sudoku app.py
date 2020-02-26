import tkinter as tk
import sys
import copy


class Application:
    def __init__(self, master, board):
        self.master = master
        self.origin_board = copy.deepcopy(board)
        self.board = board
        self.master.geometry("1920x1080")
        self.master.title("Sudoku App")
        self.master.configure(bg="white")

        self.solver(self.board)

        # Create 9x9 grid and load Sudoku puzzle
        self.grid_layout = tk.Frame(self.master)
        for row in range(9):
            for col in range(9):
                cell = tk.Label(self.grid_layout, width=10, height=5, text=self.origin_board[row][col] if self.origin_board[row][col] != 0 else "", font=("Courier", 12), borderwidth=1, relief="solid",
                                bg="white")
                cell.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        self.grid_layout.grid(row=1, column=1, padx=150)

        # Create 3x3 grid for number input
        self.numpad_layout = tk.Frame(self.master)
        count = 0
        for row in range(3):
            for col in range(3):
                numpad = tk.Label(self.numpad_layout, width=10, height=5, text=count + 1, font=("Courier", 12), borderwidth=1, relief="solid",
                                  bg="white")
                numpad.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
                count += 1
        self.numpad_layout.grid(row=1, column=2)

        # Buttons initialization
        self.button_layout = tk.Frame(self.master)

        # Clear button
        clear_button = tk.Button(self.button_layout, text="Clear", font=("Courier", 12), command=self.clear_button_press).grid(row=1, column=4, padx=50, pady=20)

        # New puzzle button
        new_button = tk.Button(self.button_layout, text="New", font=("Courier", 12)).grid(row=1, column=1, padx=50, pady=20)

        # Hint button
        hint_button = tk.Button(self.button_layout, text="Hint", font=("Courier", 12), command=self.hint_button_press).grid(row=1, column=2, padx=50, pady=20)

        # Solve button
        solve_button = tk.Button(self.button_layout, text="Solve", font=("Courier", 12), command=self.solve_button_press).grid(row=1, column=3, padx=50, pady=20)

        # Quit button
        quit_button = tk.Button(self.button_layout, text="Quit", font=("Courier", 12), command=self.quit_button_press).grid(row=1, column=5, padx=50, pady=20)

        self.button_layout.grid(row=2, column=1, columnspan=2, pady=50)

        self.master.bind("<Button-1>", self.callback)

    # Button operations
    def hint_button_press(self):
        pass

    def solve_button_press(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.grid_layout.grid_slaves(row, col)[0]['text'] == "":
                    self.grid_layout.grid_slaves(row, col)[0].configure(text=self.board[row][col])

    def clear_button_press(self):
        for row in range(len(self.origin_board)):
            for col in range(len(self.origin_board[row])):
                if self.origin_board[row][col] == 0:
                    self.grid_layout.grid_slaves(row, col)[0].configure(text="")

    def quit_button_press(self):
        sys.exit()

    # Mouse events handling
    def callback(self, event):
        widget = self.grid_layout.winfo_containing(event.x_root, event.y_root)
        if type(widget) is tk.Label:
            widget.configure(bg="sky blue")

    # Sudoku functions
    def solver(self, board):
        # find the next empty cell
        current_cell_coord = self.find_next_empty(board)

        # exit if all cells are filled
        if not current_cell_coord:
            # print('\n'.join([str(row).replace(',',' ').replace('[','').replace(']','') for row in board]))
            return True

        row, col = current_cell_coord[0], current_cell_coord[1]
        # try 1 to 9
        for i in range(1, 10):
            if self.is_valid(board, row, col, i):
                board[row][col] = i

                if self.solver(board):
                    return True

                # backtracking if return false
                board[row][col] = 0

        return False

    # find_next_empty function finds the next empty cell to work on, return None if all cells filled
    def find_next_empty(self, board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 0:
                    return [row, col]
        return None

    # isValid function checks if the input value for the current cell is valid
    def is_valid(self, board, row, col, val):
        # check if duplicate horizontally
        for cell in board[row]:
            if cell == val:
                return False

        # check if duplicate vertically
        for i in range(len(board)):
            if board[i][col] == val:
                return False

        # check if duplicate in 9-cells
        a = row // 3
        b = col // 3

        for i in range(a * 3, a * 3 + 3):
            for j in range(b * 3, b * 3 + 3):
                if board[i][j] == val:
                    return False

        # if pass all tests
        return True


if __name__ == '__main__':
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    root = tk.Tk()
    sudoku = Application(root, board)
    root.mainloop()
