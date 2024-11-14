from enum import Enum

from src.resources import ResourceManager


class GameState(Enum):
    MENU = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4


class GameStateManager:
    def __init__(self):
        self.current_state = GameState.MENU
        self.resources = ResourceManager()

    def update(self):
        if self.current_state == GameState.MENU:
            self.update_menu()
        elif self.current_state == GameState.PLAYING:
            self.update_game()
        elif self.current_state == GameState.PAUSED:
            self.update_pause()
        elif self.current_state == GameState.GAME_OVER:
            self.update_game_over()

    def draw(self, screen):
        if self.current_state == GameState.MENU:
            self.draw_menu(screen)
        # 处理其他状态的绘制...
