import pygame

from core.base_sprite import BaseSprite
from core.interfaces.IMouseReactable import IMouseReactable

class Widget(BaseSprite, IMouseReactable):
    def __init__(self, image: pygame.surface.Surface, position: tuple[int, int], size: tuple[int, int], **kwargs):
        super().__init__(image, position, size, **kwargs)

    def handle_event(self, event: pygame.event.Event):
        super().handle_event(event)
        
        if event.type == pygame.MOUSEMOTION:
            if self.is_hovered():
                self.on_hover()
            else:
                self.on_leave()
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.is_hovered():
                self.on_click()
                
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.is_hovered():
                self.on_release()

    def is_hovered(self) -> bool:
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def on_leave(self):
        return super().on_leave()

    def on_hover(self):
        return super().on_hover()

    def on_click(self):
        return super().on_click()
    
    def on_release(self):
        return super().on_release()