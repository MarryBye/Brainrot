import pygame

from core.game_object import GameObject
from core.components.image_component import ImageComponent
from core.components.transform_component import TransformComponent

class BaseSprite(GameObject, ImageComponent, TransformComponent):

    def __init__(self, image: pygame.surface.Surface, position: tuple[int, int], size: tuple[int, int], **kwargs):
        
        self.image = image
        self.shown_image = pygame.transform.scale(self.image, size)
        self.rect = self.shown_image.get_rect()
        self.rect.x, self.rect.y = position

        self.draw_hitbox = kwargs.get("draw_hitbox", False)
        self.hidden = kwargs.get("hidden", False)
        self.disabled = kwargs.get("disabled", False)
        
    def handle_event(self, event: pygame.event.Event):
        return super().handle_event(event)
    
    def draw(self, surface: pygame.surface.Surface):
        super().draw(surface)

        if self.draw_hitbox:
            pygame.draw.rect(surface, (255, 0, 0), self.rect, 1)

        if not self.hidden:
            surface.blit(self.shown_image, self.get_position())

    def update(self):
        return super().update()