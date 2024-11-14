import pygame

from src.config import (
    COLORS,
    WINDOW,
    DifficultySettings,
)
from src.game import Game
from src.menu import MainMenu
from src.resources import ResourceManager
from src.score import ScoreManager
from src.states import GameState, GameStateManager

# 初始化pygame
pygame.init()

# 游戏窗口设置
pygame.display.set_caption("Flappy Bird")


# 游戏参数
class GameMain:
    def __init__(self):
        self.screen = WINDOW
        self.clock = pygame.time.Clock()

        # 初始化所有管理器
        self.resource_manager = ResourceManager()
        self.resource_manager.load_images()
        self.resource_manager.load_sounds()

        self.score_manager = ScoreManager(self.resource_manager)
        self.game = Game(self.resource_manager, self.score_manager)
        self.state_manager = GameStateManager()

        # 创建菜单
        self.menu = MainMenu(self.resource_manager)

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(60)

            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_event(event)

            # 更新和绘制
            self.update(dt)
            self.draw()

            pygame.display.flip()

    def handle_event(self, event):
        if self.state_manager.current_state == GameState.MENU:
            menu_action = self.menu.handle_input(event)
            if menu_action:
                self.handle_menu_action(menu_action)
        elif self.state_manager.current_state == GameState.PLAYING:
            self.game.handle_input(event)

    def handle_menu_action(self, action):
        if action == "start":
            self.state_manager.current_state = GameState.PLAYING
            self.game.reset()
        elif action in ["easy", "normal", "hard"]:
            self.game.settings = DifficultySettings.get_settings(action)

    def update(self, dt):
        if self.state_manager.current_state == GameState.PLAYING:
            self.game.update(dt)

    def draw(self):
        self.screen.fill(COLORS["BLACK"])

        if self.state_manager.current_state == GameState.MENU:
            self.menu.draw(self.screen)
        elif self.state_manager.current_state == GameState.PLAYING:
            self.game.draw(self.screen)


if __name__ == "__main__":
    game = GameMain()
    game.run()
