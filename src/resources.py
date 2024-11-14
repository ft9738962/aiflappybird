import os
import random

import pygame

from config import (
    BIRD_HEIGHT,
    BIRD_JUMP_SPEED,
    BIRD_WIDTH,
    COLORS,
    GRAVITY,
    PIPE_GAP,
    PIPE_HEIGHT,
    PIPE_SPEED,
    PIPE_WIDTH,
    WINDOW,
    WINDOW_HEIGHT,
)


class Bird:
    def __init__(self):
        self.x = BIRD_WIDTH // 3
        self.y = BIRD_HEIGHT // 2
        self.velocity = 0

    def jump(self):
        self.velocity = BIRD_JUMP_SPEED

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        pygame.draw.circle(WINDOW, COLORS["RED"], (int(self.x), int(self.y)), 20)


class Pipe:
    def __init__(self):
        self.gap_y = random.randint(200, PIPE_HEIGHT - 200)
        self.x = PIPE_WIDTH
        self.width = 50
        self.scored = False

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self):
        # 上方水管
        pygame.draw.rect(
            WINDOW, COLORS["GREEN"], (self.x, 0, self.width, self.gap_y - PIPE_GAP // 2)
        )
        # 下方水管
        pygame.draw.rect(
            WINDOW,
            COLORS["GREEN"],
            (self.x, self.gap_y + PIPE_GAP // 2, self.width, WINDOW_HEIGHT),
        )

    def collide(self, bird):
        bird_rect = pygame.Rect(bird.x - 20, bird.y - 20, 40, 40)
        top_pipe = pygame.Rect(self.x, 0, self.width, self.gap_y - PIPE_GAP // 2)
        bottom_pipe = pygame.Rect(
            self.x, self.gap_y + PIPE_GAP // 2, self.width, WINDOW_HEIGHT
        )
        return bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe)


class ResourceManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.fonts = {}

    def load_images(self):
        image_path = "assets/images/"
        # 游戏对象图片
        self.images["bird"] = [
            pygame.image.load(os.path.join(image_path, f"bird{i}.png"))
            for i in range(1, 4)
        ]
        self.images["background"] = pygame.image.load(
            os.path.join(image_path, "background.png")
        )
        self.images["pipe"] = pygame.image.load(os.path.join(image_path, "pipe.png"))

        # UI元素
        self.images["title"] = pygame.image.load(os.path.join(image_path, "title.png"))
        self.images["game_over"] = pygame.image.load(
            os.path.join(image_path, "game_over.png")
        )
        # 加载数字图片(0-9)
        self.images["numbers"] = [
            pygame.image.load(os.path.join(image_path, f"number_{i}.png"))
            for i in range(10)
        ]
        # 加载按钮图片
        self.images["button_play"] = pygame.image.load(
            os.path.join(image_path, "button_play.png")
        )
        self.images["button_scores"] = pygame.image.load(
            os.path.join(image_path, "button_scores.png")
        )
