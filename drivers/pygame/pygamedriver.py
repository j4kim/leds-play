import pygame
import asyncio
from abc import ABC, abstractmethod

class PygameDriver(ABC):
    cells = ()
    default_color = 0xffffff
    screen = None
    scale = 40
    running = True
    on_event = None
    brightness = 1

    def reset(self):
        pass

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((6*self.scale, 7*self.scale), pygame.DOUBLEBUF)
        self.clear()

    async def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            pygame.display.flip()
            await asyncio.sleep(1/60)

    @abstractmethod
    def handle_event(self, event: pygame.event.Event):
        pass

    @abstractmethod
    def listen_controllers(self, on_event):
        pass

    @abstractmethod
    def stop_listening_controllers(self):
        pass

    def quit(self):
        self.running = False

    def fill(self, show = True):
        for y in range(7):
            for x in range(6):
                self.cells[y][x] = 0xffffff
        if show: self.show()

    def clear(self, show = True):
        self.cells = (
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        )
        if show: self.show()

    def set(self, x, y, color):
        self.cells[y][x] = color

    def show(self):
        self.screen.fill((0,0,0,255))
        for y in range(7):
            for x in range(6):
                margin = self.scale / 10
                rx = margin + x * self.scale
                ry = margin + y * self.scale
                size = self.scale - 2 * margin
                rect = pygame.Surface((size, size), pygame.SRCALPHA)
                colorval = self.cells[y][x]
                if type(colorval) is int:
                    colorval = '#' + hex(colorval).replace('0x','').rjust(6, '0')
                color = pygame.Color(colorval)
                color.a = int(255 * self.brightness)
                rect.fill(color)
                self.screen.blit(rect, (rx, ry))