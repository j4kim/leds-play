import pygame

pygame.joystick.init()

count = pygame.joystick.get_count()
print("Number of joysticks: {}".format(count))

for i in range(count):
    joystick = pygame.joystick.Joystick(i)
    print(joystick, joystick.get_name())