from deck import Deck


class TestDeck:

    @staticmethod
    def test_check_deck_exists():
        deck = Deck()

        assert len(deck.full_deck) == 151
