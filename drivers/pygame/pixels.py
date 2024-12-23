import pygame
import asyncio

class Pixels:
    cells = ()
    default_color = 0xffffff
    screen = None
    scale = 40

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((6*self.scale, 7*self.scale))
        self.clear()

    async def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            pygame.display.flip()
            await asyncio.sleep(1/60)

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
                margin = self.scale / 10
                rx = margin + x * self.scale
                ry = margin + y * self.scale
                size = self.scale - 2 * margin
                rect = pygame.Rect(rx, ry, size, size)
                color = self.cells[y][x]
                pygame.draw.rect(self.screen, color, rect)