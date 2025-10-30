from core import deck
from core import game_logic



if __name__=="__main__":

    print(deck.build_standard_deck())
    print(deck.shuffle_by_suit(deck=deck.build_standard_deck(), swaps=5000))

    player = {"hand": []}
    dealer = {"hand": []}

    print(game_logic.run_full_game(deck.build_standard_deck(), player, dealer))


