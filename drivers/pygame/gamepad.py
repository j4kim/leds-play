import pygame
from .pygamedriver import PygameDriver

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

class PygameGamepadDriver(PygameDriver):
    joysticks = []

    def handle_event(self, event: pygame.event.Event):
        if self.on_event and self.joysticks and event.type in [pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN, pygame.JOYAXISMOTION]:
            self.on_event(self.transform_event(event))

    def transform_event(self, event: pygame.event.Event):
        key = None
        if event.type == pygame.JOYAXISMOTION:
            v = round(event.value)
            if event.axis == 1 and v == -1:
                key = 'arrow_up'
            elif event.axis == 1 and v == 1:
                key = 'arrow_down'
            elif event.axis == 0 and v == -1:
                key = 'arrow_left'
            elif event.axis == 0 and v == 1:
                key = 'arrow_right'
            value = abs(v)
        else:
            value = 1 if event.type == pygame.JOYBUTTONDOWN else 0
            key = key_bindings.get(event.button, event.button)
        return {
            'value': value,
            'device': event.joy,
            'key': key,
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
