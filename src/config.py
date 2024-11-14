import pygame

# 屏幕设置
SCREEN_WIDTH = 288  # 游戏原始宽度
SCREEN_HEIGHT = 512  # 游戏原始高度
SCALE = 1.0  # 屏幕缩放比例
WIDTH = int(SCREEN_WIDTH * SCALE)
HEIGHT = int(SCREEN_HEIGHT * SCALE)
FPS = 60

# 物理参数
GRAVITY = 0.25
BIRD_JUMP_SPEED = -5.0
BIRD_MAX_SPEED = 10.0
GROUND_Y = HEIGHT - 112  # 地面高度

# 游戏对象参数
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
PIPE_WIDTH = 52
PIPE_HEIGHT = 320

# 游戏机制参数
ANIMATION_SPEED = 0.1  # 鸟的动画速度

# 分数系统
SCORE_POSITION = (WIDTH // 2, 50)
HIGH_SCORE_FILE = "high_scores.json"


# 难度设置
class DifficultySettings:
    EASY = {
        "GRAVITY": 0.2,
        "JUMP_SPEED": -6,
        "PIPE_SPEED": -2,
        "PIPE_GAP": 180,
        "PIPE_FREQUENCY": 2000,
    }

    NORMAL = {
        "GRAVITY": 0.25,
        "JUMP_SPEED": -7,
        "PIPE_SPEED": -3,
        "PIPE_GAP": 150,
        "PIPE_FREQUENCY": 1500,
    }

    HARD = {
        "GRAVITY": 0.3,
        "JUMP_SPEED": -8,
        "PIPE_SPEED": -4,
        "PIPE_GAP": 130,
        "PIPE_FREQUENCY": 1200,
    }


class GameSettings:
    def __init__(self):
        self.difficulty = "normal"
        self.settings = DifficultySettings.NORMAL

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        if difficulty == "easy":
            self.settings = DifficultySettings.EASY
        elif difficulty == "normal":
            self.settings = DifficultySettings.NORMAL
        elif difficulty == "hard":
            self.settings = DifficultySettings.HARD


# 资源路径
RESOURCE_PATH = {
    "images": "assets/images/",
    "sounds": "assets/sounds/",
    "fonts": "assets/fonts/",
}

# 颜色定义
COLORS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "SKY_BLUE": (78, 192, 202),
    "GREEN": (77, 206, 145),
    "RED": (255, 0, 0),
}

# 窗口定义
pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
