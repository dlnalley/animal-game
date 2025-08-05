class Piece:
    """
    Super class for each game piece.
    """
    def __init__(self, color):
        """
        Self defined, with color parameter for the players.
        :param color:
        """
        self._color = color

    def can_move(self, start, end, board):
        """
        Default function for the super class so that each piece inheriting can
        implement the method themselves.
        :param start:
        :param end:
        :param board:
        :return:
        """
        raise NotImplementedError("Subclasses must implement this method.")


class Chinchilla(Piece):
    """
    Chinchilla piece class.
    """
    def can_move(self, start, end, board):
        """
        Function to set where the piece can move and how it moves.
        :param start:
        :param end:
        :param board:
        :return:
        """
        start_col, start_row = start
        end_col, end_row = end
        return abs(start_col - end_col) == 1 and abs(start_row - end_row) == 1


class Wombat(Piece):
    """
    Wombat game piece.
    """
    def can_move(self, start, end, board):
        """
        Function to set where the piece can move and how it moves.
        :param start:
        :param end:
        :param board:
        :return:
        """
        start_col, start_row = start
        end_col, end_row = end
        return (abs(start_col - end_col) == 4 and start_row == end_row) or \
            (abs(start_row - end_row) == 4 and start_col == end_col)


class Emu(Piece):
    """
    Emu game piece.
    """
    def can_move(self, start, end, board):
        """
        Function to set where the piece can move and how it moves.
        :param start:
        :param end:
        :param board:
        :return:
        """
        start_col, start_row = start
        end_col, end_row = end
        return (abs(start_col - end_col) <= 3 and start_row == end_row) or \
            (abs(start_row - end_row) <= 3 and start_col == end_col)


class Cuttlefish(Piece):
    """
    Cuttlefish game piece.
    """
    def can_move(self, start, end, board):
        """
        Function to set where the piece can move and how it moves.
        :param start:
        :param end:
        :param board:
        :return:
        """
        start_col, start_row = start
        end_col, end_row = end
        return abs(start_col - end_col) == 2 and abs(start_row - end_row) == 2


class AnimalGame:
    """
    Class to implement the Animal Game.
    """
    def __init__(self):
        """
        Takes no arguments and sets parameters for the board, starting turn, and game state.
        """
        self._board = self._create_board(0, [])
        self._turn = "TANGERINE"
        self._game_state = "UNFINISHED"
        self._initialize_board(0)

    def _create_board(self, row, board):
        """
        Function to create the game board.
        :param row:
        :param board:
        :return:
        """
        if row == 7:
            return board
        return self._create_board(row + 1, board + [[None] * 7])

    def _initialize_board(self, index):
        """
        Function to set pieces on the game board.
        :param index:
        :return:
        """
        piece_order = [Chinchilla, Wombat, Emu, Cuttlefish, Emu, Wombat, Chinchilla]
        if index == 7:
            return
        self._board[0][index] = piece_order[index]("TANGERINE")
        self._board[6][index] = piece_order[index]("AMETHYST")
        self._initialize_board(index + 1)

    def get_game_state(self):
        """
        Function to call for the current game state.
        :return:
        """
        return self._game_state

    def make_move(self, start, end):
        """
        Function to make a move on each player's respective turn.
        :param start:
        :param end:
        :return:
        """
        start_col, start_row = ord(start[0]) - ord('a'), int(start[1]) - 1
        end_col, end_row = ord(end[0]) - ord('a'), int(end[1]) - 1

        if self._game_state != "UNFINISHED":
            return False

        piece = self._board[start_row][start_col]

        if not piece or (self._turn == "TANGERINE" and piece._color != "TANGERINE") or \
                (self._turn == "AMETHYST" and piece._color != "AMETHYST"):
            return False

        if not piece.can_move((start_col, start_row), (end_col, end_row), self._board):
            return False

        target_piece = self._board[end_row][end_col]
        if isinstance(target_piece, Cuttlefish):
            self._game_state = "TANGERINE_WON" if target_piece._color == "AMETHYST" else "AMETHYST_WON"

        self._board[end_row][end_col] = piece
        self._board[start_row][start_col] = None
        self._turn = "AMETHYST" if self._turn == "TANGERINE" else "TANGERINE"

        return True