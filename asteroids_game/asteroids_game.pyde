from game_controller import GameController

SPACE = {'w': 600, 'h': 600}
fadeout = 150.0

game_controller = GameController(SPACE, fadeout)


def setup():
    size(SPACE['w'], SPACE['h'])
    colorMode(RGB, 1)


def draw():
    background(0)
    game_controller.update()


def keyPressed():
    if (key == CODED):
        game_controller.handle_keypress(key, keyCode)
    else:
        game_controller.handle_keypress(key)


def keyReleased():
    game_controller.handle_keyup()
