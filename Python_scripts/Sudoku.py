import unittest
import numpy as np

def is_sudoku(matrix, rows, columns):
    size = rows * columns
    matrix = np.array(matrix)

    # sprawdzenie czy Macierz ma prawidłowy rozmiar

    if matrix.size != size * size:
        return False

    if not rows_ok(matrix):
        return False

    if not columns_ok(matrix):
        return False

    if not tiles_ok(matrix,rows,columns):
        return False
    return True


def rows_ok(matrix):
    for row in matrix:
        if not check_duplicates(row):
            return False
    return True


def columns_ok(matrix):
    for i in range(0, matrix.shape[0]):
        if not check_duplicates(matrix[:, i]):
            return False
    return True


def tiles_ok(matrix, rows, columns):
    size = rows * columns
    for i in range(0, int(matrix.shape[1] / columns)):
        for j in range(0, int(matrix.shape[0] / rows)):
            tile = []
            for number in range(0, size):
                tile.append(matrix[int(number / rows)][int(number % columns)])
            tile = np.array(tile)
            if not check_duplicates(tile):
                return False
    return True


def check_duplicates(matrix):
    # check if there are duplicates
    numbers = set()
    for number in matrix:
        numbers.add(number)
    OKnumbers = set(range(1, matrix.shape[0]+1))
    return numbers == OKnumbers



class TestSudoku(unittest.TestCase):

    def testOK(self):
        sudoku = [[1, 4, 9, 3, 6, 8, 5, 7, 2], [7, 2, 8, 1, 5, 4, 3, 9, 6], [5, 3, 6, 9, 2, 7, 1, 4, 8],
                  [2, 5, 4, 6, 7, 3, 8, 1, 9], [8, 9, 3, 2, 4, 1, 6, 5, 7], [6, 7, 1, 8, 9, 5, 2, 3, 4],
                  [9, 8, 5, 7, 3, 6, 4, 2, 1], [3, 1, 2, 4, 8, 9, 7, 6, 5], [4, 6, 7, 5, 1, 2, 9, 8, 3]]
        self.assertTrue(is_sudoku(sudoku, 3, 3))

    def testWrongSize(self):
        sudoku = [[1, 4, 9, 3, 6, 8, 5, 7, 2], [7, 2, 8, 1, 5, 4, 3, 9, 6], [5, 3, 6, 9, 2, 7, 1, 4, 8],
                  [2, 5, 4, 6, 7, 3, 8, 1, 9], [8, 9, 3, 2, 4, 1, 6, 5, 7], [6, 7, 1, 8, 9, 5, 2, 3, 4],
                  [9, 8, 5, 7, 3, 6, 4, 2, 1], [3, 1, 2, 4, 8, 9, 7, 6, 5], [4, 6, 7, 5, 1, 2, 9, 8, 3]]
        self.assertFalse(is_sudoku(sudoku, 2, 3))



    def testWrong(self):
        sudoku = [[1, 4, 9, 3, 6, 8, 5, 7, 2], [7, 1, 8, 1, 5, 4, 3, 9, 6], [5, 3, 6, 9, 2, 7, 1, 4, 8],
                  [2, 5, 4, 6, 7, 3, 8, 1, 9], [8, 9, 3, 2, 4, 1, 6, 5, 7], [6, 7, 1, 8, 9, 5, 2, 3, 4],
                  [9, 8, 5, 7, 3, 6, 4, 2, 1], [3, 1, 2, 4, 8, 9, 7, 6, 5], [4, 6, 7, 5, 1, 2, 9, 8, 3]]
        self.assertFalse(is_sudoku(sudoku, 3, 3))

    def testWrongTile(self):
        sudoku = [[1, 9, 8, 7, 6, 5, 4, 3, 2], [2, 1, 9, 8, 7, 6, 5, 4, 3], [3, 2, 1, 9, 8, 7, 6, 5, 4],
                  [4, 3, 2, 1, 9, 8, 7, 6, 5], [5, 4, 3, 2, 1, 9, 8, 7, 6], [6, 5, 4, 3, 2, 1, 9, 8, 7],
                  [7, 6, 5, 4, 3, 2, 1, 9, 8], [8, 7, 6, 5, 4, 3, 2, 1, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1]]
        self.assertFalse(is_sudoku(sudoku, 3, 3))

    def testWrongColumn(self):
        sudoku = [[1, 9, 8, 7, 6, 5, 4, 3, 2], [1, 9, 8, 7, 6, 5, 4, 3, 2], [1, 9, 8, 7, 6, 5, 4, 3, 2],
                  [1, 9, 8, 7, 6, 5, 4, 3, 2], [1, 9, 8, 7, 6, 5, 4, 3, 2], [1, 9, 8, 7, 6, 5, 4, 3, 2],
                  [1, 9, 8, 7, 6, 5, 4, 3, 2], [1, 9, 8, 7, 6, 5, 4, 3, 2], [1, 9, 8, 7, 6, 5, 4, 3, 2]]
        self.assertFalse(is_sudoku(sudoku, 3, 3))

    def testWrongLine(self):
        sudoku = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3],
                  [4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6, 6],
                  [7, 7, 7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9]]
        self.assertFalse(is_sudoku(sudoku, 3, 3))

    def testWrongSet(self):
        sudoku = [[10, 4, 9, 3, 6, 8, 5, 7, 2], [7, 2, 8, 1, 5, 4, 3, 9, 6], [5, 3, 6, 9, 2, 7, 1, 4, 8],
                  [2, 5, 4, 6, 7, 3, 8, 1, 9], [8, 9, 3, 2, 4, 1, 6, 5, 7], [6, 7, 1, 8, 9, 5, 2, 3, 4],
                  [9, 8, 5, 7, 3, 6, 4, 2, 1], [3, 1, 2, 4, 8, 9, 7, 6, 5], [4, 6, 7, 5, 1, 2, 9, 8, 3]]
        self.assertFalse(is_sudoku(sudoku, 3, 3))

if __name__ == '__main__':
    unittest.main()
