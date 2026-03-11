"""
WAR Card Game Simulation
An automated simulation of the classic card game 'War', demonstrating 
complex loop structures and object-oriented deck management.
"""

import random

# Constants
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        """Removes and returns the top card from the player's deck."""
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        """Adds won cards (single or list) to the bottom of the deck."""
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

def run_war_simulation():
    # Setup
    deck = Deck()
    deck.shuffle()
    p1 = Player("P1")
    p2 = Player("P2")

    # Initial Deal
    for i in range(26):
        p1.add_cards(deck.deal_one())
        p2.add_cards(deck.deal_one())

    game_on = True
    round_count = 0

    while game_on:
        # Check if anyone is out of cards
        if len(p1.all_cards) == 0:
            print(f"Player {p2.name} Wins! {p1.name} is out of cards.")
            break
        if len(p2.all_cards) == 0:
            print(f"Player {p1.name} Wins! {p2.name} is out of cards.")
            break

        round_count += 1
        p1_table = [p1.remove_one()]
        p2_table = [p2.remove_one()]

        # Comparison Logic
        at_war = True
        while at_war:
            if p1_table[-1].value > p2_table[-1].value:
                p1.add_cards(p1_table + p2_table)
                at_war = False
            elif p2_table[-1].value > p1_table[-1].value:
                p2.add_cards(p1_table + p2_table)
                at_war = False
            else:
                # War Tie Logic
                if len(p1.all_cards) < 5:
                    print(f"P1 has insufficient cards for War! {p2.name} wins.")
                    game_on = False
                    break
                elif len(p2.all_cards) < 5:
                    print(f"P2 has insufficient cards for War! {p1.name} wins.")
                    game_on = False
                    break
                else:
                    # Draw 5 cards for the 'sacrifice'
                    for _ in range(5):
                        p1_table.append(p1.remove_one())
                        p2_table.append(p2.remove_one())

    print(f"Game ended after {round_count} rounds.")

if __name__ == "__main__":
    run_war_simulation()
