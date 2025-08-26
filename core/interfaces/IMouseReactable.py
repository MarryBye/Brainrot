from abc import ABC, abstractmethod

class IMouseReactable(ABC):
    @abstractmethod
    def on_hover(self):
        pass

    @abstractmethod
    def on_click(self):
        pass

    @abstractmethod
    def on_release(self):
        pass
    
    @abstractmethod
    def on_leave(self):
        pass
    
    @abstractmethod
    def is_hovered(self) -> bool:
        pass