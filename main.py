import pygame
from checkers.game import Game
from checkers.algorithm import minimax

cols = 8
width = 800
height = 800
square = width // cols
WHITE = (255, 255, 255)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Checkers")
# deff = input("Enter Game Difficulty from 1 to 5 (1 easy, 5 Hard): ")


def get_from_mouse(position):
    x, y = position
    row = y // square
    col = x // square
    return row, col


def main():
    run = True
    game = Game(window)
    while run:
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


main()
