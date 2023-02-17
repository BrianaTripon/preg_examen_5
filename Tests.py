from Controller.controller import Controller
from Domain.entities import Board


def tests():
    board = Board()
    controller = Controller(board)
    controller.move_x(1, 1)
    assert board.get_data() == [[' ', ' ', ' '], [' ', 'X', ' '], [' ', ' ', ' ']]
    controller.move_o(2, 2)
    assert board.get_data() == [[' ', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'O']]
    controller.replace_x(1, 1, 0, 0)
    assert board.get_data() == [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', 'O']]
    
