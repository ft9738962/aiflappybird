import pygame

from config import GROUND_Y, HEIGHT, WIDTH
from main import Bird, Pipe


class Game:
    def __init__(self, resource_manager, score_manager):
        self.resource_manager = resource_manager
        self.score_manager = score_manager
        self.bird = None
        self.pipes = []
        self.settings = None
        self.reset()

    def reset(self):
        # 重置游戏状态
        self.bird = Bird(self.resource_manager)
        self.pipes = []
        self.next_pipe_time = 0
        self.score_manager.reset_score()
        self.game_over = False

    def update(self, dt):
        if self.game_over:
            return

        # 更新鸟的位置
        self.bird.update(dt)

        # 更新管道
        self.update_pipes(dt)

        # 碰撞检测
        if self.check_collisions():
            self.game_over = True
            self.resource_manager.play_sound("hit")
            return

        # 检查得分
        self.check_score()

    def update_pipes(self, dt):
        # 创建新管道
        self.next_pipe_time -= dt
        if self.next_pipe_time <= 0:
            self.create_pipe()
            self.next_pipe_time = self.settings.PIPE_FREQUENCY

        # 更新现有管道
        for pipe in self.pipes[:]:
            pipe.update(dt)
            if pipe.is_off_screen():
                self.pipes.remove(pipe)

    def create_pipe(self):
        new_pipe = Pipe(self.resource_manager, self.settings)
        self.pipes.append(new_pipe)

    def check_collisions(self):
        # 检查地面碰撞
        if self.bird.y >= GROUND_Y - 10:
            return True

        # 检查管道碰撞
        for pipe in self.pipes:
            if pipe.collides_with(self.bird):
                return True

        return False

    def check_score(self):
        for pipe in self.pipes:
            if pipe.check_passed(self.bird):
                self.score_manager.add_score()
                self.resource_manager.play_sound("score")

    def draw(self, screen):
        # 绘制背景
        screen.blit(self.resource_manager.images["background"], (0, 0))

        # 绘制管道
        for pipe in self.pipes:
            pipe.draw(screen)

        # 绘制鸟
        self.bird.draw(screen)

        # 绘制分数
        self.score_manager.draw_score(screen)

        # 如果游戏结束,绘制游戏结束画面
        if self.game_over:
            self.draw_game_over(screen)

    def draw_game_over(self, screen):
        game_over_img = self.resource_manager.images["game_over"]
        x = WIDTH // 2 - game_over_img.get_width() // 2
        y = HEIGHT // 3
        screen.blit(game_over_img, (x, y))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not self.game_over:
                self.bird.jump()
                self.resource_manager.play_sound("jump")
