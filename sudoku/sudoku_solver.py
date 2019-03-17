import numpy as np
import sys


def rows_contain_identical_numbers(sudoku):
    for n in range(1, 10):
        if (np.sum(sudoku == n, axis=1) > 1).any():
            return True

    return False


def cols_contain_identical_numbers(sudoku):
    for n in range(1, 10):
        if (np.sum(sudoku == n, axis=0) > 1).any():
            return True

    return False


def squares_contain_identical_numbers(sudoku):
    for sr in range(3):
        for sc in range(3):
            for n in range(1, 10):
                square = sudoku[sr*3:sr*3+3, sc*3:sc*3+3]
                if (np.sum(square == n) > 1).any():
                    return True

    return False


def rules_are_broken(sudoku):
    if rows_contain_identical_numbers(sudoku) or \
       cols_contain_identical_numbers(sudoku) or \
       squares_contain_identical_numbers(sudoku):
        return True
    else:
        return False


def get_previous_empty_cell(row, col, sudoku_orig):
    flat_sudoku_orig = sudoku_orig.flatten()[:9*row + col]

    index = np.where(flat_sudoku_orig == 0)[0][-1]
    c = index % 9
    r = int((index - c)/9)

    return r, c


def get_next_cell(row, col):
    if col == 8:
        r = row + 1
        c = 0
    else:
        r = row
        c = col + 1

    return r, c


sudoku = np.array([[8, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 3, 6, 0, 0, 0, 0, 0],
                   [0, 7, 0, 0, 9, 0, 2, 0, 0],
                   [0, 5, 0, 0, 0, 7, 0, 0, 0],
                   [0, 0, 0, 0, 4, 5, 7, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 3, 0],
                   [0, 0, 1, 0, 0, 0, 0, 6, 8],
                   [0, 0, 8, 5, 0, 0, 0, 1, 0],
                   [0, 9, 0, 0, 0, 0, 4, 0, 0]])

sudoku_orig = sudoku.copy()

r = 0
c = 0
n = 1

while r < 9:
    if sudoku_orig[r, c] == 0:
        sudoku[r, c] = n

        if rules_are_broken(sudoku):
            if n == 9:
                while sudoku[r, c] == 9:
                    sudoku[r, c] = 0
                    r, c = get_previous_empty_cell(r, c, sudoku_orig)
                n = sudoku[r, c] + 1
            else:
                n += 1
        else:
            r, c = get_next_cell(r, c)
            n = 1
    else:
        r, c = get_next_cell(r, c)
        n = 1

print("Solution:\n {0}".format(sudoku))


































