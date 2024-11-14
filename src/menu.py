import pygame


class MainMenu:
    def __init__(self, resource_manager):
        self.resources = resource_manager
        self.buttons = {
            "start": pygame.Rect(150, 200, 100, 50),
            "easy": pygame.Rect(150, 280, 100, 50),
            "normal": pygame.Rect(150, 340, 100, 50),
            "hard": pygame.Rect(150, 400, 100, 50),
        }

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button_name, button_rect in self.buttons.items():
                    if button_rect.collidepoint(mouse_pos):
                        return button_name
        return None

    def draw(self, screen):
        # 绘制标题
        title = self.resources.get_image("title")
        screen.blit(title, (100, 50))

        # 绘制按钮
        for button_name, button_rect in self.buttons.items():
            pygame.draw.rect(screen, (200, 200, 200), button_rect)
            # 绘制按钮文字...
