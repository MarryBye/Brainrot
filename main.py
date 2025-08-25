import pygame

from random import choice, randint

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Pygame Window")
clock = pygame.time.Clock()
running = True

class GameObject:
    def __init__(self, image: pygame.surface.Surface, position: tuple[int, int], size: tuple[int, int], **kwargs):

        self.set_image(image)
        self.set_size(size)
        self.set_position(position)

        self.goto_goal_coordinates: tuple[int, int] = None

        self.debug_draw = kwargs.get("debug_draw", False)
        self.hidden = kwargs.get("hidden", False)
    
    def set_image(self, image: pygame.surface.Surface):
        size = self.get_size() if hasattr(self, 'rect') else (32, 32)
        position = self.get_position() if hasattr(self, 'rect') else (0, 0)
        
        self.image = image
        self.shown_image = pygame.transform.scale(self.image, size)
        
        new_rect = self.shown_image.get_rect()
        new_rect.x, new_rect.y = position
        self.rect = new_rect
        
    def get_image(self) -> pygame.surface.Surface:
        return self.image
    
    def set_size(self, size: tuple[int, int]):
        self.shown_image = pygame.transform.scale(self.image, size)
        new_rect = self.shown_image.get_rect()
        new_rect.x, new_rect.y = self.get_position()
        self.rect = new_rect

    def get_size(self) -> tuple[int, int]:
        return self.rect.width, self.rect.height
    
    def set_position(self, position: tuple[int, int]):
        self.rect.x, self.rect.y = position
        
    def get_position(self) -> tuple[int, int]:
        return self.rect.x, self.rect.y
    
    def set_color(self, color: tuple[int, int, int]):
        self.image.fill(color)
        self.color = color
        
    def get_color(self) -> tuple[int, int, int]:
        return self.color

    def draw(self, surface: pygame.surface.Surface):
        if not self.hidden:
            surface.blit(self.shown_image, self.get_position())
        
        if self.debug_draw:
            pygame.draw.rect(surface, (0, 255, 0), self.rect, 2)
            
    def is_selected(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos) or self.rect.colliderect(selection.rect)

    def update(self):
        if self.goto_goal_coordinates:
            goal_x, goal_y = self.goto_goal_coordinates
            current_x, current_y = self.get_position()
            
            if (current_x, current_y) != (goal_x, goal_y):
                step_x = (goal_x - current_x) / max(abs(goal_x - current_x), 1)
                step_y = (goal_y - current_y) / max(abs(goal_y - current_y), 1)
                
                new_x = current_x + step_x
                new_y = current_y + step_y
                
                if abs(new_x - goal_x) < 1 and abs(new_y - goal_y) < 1:
                    self.set_position((goal_x, goal_y))
                    self.goto_goal_coordinates = None
                else:
                    self.set_position((new_x, new_y))

test_img = pygame.image.load("test.png")

voices = [
    pygame.mixer.Sound(f"voice{i}.ogg") for i in range(1, 6)
]

vujivalovos = [
    GameObject(test_img, (10 + 72 * i, 100), (64, 64), debug_draw=False) for i in range(10) 
]

bg_img = pygame.image.load("bg.jpeg")
bg = GameObject(bg_img, (0, 0), (800, 600), hidden=False)

selection = GameObject(test_img, (0, 0), (0, 0), debug_draw=True, hidden=True)
selected_units = []

is_selecting = False

pygame.mixer_music.load("wh_music.mp3")
pygame.mixer_music.play(loops=-1)

def play_voice():
    n = randint(0, 3)
    if n == 3:
        choice(voices).play()

while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                selected_units.clear()
                for obj in vujivalovos:
                    if obj.is_selected() and obj not in selected_units:
                        selected_units.append(obj)
                        play_voice()
                        break
                selection.set_position(pygame.mouse.get_pos())
                selection.set_size((0, 0))
                is_selecting = True
                
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and is_selecting:
                is_selecting = False
                selection.set_size((0, 0))
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                play_voice()
                for obj in selected_units:
                    obj.goto_goal_coordinates = pygame.mouse.get_pos()
                
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0] and is_selecting:
                mouse_pos = pygame.mouse.get_pos()

                if mouse_pos[0] < selection.get_position()[0]:
                    selection.set_position((mouse_pos[0], selection.get_position()[1]))
                    
                if mouse_pos[1] < selection.get_position()[1]:
                    selection.set_position((selection.get_position()[0], mouse_pos[1]))
                    
                width = mouse_pos[0] - selection.get_position()[0]
                height = mouse_pos[1] - selection.get_position()[1]

                selection.set_size((width, height))
            
    screen.fill((0, 0, 0))
    
    bg.draw(screen)
    
    for obj in vujivalovos:
        obj.draw(screen)
        obj.update()
        obj.debug_draw = False
        if obj.is_selected():
            if is_selecting:
                selected_units.append(obj)
            else:
                obj.debug_draw = True
            
    for selected in selected_units:
        selected.debug_draw = True
    
    selection.draw(screen)
    selection.update()
    
    clock.tick(60)
    
    pygame.display.update()