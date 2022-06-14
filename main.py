import os

CLICKERS = [  # (cps, price)
    (1, 15),
    (10, 150)
]


GAME_UI = """Počet sušenek: $COOKIES
CPS: $CPS
Nakoupená klikátka:
$CLICKERS
o - obchod
"""

SHOP_UI = """

"""


class GameState:
    def __init__(self):
        self.cookies = 0
        self.cps = 0
        self.clickers = {}  # key: value -> cps: number bought

    def addcookie(self):
        self.cookies += 1


def print_game_state(state: GameState) -> None:
    text = GAME_UI.replace("$COOKIES", str(state.cookies))
    text = text.replace("$CPS", str(state.cps))
    text = text.replace("$CLICKERS", "\n".join([f"{cps}cps clicker: {n}" for cps, n in state.clickers.items()]))
    print(text)


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
