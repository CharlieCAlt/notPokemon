from game_engine.game import Game

class TestBattles:

    @staticmethod
    def test_choose_attacker():
        game = Game()
        assert game.attacker == game.player_1 or game.attacker == game.player_2

    @staticmethod
    def test_attacker_wins():
        # game = Game()
        # if attacker.attack > defender.defend:
        #    assert attacker.win == True
        # else:
        #    assert attacker.win == False
        pass
