from deck import Deck


class TestDeck:

    @staticmethod
    def test_check_deck_exists():
        deck = Deck()

        assert len(deck.full_deck) == 151

    @staticmethod
    def test_check_deck_split_evenly():
        deck = Deck()
        deck_a, deck_b = deck.shuffle()

        assert len(deck_a) == 75 or len(deck_a) == 76
