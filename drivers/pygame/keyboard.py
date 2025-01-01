import pygame
from .pygamedriver import PygameDriver

key_bindings = {
    pygame.K_UP: 'arrow_up',
    pygame.K_RIGHT: 'arrow_right',
    pygame.K_DOWN: 'arrow_down',
    pygame.K_LEFT: 'arrow_left',
    pygame.K_w: 'north',
    pygame.K_a: 'east',
    pygame.K_s: 'south',
    pygame.K_d: 'west',
    pygame.K_q: 'left',
    pygame.K_e: 'right',
    pygame.K_SPACE: 'start',
    pygame.K_RETURN: 'start',
    pygame.K_BACKSPACE: 'select',
    pygame.K_ESCAPE: 'select',
}

class PygameKeyboardDriver(PygameDriver):

    def handle_event(self, event: pygame.event.Event):
        if self.on_event and event.type in [pygame.KEYUP, pygame.KEYDOWN]:
            self.on_event({
                'value': 1 if event.type == pygame.KEYDOWN else 0,
                'key': key_bindings.get(event.key, event.unicode),
            })

    def listen_controllers(self, on_event):
        self.on_event = on_event

    def stop_listening_controllers(self):
        self.on_event = None
