class Controller:
    def __init__(self, repo):
        self.__repo = repo

    def move_x(self, i, j):
        """moves x to a squere"""
        self.__repo.move_x(i, j)

    def move_o(self, i, j):
        """moves o to a squere"""
        self.__repo.move_o(i, j)

    def print_board(self):
        return self.__repo.create_board()

    def find_empty(self):
        self.__repo.find_empty_and_replace()

    def replace_x(self, row, col, row1, col1):
        try:
            self.__repo.replace_x(row, col, row1, col1)
        except ValueError as ve:
            raise ValueError(ve)

    def move_o_from_square_to_another(self):
        row, col = self.__repo.find_o()
        row1, col1 = self.__repo.find_empty()
        self.__repo.replace_o(row, col, row1, col1)

    def won_game(self):
        return self.__repo.won_game()

    def get_data_board(self):
        return self.__repo.get_data()

    def dont_move(self):
        self.__repo.dont_move()