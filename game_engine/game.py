from deck import Deck
from game_engine.player import Player
import numpy as np
from database import Database
import pokemon_download
import requests



class Game:

    def __init__(self):
        database = Database()
        database.delete_table()
        database.createTables()
        pokemon_download.getPokemon(database)
        self.deck = Deck()
        deck_a, deck_b = self.deck.shuffle()
        self.player_1 = Player(1)
        self.player_2 = Player(2)
        self.player_1.deck = deck_a
        self.player_2.deck = deck_b
        self.counter_1 = self.player_1.counter
        self.counter_2 = self.player_2.counter
        self.attacker = None
        self.defender = None
        self.finished = False

    def choose_attacker(self):
        number = np.random.randint(1,3)
        if number == 1:
            self.attacker = self.player_1
            self.defender = self.player_2
        if number == 2:
            self.attacker = self.player_2
            self.defender = self.player_1

    def attack(self):
        attacker = self.attacker
        defender = self.defender
        deck = self.deck
        attack = deck.get_attack(attacker.deck, deck.counter)[0]
        defense = deck.get_defense(defender.deck, deck.counter)[0]
        # Need the player to choose a type for attacker
        type_attacker, type_attacker1 = self.get_types(self.attacker)
        type_defender, type_defender1 = self.get_types(self.defender)
        damage_modifier = self.damageModifier(type_attacker, type_defender, type_defender1)
        attack *= damage_modifier
        if attack > defense:
            result = 'won'
            attacker.deck.append(defender.deck[deck.counter])
            del defender.deck[deck.counter]
            # Might need to have two different counters for each player as when card is deleted counter needs to stay the same
        else:
            result = 'lost'
            defender.deck.append(attacker.deck[deck.counter])
            del attacker.deck[deck.counter]
            self.attacker = defender
            self.defender = attacker
        return result

    def get_types(self, player):
        types = self.deck.get_types(player.deck, self.deck.counter)
        return types[0], types[1]


    def finish(self):
        winner = None
        if len(self.player_1.deck) == 0:
            winner = self.player_2
            self.finished = True
        if len(self.player_2.deck) == 0:
            winner = self.player_1
            self.finished = True
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



