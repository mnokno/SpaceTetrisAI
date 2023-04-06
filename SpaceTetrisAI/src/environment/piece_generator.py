from random import randint


class PieceGenerator:
    """
    Piece generator can be used to generate random pieces and ensures that upcoming
    pieces do not change after backtracking
    """

    __history: [(int, int)] = []
    """
    Stores previously generated pieces
    """

    def get_piece(self, time_stamp: int) -> (int, int):
        """
        Returns a new piece mask repointing to the given time_stamp

        :param time_stamp: How many piece where played in the game
        :return: return new piece maks
        """

        while not time_stamp < len(self.__history):
            self.__history.append((randint(0, 14), randint(0, 3)))

        if time_stamp < len(self.__history):
            return self.__history[time_stamp]
