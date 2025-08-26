import pygame

class ImageComponent:
    
    def set_image(self, image: pygame.surface.Surface):
        size = self.rect.size if hasattr(self, 'rect') else (32, 32)
        position = self.rect.topleft if hasattr(self, 'rect') else (0, 0)
        
        self.image = image
        self.shown_image = pygame.transform.scale(self.image, size)
        
        new_rect = self.shown_image.get_rect()
        new_rect.x, new_rect.y = position
        self.rect = new_rect
        
    def get_image(self) -> pygame.surface.Surface:
        return self.image