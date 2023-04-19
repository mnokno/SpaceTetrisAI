import types
from src.environment.game import Game
from src.environment.piece import Piece
from src.agents.agent import Agent


def score_agent(agent: Agent, game: Game, max_steps: int = 500, deep_score: bool = False) -> int:
    """
    Makes the give agent play out the given game and return agents score for that game

    :param agent: Agent to test
    :param game: Game that the agent will play
    :param max_steps: Maximum number of block that the agent can play before game is terminated
    :param deep_score: Decides water or not deep evaluation will be used (much better result but much slower)
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

        bets_play_main = score_current_piece(agent, game, True, shallow=(not deep_score))
        game.swap_pieces()
        bets_play_alt = score_current_piece(agent, game, False, shallow=(not deep_score))
        game.swap_pieces()
        if bets_play_alt.score > bets_play_main.score:
            bets_play = bets_play_alt
        else:
            bets_play = bets_play_main

        if bets_play.x == -1:
            game.cant_play()
        else:
            if not bets_play.main_piece:
                game.swap_pieces()
            while game.get_main_piece()[1] != bets_play.rotation:
                game.rotate_piece()
            game.place_piece(bets_play.x, bets_play.y)

    return game.get_score()


def score_current_piece(agent: Agent, game: Game, mian: bool, shallow: bool = True, expose_piece: bool = True) -> types.SimpleNamespace:
    """
    Score the position by checking the current piece if shallow, will score the position by trying the fit the current
    piece first than the alternative piece

    @param agent: Agent to make the decision
    @param game: Game which the agent will play
    @param mian: Weather or not the current piece is the main piece
    @param shallow: Weather or not to perform deep or shallow evaluation, shallow evaluation is more prone to horizon
    effect however It's much faster than deep evaluation
    @param expose_piece: Weather or not the alternative piece is exposed to the agent
    @return: Score for the position
    """
    bets_play = types.SimpleNamespace()
    bets_play.score = -99999
    bets_play.x = -1
    bets_play.y = -1
    bets_play.rotation = 0
    bets_play.main_piece = mian

    for r in range(4):
        piece = Piece.get_piece_bitmask(game.get_main_piece()[0], game.get_main_piece()[1])
        for x in range(5):
            for y in range(5):
                if game.get_board().can_play_piece(piece, x, y):
                    game.place_piece(x, y)

                    score = 0
                    if shallow:
                        if expose_piece:
                            score = agent.score(
                                game.get_board().get_flat_board_vector(),
                                Piece.get_flat_piece_vector(game.get_alt_piece()[0], game.get_alt_piece()[1]),
                                game.get_score(),
                                game.get_multiplayer()
                            )
                        else:
                            score = agent.score(
                                game.get_board().get_flat_board_vector(),
                                Piece.get_empty_flat_piece_vector(),
                                game.get_score(),
                                game.get_multiplayer()
                            )

                    if not shallow:
                        deep_score = score_current_piece(agent, game, mian, shallow=True, expose_piece=False)
                        if deep_score.x == -1:
                            score = agent.score(
                                game.get_board().get_flat_board_vector(),
                                Piece.get_flat_piece_vector(game.get_alt_piece()[0], game.get_alt_piece()[1]),
                                game.get_score(),
                                game.get_multiplayer()
                            ) + deep_score.score
                        else:
                            score = deep_score.score

                    game.backtrack()
                    if score > bets_play.score:
                        bets_play.score = score
                        bets_play.x = x
                        bets_play.y = y
                        bets_play.rotation = game.get_main_piece()[1]
        game.rotate_piece()

    return bets_play
