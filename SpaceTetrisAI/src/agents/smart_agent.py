from src.agents.agent import Agent


class SmartAgent(Agent):

    def score(self, board: list[int], left_piece: list[int], objective_score: int, multiplier: int) -> int:
        """
        Scores the given board based on the board itself, other piece and multiple

        :param board: Board state in a flat vector
        :param left_piece: Piece left in  a flat vector
        :param objective_score: Current game score
        :param multiplier: Multiplier
        :return: Score for this position
        """
        return objective_score - SmartAgent.__get_number_of_neighbouring_empty_blocks(board)

    @staticmethod
    def __get_number_of_neighbouring_empty_blocks(board: list[int]) -> int:
        """
        Gets the number of neighbouring empty blocks

        :param board: Vectorized board
        :return: Number of empty neighbouring blocks origin
        """
        count = 0
        offsets = [1, -1, 5, -5, 6, -6, 4, -4]
        for i in range(25):
            if board[i] == 1:
                for offset in offsets:
                    if SmartAgent.__is_connection_valid(i, i + offset):
                        if board[i + offset] == 0:
                            count += 1
        return count

    @staticmethod
    def __is_connection_valid(origin: int, to: int) -> bool:
        """
        Checks if the given connection is valid. The connection can be invalid because it is outside the board,
        or it had wrapped around an edge of the board, both mean that the connection is not to a neighbouring block.

        :param origin: From block
        :param to: To block
        :return: True if the connection is valid, False otherwise
        """
        # above or below the board
        if to < 0 or to > 24:
            return False
        # wrapped around an edge
        if origin % 5 == 0 and ((origin - to == 6) or (origin - to == -4)):
            return False
        if origin % 4 == 0 and ((origin - to == 4) or (origin - to == -6)):
            return False

        return True
