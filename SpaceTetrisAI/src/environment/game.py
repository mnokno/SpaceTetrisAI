from src.environment.piece import Piece
from src.environment.board import Board
from src.environment.piece_generator import PieceGenerator


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

    __pieceGenerator: PieceGenerator
    """
    Stores piece generator object used for piece generation
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

    __multiplier: int
    """
    Stores multiplier
    """

    def __init__(self):
        """
        Creates new fresh board
        """
        self.__pieceGenerator = PieceGenerator()
        self.__board = Board()
        self.__piece_main = self.__pieceGenerator.get_piece(len(self.__historicData))
        self.__piece_alt = self.__pieceGenerator.get_piece(len(self.__historicData) + 1)
        self.__lives = 3
        self.__score = 0
        self.__multiplier = 1

    def place_piece(self, x: int, y: int) -> None:
        """
        Plays the mian piece at specified x, y. Will cause an exception if the play is illegal.

        :param x: X position, has to be between 0 and 4
        :param y: Y position, has to be between 0 and 4
        """

        if not self.__board.can_play_piece(self.__piece_main, x, y):
            raise Exception("Illegal piece play attempted!")

        self.__historicData.append((
            self.__board.get_board(),
            self.__piece_main,
            self.__piece_alt,
            self.__lives,
            self.__score,
            self.__multiplier
        ))

        self.__board.play_piece(self.__piece_main, x, y)
        cleared_blocks, cleared_lines = self.__board.clear_lines()

        self.__piece_main = self.__piece_alt
        self.__piece_alt = self.__pieceGenerator.get_piece(len(self.__historicData) + 1)

        if cleared_blocks == 0:
            self.__multiplier = 1
        else:
            self.__score += cleared_lines * cleared_blocks * 10 * self.__multiplier
            self.__multiplier += 1

    def swap_pieces(self) -> None:
        """
        Swaps the main piece with alternative piece
        """
        self.__piece_main, self.__piece_alt = self.__piece_alt, self.__piece_main

    def backtrack(self) -> None:
        """
        Goes back in history one step
        """
        board, self.__piece_main, self.__piece_alt, self.__lives, self.__score, self.__multiplier \
            = self.__historicData.pop()
        self.__board.set_board(board)

    def get_board(self) -> Board:
        """
        Getter for board
        :return: board
        """
        return self.__board

    def get_main_piece(self) -> int:
        """
        Getter for main piece
        :return: main piece
        """
        return self.__piece_main

    def get_alt_piece(self) -> int:
        """
        Getter for alternative piece
        :return: alternative piece
        """
        return self.__piece_alt

    def get_lives(self) -> int:
        """
        Getter for lives
        :return: lives
        """
        return self.__lives

    def get_score(self) -> int:
        """
        Getter for score
        :return: score
        """
        return self.__score

    def get_multiplayer(self) -> int:
        """
        Getter for multiplier
        :return: multiplier
        """
        return self.__multiplier
