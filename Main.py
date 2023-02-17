from Controller.controller import Controller
from Domain.entities import Board
from UI.ui import UI

board = Board()
controller = Controller(board)
ui = UI(controller)

ui.start()