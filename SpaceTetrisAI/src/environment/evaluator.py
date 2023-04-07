import types
from src.environment.game import Game
from src.environment.piece import Piece
from src.agents.agent import Agent


def score_agent(agent: Agent, game: Game, max_steps: int = 500) -> int:
    """
    Makes the give agent play out the given game and return agents score for that game

    :param agent: Agent to test
    :param game: Game that the agent will play
    :param max_steps: Maximum number of block that the agent can play before game is terminated
    :return: Score the agent achieved in that game
    """

    for i in range(max_steps):
        if game.get_lives() < 0:
            break

        bets_play = types.SimpleNamespace()
        bets_play.score = -99999
        bets_play.x = -1
        bets_play.y = -1
        bets_play.rotation = 0
        bets_play.main_piece = True

        for r in range(4):
            piece = Piece.get_piece_bitmask(game.get_main_piece()[0], game.get_main_piece()[1])
            for x in range(5):
                for y in range(5):
                    if game.get_board().can_play_piece(piece, x, y):
                        game.place_piece(x, y)
                        score = agent.score(
                            game.get_board().get_flat_board_vector(),
                            Piece.get_flat_piece_vector(game.get_alt_piece()[0], game.get_alt_piece()[1]),
                            game.get_score(),
                            game.get_multiplayer()
                        )
                        game.backtrack()
                        if score > bets_play.score:
                            bets_play.score = score
                            bets_play.x = x
                            bets_play.y = y
                            bets_play.rotation = game.get_main_piece()[1]
                            bets_play.main_piece = True
            game.rotate_piece()

        game.swap_pieces()

        for r in range(4):
            piece = Piece.get_piece_bitmask(game.get_main_piece()[0], game.get_main_piece()[1])
            for x in range(5):
                for y in range(5):
                    if game.get_board().can_play_piece(piece, x, y):
                        game.place_piece(x, y)
                        score = agent.score(
                            game.get_board().get_flat_board_vector(),
                            Piece.get_flat_piece_vector(game.get_alt_piece()[0], game.get_alt_piece()[1]),
                            game.get_score(),
                            game.get_multiplayer()
                        )
                        game.backtrack()
                        if score > bets_play.score:
                            bets_play.score = score
                            bets_play.x = x
                            bets_play.y = y
                            bets_play.rotation = game.get_main_piece()[1]
                            bets_play.main_piece = False
            game.rotate_piece()

        game.swap_pieces()

        if bets_play.x == -1:
            game.cant_play()
        else:
            if not bets_play.main_piece:
                game.swap_pieces()
            while game.get_main_piece()[1] != bets_play.rotation:
                game.rotate_piece()
            game.place_piece(bets_play.x, bets_play.y)

    return game.get_score()
