import pygame

class TransformComponent:
    def set_position(self, position: tuple[int, int]):
        self.rect.x, self.rect.y = position
        
    def get_position(self) -> tuple[int, int]:
        return (self.rect.x, self.rect.y)

    def set_size(self, size: tuple[int, int]):
        position = self.rect.topleft if hasattr(self, 'rect') else (0, 0)

        self.shown_image = pygame.transform.scale(self.image, size)

        new_rect = self.shown_image.get_rect()
        new_rect.x, new_rect.y = position
        self.rect = new_rect

    def get_size(self) -> tuple[int, int]:
        return self.rect.size