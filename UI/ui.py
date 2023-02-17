class UI:
    def __init__(self, controller):
        self.__controller = controller

    def start(self):
        nr = 0
        while True:
            ok = 0
            print(self.__controller.print_board())
            if nr < 4:
                print("Choose a square to place: ")
                row = int(input("Enter the row: "))
                col = int(input("Enter the column: "))
                try:
                    self.__controller.move_x(row, col)
                    print(self.__controller.print_board())
                    nr  = nr + 1
                    ok = 1
                    if self.__controller.won_game() is True:
                        print("You won! :)")
                        break
                except ValueError as ve:
                    print(ve)
                if ok == 1 and nr == 1:
                    self.__controller.find_empty()
                    if self.__controller.won_game() is True:
                        print("You lost! :(")
                        break
                elif ok == 1 and nr > 1:
                    try:
                        self.__controller.dont_move()
                        if self.__controller.won_game() is True:
                            print("You lost! :(")
                            print(self.__controller.print_board())
                            break
                    except ValueError:
                        self.__controller.find_empty()
            if nr == 4:
                print("Choose a square to move from: ")
                valid = 0
                while valid == 0:
                    row = int(input("Enter the row: "))
                    col = int(input("Enter the column: "))
                    if row < 3 and col < 3 and row >= 0 and col >= 0:
                        valid = 1
                    else:
                        print("Invalid input!")
                print("Choose a square where to be moved : ")
                valid = 0
                while valid == 0:
                    row1 = int(input("Enter the row: "))
                    col1 = int(input("Enter the column: "))
                    if row1 < 3 and col1 < 3 and row1 >= 0 and col1 >= 0:
                        valid = 1
                    else:
                        print("Invalid input!")
                try:
                    self.__controller.replace_x(row, col, row1, col1)
                    print(self.__controller.print_board())
                    if self.__controller.won_game() is True:
                        print("You won! :)")
                        break
                    ok = 1
                except ValueError as ve:
                    print(ve)
                if ok == 1:
                    self.__controller.move_o_from_square_to_another()
                    if self.__controller.won_game() is True:
                        print("You lost! :(")
                        print(self.__controller.print_board())
                        break
                    ok = 0

