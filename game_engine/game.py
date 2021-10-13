from deck import Deck
from game_engine.player import Player
import requests


class Game:

    def __init__(self):
        self.deck = Deck()
        deck_a, deck_b = self.deck.shuffle()
        self.player_1 = Player()
        self.player_2 = Player()
        self.player_1.deck = deck_a
        self.player_2.deck = deck_b
        self.attacker = None
        self.defender = None
        self.finished = False

    def choose_attacker(self):
        pass

    def attack(self):
        attack = self.deck.get_attack(self.attacker.deck, self.deck.counter)
        winner = self.attacker
        return winner

    def damageModifier(self, attackerType, defenseType1, defenseType2):
        url = self.typeURL(attackerType)
        defenseType = [defenseType1, defenseType2]
        modifier = self.calculateModifier(url, defenseType)
        modifier /= 10
        return modifier

    def typeURL(self, attackerType):
        typeUrl = None
        r = requests.get("https://pokeapi.co/api/v2/type/")
        response = r.json()
        results = response["results"]
        for type in results:
            typeName = type["name"]
            if typeName == attackerType:
                typeUrl = type["url"]
        return typeUrl

    def calculateModifier(self, typeUrl, defenseType):
        dmgModifier = int(10)
        r = requests.get(typeUrl)
        response = r.json()
        results = response["damage_relations"]
        doubleDamage = results["double_damage_to"]
        halfDamage = results["half_damage_to"]
        noDamage = results["no_damage_to"]
        for dType in defenseType:
            for typeName in doubleDamage:
                if dType in typeName.values():
                    dmgModifier *= 2
            for typeName in halfDamage:
                if dType in typeName.values():
                    dmgModifier *= 0.5
            for typeName in noDamage:
                if dType in typeName.values():
                    dmgModifier *= 0
        return dmgModifier


