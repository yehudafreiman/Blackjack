from core import player_io
from core import deck


def calculate_hand_value(hand: list[dict]) -> int:
    result = 0
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6':6 , '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}
    for card in hand:
        for k, v in values.items():
            if k == card["rank"]:
                result += v
    return result

def deal_two_each(deck :list[dict], player: dict, dealer: dict) -> None:
    player["hand"].append(deck.pop())
    dealer["hand"].append(deck.pop())

    player_hand_value = calculate_hand_value(player["hand"])
    dealer_hand_value = calculate_hand_value(dealer["hand"])

    print(f"player hand value: {player_hand_value}, dealer hand value: {dealer_hand_value}")
    return None

print(deal_two_each(deck.build_standard_deck(), player = {"hand": []}, dealer = {"hand": []}))
print(calculate_hand_value(deck.build_standard_deck()))




def dealer_play(deck: list[dict], dealer: dict) -> bool:
    return




def run_full_game(deck: list[dict], player: dict, dealer:dict) -> None:
    # deal_two_each()

    # player_io.ask_player_action()
    return