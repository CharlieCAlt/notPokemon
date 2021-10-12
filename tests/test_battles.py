from game_engine.game import Game

class TestBattles:

    @staticmethod
    def test_choose_attacker():
        game = Game()
        assert game.attacker == game.player_1 or game.attacker == game.player_2

    @staticmethod
    def test_attack():
        game = Game()
        attacking_player = game.attacker
        winner = game.attack()
        attacking_player_after = game.attacker
        if winner == attacking_player:
            assert attacking_player == attacking_player_after
        else:
            assert attacking_player != attacking_player_after


    @staticmethod
    def test_out_of_cards():
        game = Game()
        while not game.finished:
            winner = game.attack()
        if len(game.player_1.deck) == 0 or len(game.player_2.deck) == 0:
            assert game.finished
        else:
            assert not game.finished
