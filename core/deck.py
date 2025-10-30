import random

def build_standard_deck() -> list[dict]:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suites = ['H', 'C', 'D', 'S']
    deck = []
    for rank in ranks:
        for suite in suites:
            deck.append({'rank':rank,'suite':suite})
    return deck

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for i in range(1, swaps + 1):
        index_i = random.randrange(0, len(build_standard_deck()) - 1)
        index_j = random.randrange(0, len(build_standard_deck()) - 1)
        if index_i != index_j:
            deck[index_i], deck[index_j] = deck[index_j], deck[index_i]
        else:
            continue
    return deck

