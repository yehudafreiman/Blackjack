from core import player_io

def calculate_hand_value(hand: list[dict]) -> int:
    result = 0
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6':6 , '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}
    for card in hand:
        for k, v in values.items():
            if k == card["rank"]:
                result += v
    return result

def deal_two_each(deck :list[dict], player: dict, dealer: dict) -> None:
    for i in range(2):
        player["hand"].append(deck.pop())
    for i in range(2):
        dealer["hand"].append(deck.pop())
    player_hand_value = calculate_hand_value(player["hand"])
    dealer_hand_value = calculate_hand_value(dealer["hand"])
    print(f"player hand value: {player_hand_value}, dealer hand value: {dealer_hand_value}")
    return None


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while True:
        dealer["hand"].append(deck.pop())
        if calculate_hand_value(dealer["hand"]) > 21:
            print(f"dealer hand value: {calculate_hand_value(dealer["hand"])}")
            print("dealer loss")
            return False
        if 17 < calculate_hand_value(dealer["hand"]) < 21:
            print(f"dealer hand value: {calculate_hand_value(dealer["hand"])}")
            print("dealer end")
            return True


def run_full_game(deck: list[dict], player: dict, dealer:dict) -> None:
    deal_two_each(deck, player, dealer)
    selected_action = player_io.ask_player_action()
    if selected_action == "H":
        while True:
            player["hand"].append(deck.pop())
            player_hand_value = calculate_hand_value(player["hand"])
            if player_hand_value > 21:
                print(f"player hand value: {player_hand_value}")
                print("player loss")
                break
            else:
                continue
    else:
        dealer_play(deck, dealer)
        if dealer_play(deck, dealer) == True:
            if calculate_hand_value(player["hand"]) == calculate_hand_value(dealer["hand"]):
                print("teiku")
            elif calculate_hand_value(player["hand"]) < calculate_hand_value(dealer["hand"]):
                print("dealer won")
            else:
                print("player won")
    return None
