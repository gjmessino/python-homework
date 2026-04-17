class TictactoeException(Exception):
    def __innit__(self, message):
        self.message = message
        super.__innit__()

class Board():
    def __innit__(self):
        self.board_array = [[" "," ", " "][" "," ", " "][" "," ", " "]]
        self.turn = "X"
    valid_moves = ["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]
    def __str__(self):
        for item in self.board_array:
            item = str(item + "\n")
        print(self.board)
    def move(self, move_string):
        if move_string not in valid_moves:
            raise TictactoeException ("That's not a valid move.")
        elif self.board_array[valid_moves.index(move_string)] != " " :
            raise TictactoeException ("That spot is taken.")
        else:
            if self.turn == "X":
                self.board_array[#index tbd] = "X"
            else:
                self.board_array[#index tbd] = "Y"
