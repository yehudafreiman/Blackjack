
def ask_player_action() -> str:
    while True:
        action = input("Enter 'S' or 'H' in capital letters: ")
        if action == 'S' or action == 'H':
            break
        print("Enter a valid action")
    return action
