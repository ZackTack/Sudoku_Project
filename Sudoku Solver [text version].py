# sudoku solver
def solver(board):
    # find the next empty cell
    current_cell_coord = find_next_empty(board)

    # exit if all cells are filled
    if not current_cell_coord:
        print('\n'.join([str(row).replace(',',' ').replace('[','').replace(']','') for row in board]))
        return True

    row, col = current_cell_coord[0], current_cell_coord[1]
    # try 1 to 9
    for i in range(1, 10):
        if isValid(board, row, col, i):
            board[row][col] = i

            if solver(board):
                return True

            # backtracking if return false
            board[row][col] = 0

    return False


# find_next_empty function finds the next empty cell to work on, return None if all cells filled
def find_next_empty(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return [row, col]
    return None


# isValid function checks if the input value for the current cell is valid
def isValid(board, row, col, val):
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

    for i in range(a*3, a*3+3):
        for j in range(b*3, b*3+3):
            if board[i][j] == val:
                return False

    # if pass all tests
    return True


def main():
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
    import traceback
    try:
        if solver(board):
            pass
        else:
            print("failed")
    except Exception as e:
        traceback.print_exc()


if __name__ == '__main__':
    main()
