

class Board:
    def __init__(self):
        self._board = [[0] * 8 for _ in range(8)]
        for x in range(1, 9, 2):
            self._board[1][x] = 6
            self._board[5][x] = 9
            self._board[7][x] = 9

        for x in range(0, 8, 2):
            self._board[0][x] = 6
            self._board[2][x] = 6
            self._board[6][x] = 9

    def __str__(self):
        strin = ""
        for y in range(8):
            for x in range(8):
                strin += " " + str(self._board[y][x])
            strin += "\n"
        return strin

if __name__ == "__main__":
    b = Board()
    print(b)