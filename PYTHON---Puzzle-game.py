import random

def create_puzzle(size):
    """Creates a size x size puzzle with numbers 1 to size^2 - 1."""
    puzzle = list(range(1, size*size)) + [0]
    random.shuffle(puzzle)
    return [puzzle[i*size:(i+1)*size] for i in range(size)]

def print_puzzle(puzzle):
    """Prints the puzzle in a readable format."""
    for row in puzzle:
        print(' '.join(str(n).rjust(2, ' ') for n in row))

def find_empty(puzzle):
    """Finds the position of the empty space (0)."""
    for i, row in enumerate(puzzle):
        if 0 in row:
            return i, row.index(0)

def is_solved(puzzle):
    """Checks if the puzzle is solved."""
    size = len(puzzle)
    correct = list(range(1, size*size)) + [0]
    return puzzle == [correct[i*size:(i+1)*size] for i in range(size)]

def move(puzzle, direction):
    """Moves the empty space (0) in the given direction if possible."""
    x, y = find_empty(puzzle)
    size = len(puzzle)
    if direction == 'up' and x > 0:
        puzzle[x][y], puzzle[x-1][y] = puzzle[x-1][y], puzzle[x][y]
    elif direction == 'down' and x < size-1:
        puzzle[x][y], puzzle[x+1][y] = puzzle[x+1][y], puzzle[x][y]
    elif direction == 'left' and y > 0:
        puzzle[x][y], puzzle[x][y-1] = puzzle[x][y-1], puzzle[x][y]
    elif direction == 'right' and y < size-1:
        puzzle[x][y], puzzle[x][y+1] = puzzle[x][y+1], puzzle[x][y]
    else:
        print("Invalid move!")

def main():
    size = 3  # 3x3 puzzle
    puzzle = create_puzzle(size)
    
    while not is_solved(puzzle):
        print_puzzle(puzzle)
        move_input = input("Move (up, down, left, right): ").lower()
        move(puzzle, move_input)
    
    print("Congratulations! You've solved the puzzle!")
    print_puzzle(puzzle)

if __name__ == "__main__":
    main()
