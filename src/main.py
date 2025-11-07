from game import game
from pygame import event, \
    QUIT


def main():
    _game = game()
    _game.init()
    while (_game.game_running):
        for e in event.get():
            if e.type == QUIT:
                _game.game_running = False
        _game.update()
        _game.draw()
    _game.end()


if __name__ == "__main__":
    main()
