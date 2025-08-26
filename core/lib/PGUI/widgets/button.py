import pygame

from core.lib.PGUI.widgets.widget import Widget

class Button(Widget):
    def __init__(self, image: pygame.surface.Surface, position: tuple[int, int], size: tuple[int, int], **kwargs):
        super().__init__(image, position, size, **kwargs)

    def on_hover(self):
        self.shown_image.fill((200, 200, 200))
        
    def on_leave(self):
        self.shown_image.fill((225, 225, 225))

    def on_click(self):
        self.shown_image.fill((255, 255, 255))
        
    def on_release(self):
        self.shown_image.fill((200, 200, 200))
