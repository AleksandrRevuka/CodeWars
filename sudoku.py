import numpy as np

def make_sections(array: np.array) -> list:
    puzzle_sections = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            section = array[i:i+3, j:j+3].flatten().tolist()
            puzzle_sections.append(section)
    return puzzle_sections


def sudoku(puzzle: list) -> list:
    """return the solved puzzle as a 2d array of 9 x 9"""
    result_numbers = set(i for i in range(10))
    puzzle = np.array(puzzle, np.int32)

    while True:

        zero_indices = np.where(puzzle == 0)
        puzzle_sections = make_sections(puzzle)

        if zero_indices[0].size == 0:
            break 

        for row, col in zip(*zero_indices):

            section = set(puzzle_sections[(row // 3 * 3) + (col // 3)])
            col_value = set(puzzle[:, col])
            row_value = set(puzzle[row, :])
            difference = result_numbers - col_value - row_value - section

            if len(difference) == 1:
                puzzle[row, col] = difference.pop()

    return puzzle.tolist()


if __name__ == '__main__':

    puzzle = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]
    
    result = sudoku(puzzle)
    print(result)