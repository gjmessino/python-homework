class TictactoeException(Exception):
    def __innit__(self, message):
        self.message = message
        super.__innit__()

class Board():
    valid_moves = ["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]
    def __innit__(self):
        self.board_array = [[" "," ", " "][" "," ", " "][" "," ", " "]]
        self.turn = "X"
    def __str__(self):
        for item in self.board_array:
            item = str(item + "\n")
        print(self.board)
    def move(self, move_string):
        def find_index(move_str):
            if "left" in move_str:
                first_ind = 0
            if "center" in move_str:
                first_ind = 1
            else:
                first_ind = 2
            if "upper" in move_str:
                second_ind = 0
            elif "middle" in move_str:
                second_ind = 1
            else:
                second_ind = 2
            return [first_ind, second_ind]
        move_index = find_index(move_string)
        if move_string not in valid_moves:
            raise TictactoeException ("That's not a valid move.")
        elif self.board_array[move_index] != " " :
            raise TictactoeException ("That spot is taken.")
        else:
            if self.turn == "X":
                self.board_array[move_index] = "X"
                self.turn = "O"
            else:
                self.board_array[move_index] = "O"
                self.turn = "X"
    def whats_next(self):
        def check_rows(xo):
            for row in self.board_array:
                if row[0] == xo and row[1] == xo and row[2] == xo:
                    return True
        def check_columns(xo):

        def check_diagonal(xo):
            for i in range(3):
                if self.board_array[i][i] == xo or self.board_array[-i][i] ==xo:
                    return True
