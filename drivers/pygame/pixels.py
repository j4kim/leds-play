import pygame
import asyncio

key_bindings = {
    2: 'north',
    0: 'east',
    1: 'south',
    3: 'west',
    9: 'left',
    10: 'right',
    4: 'select',
    6: 'start',
}

class Pixels:
    cells = ()
    default_color = 0xffffff
    screen = None
    scale = 40
    running = True
    joysticks = []
    on_event = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((6*self.scale, 7*self.scale))
        self.clear()

    async def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if self.on_event and self.joysticks and event.type in [pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN, pygame.JOYAXISMOTION]:
                    self.on_event(self.transform_event(event))
            pygame.display.flip()
            await asyncio.sleep(1/60)

    def transform_event(self, event: pygame.event.Event):
        binding = None
        if event.type == pygame.JOYAXISMOTION:
            v = round(event.value)
            if event.axis == 1 and v == -1:
                binding = 'arrow_up'
            elif event.axis == 1 and v == 1:
                binding = 'arrow_down'
            elif event.axis == 0 and v == -1:
                binding = 'arrow_left'
            elif event.axis == 0 and v == 1:
                binding = 'arrow_right'
            value = abs(v)
        else:
            value = 1 if event.type == pygame.JOYBUTTONDOWN else 0
            binding = key_bindings[event.button]
        return {
            'value': value,
            'device': event.joy,
            'binding': binding,
        }

    def listen_controllers(self, on_event):
        count = pygame.joystick.get_count()
        if count == 0:
            raise Exception("No devices found")
        for i in range(count):
            joystick = pygame.joystick.Joystick(i)
            self.joysticks.append(joystick)
            self.on_event = on_event

    def stop_listening_controllers(self):
        self.joysticks = []
        self.on_event = None

    def quit(self):
        self.running = False

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