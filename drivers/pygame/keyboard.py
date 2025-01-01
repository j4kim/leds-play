import pygame
import asyncio
from .pygamedriver import PygameDriver

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

class PygameKeyboardDriver(PygameDriver):

    def handle_event(self, event: pygame.event.Event):
        if self.on_event and event.type in [pygame.KEYUP, pygame.KEYDOWN]:
            x = self.on_event({
                'value': 1 if event.type == pygame.KEYDOWN else 0,
                'key': key_bindings.get(event.unicode, event.unicode),
            })
            if asyncio.iscoroutine(x):
                asyncio.create_task(x)

    def listen_controllers(self, on_event):
        self.on_event = on_event

    def stop_listening_controllers(self):
        self.on_event = None
