import pygame

class Pixels:
    cells = ()
    default_color = 0xffffff
    screen = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 700))
        pygame.event.get()
        self.clear()

    def fill(self):
        for y in range(7):
            for x in range(6):
                self.cells[y][x] = 0xffffff
        self.show()

    def clear(self):
        self.cells = (
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        )
        self.show()

    def set(self, x, y, color):
        self.cells[y][x] = color

    def show(self):
        for y in range(7):
            for x in range(6):
                pygame.draw.rect(self.screen, self.cells[y][x], pygame.Rect(10+x*100, 10+y*100, 80, 80))
        pygame.display.flip()