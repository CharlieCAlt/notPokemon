from game_engine.game import Game

class TestBattles:

    @staticmethod
    def test_choose_attacker():
        game = Game()
        game.choose_attacker()
        assert game.attacker == game.player_1 or game.attacker == game.player_2

    @staticmethod
    def test_attack():
        game = Game()
        game.choose_attacker()
        attacking_player = game.attacker
        result = game.attack()
        attacking_player_after = game.attacker
        if result == 'win':
            assert attacking_player == attacking_player_after
        else:
            assert attacking_player != attacking_player_after


    @staticmethod
    def test_out_of_cards():
        game = Game()
        game.choose_attacker()
        while not game.finished:
            result = game.attack()
            winner = game.finish()
        assert game.finished
