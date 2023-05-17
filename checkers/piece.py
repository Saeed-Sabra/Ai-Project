import pygame


cols = 8
width = 800
square = width // cols
crown = pygame.transform.scale(pygame.image.load("checkers/crown.png"), (44, 25))


class Piece:
    pad = 13

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = square * self.col + square // 2
        self.y = square * self.row + square // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), square // 2 - self.pad)
        if self.king:
            win.blit(
                crown,
                (self.x - crown.get_width() // 2, self.y - crown.get_height() // 2),
            )

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
