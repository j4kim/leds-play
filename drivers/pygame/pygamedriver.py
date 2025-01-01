import pygame
import asyncio

key_bindings = {
    'w': 'arrow_up',
    'd': 'arrow_right',
    's': 'arrow_down',
    'a': 'arrow_left',
    'i': 'north',
    'l': 'east',
    'k': 'south',
    'j': 'west',
    'q': 'left',
    'o': 'right',
    ' ': 'select',
    '\r': 'start',
}

class PygameDriver:
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
                if self.on_event and event.type in [pygame.KEYUP, pygame.KEYDOWN]:
                    x = self.on_event({
                        'value': 1 if event.type == pygame.KEYDOWN else 0,
                        'key': key_bindings.get(event.unicode, event.unicode),
                    })
                    if asyncio.iscoroutine(x):
                        asyncio.create_task(x)
            pygame.display.flip()
            await asyncio.sleep(1/60)

    def listen_controllers(self, on_event):
        self.on_event = on_event

    def stop_listening_controllers(self):
        self.on_event = None

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