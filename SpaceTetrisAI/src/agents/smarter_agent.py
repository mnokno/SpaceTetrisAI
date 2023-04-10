from src.agents.agent import Agent


class SmarterAgent(Agent):

    def score(self, board: list[int], left_piece: list[int], objective_score: int, multiplier: int) -> int:
        """
        Scores the given board based on the board itself, other piece and multiple

        :param board: Board state in a flat vector
        :param left_piece: Piece left in  a flat vector
        :param objective_score: Current game score
        :param multiplier: Multiplier
        :return: Score for this position
        """
        return objective_score + SmarterAgent.__score(board)

    @staticmethod
    def __score(board: list[int]) -> int:
        """
        Scores the given position

        :param board: Vectorized board
        :return: Score
        """
        cell_dif = [0 for _ in range(len(board))]

        # Adds boarder diff
        for i in range(5):
            cell_dif[i] += 1
            cell_dif[20 + i] += 1
            cell_dif[i * 5] += 1
            cell_dif[i * 5 + 4] += 1

        # Add neighbour diff
        offsets = [1, -1, 5, -5]
        for i in range(len(board)):
            if board[i] == 1:
                for o in offsets:
                    if SmarterAgent.__is_connection_valid(i, i + o):
                        cell_dif[i + o] += 1

        # Increases score if for filled cells
        for i in range(len(board)):
            if board[i] == 1:
                cell_dif[i] = -cell_dif[i]

        # Sums score
        score = 0
        for i in range(len(board)):
            score += cell_dif[i]

        return int(-score / 1.75)

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
