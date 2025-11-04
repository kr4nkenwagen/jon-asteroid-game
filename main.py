from game import game
import pygame


def main():
    _game = game()
    _game.init()
    while (_game.game_running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _game.game_running = False
        _game.update()
        _game.draw()
    _game.end()


if __name__ == "__main__":
    main()
