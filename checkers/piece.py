import pygame

GREY = (128, 128, 128)
cols = 8
width = 800
square = width // cols
crown = pygame.transform.scale(pygame.image.load("checkers/crown.png"), (44, 25))


class Piece:
    PADDING = 15
    OUTLINE = 2

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
        radius = square // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
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
