from src.environment.piece import Piece
from src.environment.board import Board


class Game:
    """
    Implementation of a game environment that can be used to train agents,
    provides implementation for scoring and efficient backtracking.
    """

    __historicData: [(int, int, int, int, int, int)] = []
    """
    Stores historic data required to backtrack in a stack in the following order
    (board_bitboard, piece_main, piece_alt, lives, score, multiplayer)
    """

    __board: Board
    """
    Stores board
    """

    __piece_main: int
    """
    Stores maks for the main piece
    """

    __piece_alt: int
    """
    Stores mask for the alternative piece
    """

    __lives: int
    """
    Stores number of lives
    """

    __score: int
    """
    Stores score
    """

    __multiplayer: int
    """
    Stores multiplayer
    """

    def __init__(self):
        """
        Creates new fresh board
        """
        self.__board = Board()
        #TODO self.__piece_main =
        #TODO self.__piece_alt =
        self.__lives = 3
        self.__score = 0
        self.__multiplayer = 1
