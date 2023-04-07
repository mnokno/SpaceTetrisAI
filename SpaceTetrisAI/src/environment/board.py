from src.environment.precalculated_data import PrecalculatedData


class Board:
    """
    Board class is an efficient implementation of a space tetris game board storing. Stores current board state and
    provides utilities to interact with it.
    """

    __board: int
    """
    Bitboard representing current board state
    """

    def __init__(self):
        """
        Create a new empty board
        """
        self.__board = ~PrecalculatedData.boardBitmask

    def can_play_piece(self, piece_mask: int, x: int, y: int) -> bool:
        """
        Checks if the given piece can be played at given place (x, y)

        :param piece_mask: Bitboard mask representation of the piece to check
        :param x: X/Column of piece center
        :param y: Y/Row of piece center
        :return: Return True if the piece can be place in specified position, False otherwise
        """
        return (self.__board & (piece_mask << (x + y*7))) == 0

    def play_piece(self, piece_mask: int, x: int, y: int) -> None:
        """
        Play given piece at given place (x, y) without checking if it's allowed, call can_play_piece to check it
        the piece can be played without any collisions.

        :param piece_mask: Bitboard mask representation of the piece to play
        :param x: X/Column of piece center
        :param y: Y/Row of piece center
        """
        self.__board |= (piece_mask << (x + y*7))

    def clear_lines(self) -> (int, int):
        """
        Clears all vertical and horizontal lines

        :return: Returns number of blocks cleared, Number of lines cleared
        """

        rows_to_clear = []
        columns_to_clear = []

        for i in range(5):
            if (self.__board & PrecalculatedData.rowBitmasks[i]) == PrecalculatedData.rowBitmasks[i]:
                rows_to_clear.append(i)
            if (self.__board & PrecalculatedData.columnBitmasks[i]) == PrecalculatedData.columnBitmasks[i]:
                columns_to_clear.append(i)

        for i in rows_to_clear:
            self.__board &= ~PrecalculatedData.rowBitmasks[i]
        for i in columns_to_clear:
            self.__board &= ~PrecalculatedData.columnBitmasks[i]

        return ((len(rows_to_clear) + len(columns_to_clear)) * 5 - len(rows_to_clear) * len(columns_to_clear),
                (len(rows_to_clear) + len(columns_to_clear)))

    def get_board(self) -> int:
        """
        Getter for bitboard representation of the internal board

        :return: Bitboard representation of the internal board
        """
        return self.__board

    def get_flat_board_vector(self) -> [int]:
        """
        Gets this board in a flat vector from
        :return: Flat vector from this board
        """
        flat_vector = []
        for x in range(5):
            for y in range(5):
                if self.__board & (1 << ((x + 1) + (y + 1) * 7)) == 0:
                    flat_vector.append(0)
                else:
                    flat_vector.append(1)
        return flat_vector

    def set_board(self, board: int) -> None:
        """
        Setter for bitboard representation of the internal board

        :param board: New bitboard to set as the internal board state
        """
        self.__board = board
