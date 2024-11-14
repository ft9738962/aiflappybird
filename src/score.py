import pygame

from config import WIDTH


class ScoreManager:
    def __init__(self, resource_manager):
        self.resource_manager = resource_manager
        self.current_score = 0
        self.high_scores = self.load_high_scores()
        self.score_changed = False
        self.score_position = (WIDTH // 2, 50)  # 居中显示

    def add_score(self, points=1):
        self.current_score += points
        self.score_changed = True

    def reset_score(self):
        self.current_score = 0
        self.score_changed = True

    def draw_score(self, screen):
        # 将分数转换为字符串
        score_str = str(self.current_score)
        number_images = self.resource_manager.images["numbers"]

        # 计算所有数字的总宽度以居中显示
        total_width = sum(number_images[int(d)].get_width() for d in score_str)
        spacing = 2  # 数字间距
        x = self.score_position[0] - total_width // 2
        y = self.score_position[1]

        # 渲染每个数字
        for digit in score_str:
            digit_image = number_images[int(digit)]
            screen.blit(digit_image, (x, y))
            x += digit_image.get_width() + spacing

    def draw_high_scores(self, screen):
        # 绘制最高分界面
        y = 200
        for difficulty, score in self.high_scores.items():
            score_str = f"{difficulty.title()}: {score}"
            # 使用pygame的默认字体,也可以使用自定义字体
            text = pygame.font.Font(None, 36).render(score_str, True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, y))
            y += 50
