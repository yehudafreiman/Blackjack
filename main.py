from core import deck
from core import game_logic
from core import player_io



if __name__=="__main__":

    deck.build_standard_deck()
    deck.shuffle_by_suit(deck=deck.build_standard_deck(), swaps=5000)

    player = {"hand": []}
    dealer = {"hand": []}

    print(game_logic.run_full_game(deck.shuffle_by_suit(deck=deck.build_standard_deck(), swaps=5000), player, dealer))


