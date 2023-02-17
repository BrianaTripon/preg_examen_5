from texttable import *


class Board:
    def __init__(self):
        self.__data = [[" "] * 3 for i in range(3)]

    def create_board(self):
        board = Texttable()
        for index in range(3):
            board.add_row(self.__data[index])
        return board.draw()
    # def __init__(self):
    #     self.__data = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
    #
    # def __str__(self):
    #     s = '+---+---+---+\n'
    #     for i in self.__data:
    #         s += '|'
    #         for j in i:
    #             if j == '0':
    #                 s += '   |'
    #             elif j == '1':
    #                 s += ' X |'
    #             elif j == '2':
    #                 s += ' O |'
    #         s += '\n'
    #         s += '+---+---+---+\n'
    #     return s

    def update_data(self, d):
        self.__data = d

    def get_data(self):
        return self.__data

    def move_x(self, row, col):
        if row > 2 or col > 2 or row < 0 or col < 0:
            raise ValueError("Invalid row/column values!")
        if self.__data[row][col] == ' ':
            self.__data[row][col] = 'X'
        else:
            raise ValueError("Square already occupied!")

    def move_o(self, row, col):
        if row > 2 or col > 2 or row < 0 or col < 0:
            raise ValueError("Invalid row/column values!")
        if self.__data[row][col] == ' ':
            self.__data[row][col] = 'O'
        else:
            raise ValueError("Square already occupied!")

    # def mov_x(self, row, col):
    #     if row > 2 or col > 2 or row < 0 or col < 0:
    #         raise ValueError("Invalid row/column values!")
    #     if self.__data[row][col] == '0':
    #         self.__data[row][col] = '1'
    #     else:
    #         raise ValueError("Square already occupied!")
    #
    # def mov_o(self, row, col):
    #     if row > 2 or col > 2 or row < 0 or col < 0:
    #         raise ValueError("Invalid row/column values!")
    #     if self.__data[row][col] == '0':
    #         self.__data[row][col] = '2'
    #     else:
    #         raise ValueError("Square already occupied!")

    def replace_x(self, row, col, row1, col1):
        """
        program moves x from square (row, col) to square (row1, col1)
        :param row:
        :param col:
        :param row1:
        :param col1:
        :return:
        """
        if self.__data[row][col] == "X" and self.__data[row1][col1] == ' ' and ((row == row1 or row == row1 - 1 or row == row1 +1) and (col == col1 or col == col1 - 1 or col == col1 + 1)):
            self.__data[row1][col1] = 'X'
            self.__data[row][col] = ' '
        else:
            raise ValueError("Invalid move!")

    def replace_o(self, row, col, row1, col1):
        """
        program moves O from square (row, col) to square (row1, col1)
        """
        if self.__data[row][col] == "O" and self.__data[row1][col1] == ' ':
            self.__data[row1][col1] = 'O'
            self.__data[row][col] = ' '
        else:
            raise ValueError("Invalid move!")

    def find_empty_and_replace(self):
        ok = 0
        for i in range(0,3):
            for j in range(0,3):
                if self.__data[i][j] == ' ':
                    self.__data[i][j] = 'O'
                    ok = 1
                if ok == 1:
                    ok = 2
                    break
            if ok == 2:
                break

    def find_o(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.__data[i][j] == 'O':
                    return i, j

    def find_empty(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.__data[i][j] == ' ':
                    return i, j

    def won_game(self):
        if self.__data[0] == ['X', 'X', 'X'] or self.__data[0] == ['O', 'O', 'O']:
            return True
        elif self.__data[1] == ['X', 'X', 'X'] or self.__data[0] == ['O', 'O', 'O']:
            return True
        elif self.__data[2] == ['X', 'X', 'X'] or self.__data[0] == ['O', 'O', 'O']:
            return True
        elif self.__data[0][0] == 'X' and self.__data[1][1] == 'X' and self.__data[2][2] == 'X':
            return True
        elif self.__data[0][0] == 'O' and self.__data[1][1] == 'O' and self.__data[2][2] == 'O':
            return True
        elif self.__data[0][2] == 'X' and self.__data[1][1] == 'X' and self.__data[2][0] == 'X':
            return True
        elif self.__data[0][2] == 'O' and self.__data[1][1] == 'O' and self.__data[2][0] == 'O':
            return True
        elif self.__data[0][0] == 'X' and self.__data[0][1] == 'X' and self.__data[0][2] == 'X':
            return True
        elif self.__data[0][0] == 'O' and self.__data[0][1] == 'O' and self.__data[0][2] == 'O':
            return True
        elif self.__data[1][0] == 'X' and self.__data[1][1] == 'X' and self.__data[1][2] == 'X':
            return True
        elif self.__data[1][0] == 'O' and self.__data[1][1] == 'O' and self.__data[1][2] == 'O':
            return True
        elif self.__data[2][0] == 'X' and self.__data[2][1] == 'X' and self.__data[2][2] == 'X':
            return True
        elif self.__data[2][0] == 'O' and self.__data[2][1] == 'O' and self.__data[2][2] == 'O':
            return True

    def dont_move(self):
        ok = 0
        for i in range(0,3):
            if self.__data[i] == ['X', 'X', ' ']:
                self.__data[i] = ['x', 'X', 'O']
                ok = 1
            elif self.__data[i] == [' ', 'X', 'X']:
                self.__data[i] = ['O', 'X', 'X']
                ok=1
            elif self.__data[i] == ['X', ' ', 'X']:
                self.__data[i] = ['X', 'O', 'X']
                ok = 1
        if ok == 0:
            if self.__data[0][0] == 'X' and self.__data[1][1] == 'X' and self.__data[2][2] == ' ':
                self.__data[2][2] = 'O'
                ok = 1
            elif self.__data[0][0] == 'X' and self.__data[1][1] == ' ' and self.__data[2][2] == 'X':
                self.__data[2][2] = 'O'
                ok = 1
            elif self.__data[0][0] == ' ' and self.__data[1][1] == 'X' and self.__data[2][2] == 'X':
                self.__data[2][2] = 'O'
                ok = 1
            elif self.__data[0][2] == 'X' and self.__data[1][1] == 'X' and self.__data[2][0] == ' ':
                self.__data[2][0] = 'O'
                ok = 1
            elif self.__data[0][2] == 'X' and self.__data[1][1] == ' ' and self.__data[2][0] == 'X':
                self.__data[1][1] = 'O'
                ok = 1
            elif self.__data[0][2] == ' ' and self.__data[1][1] == 'X' and self.__data[2][0] == 'X':
                self.__data[0][2] = 'O'
                ok = 1
            elif self.__data[0][0] == ' ' and self.__data[1][0] == 'X' and self.__data[2][0] == 'X':
                self.__data[0][0] = 'O'
                ok = 1
            elif self.__data[0][0] == 'X' and self.__data[1][0] == ' ' and self.__data[2][0] == 'X':
                self.__data[1][0] = '2'
                ok = 1
            elif self.__data[0][0] == 'X' and self.__data[1][0] == 'X' and self.__data[2][0] == ' ':
                self.__data[2][0] = 'O'
                ok = 1
            elif self.__data[0][1] == ' ' and self.__data[1][1] == 'X' and self.__data[2][1] == 'X':
                self.__data[0][1] = 'O'
                ok = 1
            elif self.__data[0][1] == 'X' and self.__data[1][1] == ' ' and self.__data[2][1] == 'X':
                self.__data[1][1] = 'O'
                ok = 1
            elif self.__data[0][1] == 'X' and self.__data[1][1] == 'X' and self.__data[2][1] == ' ':
                self.__data[2][1] = 'O'
                ok = 1
            elif self.__data[0][2] == 'X' and self.__data[1][2] == 'X' and self.__data[2][2] == ' ':
                self.__data[2][2] = 'O'
                ok = 1
            elif self.__data[0][2] == 'X' and self.__data[1][2] == 'X' and self.__data[2][2] == ' ':
                self.__data[0][2] = 'O'
                ok = 1
            elif self.__data[0][2] == 'X' and self.__data[1][2] == ' ' and self.__data[2][2] == 'X':
                self.__data[1][2] = 'O'
                ok = 1
            elif self.__data[0][2] == ' ' and self.__data[1][2] == 'X' and self.__data[2][2] == 'X':
                self.__data[0][2] = 'O'
                ok = 1
            if ok == 0:
                ok = 0
                for i in range(0, 3):
                    for j in range(0, 3):
                        if self.__data[i][j] == ' ':
                            self.__data[i][j] = 'O'
                            ok = 1
                        if ok == 1:
                            ok = 2
                            break
                    if ok == 2:
                        break

