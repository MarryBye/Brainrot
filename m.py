import pygame

from core.lib.PGUI.widgets.widget import Widget
from core.lib.PGUI.widgets.button import Button

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Example usage of Widget
widget_image = pygame.Surface((100, 50))
widget = Button(widget_image, (50, 50), (100, 50))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        widget.handle_event(event)

    widget.update()

    screen.fill((30, 30, 30))
    widget.draw(screen)
    
    clock.tick(60)
    pygame.display.update()