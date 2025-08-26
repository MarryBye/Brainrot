import pygame

from abc import ABC, abstractmethod

class GameObject(ABC):
    
    @abstractmethod
    def handle_event(self, event: pygame.event.Event):
        pass
    
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, surface: pygame.surface.Surface):
        pass