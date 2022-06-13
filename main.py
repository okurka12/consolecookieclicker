import os


class GameState:
    def __init__(self):
        self.cookies = 0

    def addcookie(self):
        self.cookies += 1


def print_game_state(state: GameState) -> None:
    print(f"Počet sušenek: {state.cookies}")


def clear():
    os.system("cls")


def game_loop():
    state = GameState()
    while True:
        clear()
        print_game_state(state)
        input()
        state.addcookie()


def main():
    game_loop()



if __name__ == "__main__":
    main()
