from src.game import Bird


class Animation:
    def __init__(self, frames, frame_duration):
        self.frames = frames
        self.frame_duration = frame_duration
        self.current_frame = 0
        self.timer = 0

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.frame_duration:
            self.timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def get_current_frame(self):
        return self.frames[self.current_frame]


class AnimatedBird(Bird):
    def __init__(self, resource_manager):
        super().__init__()
        bird_frames = resource_manager.get_image("bird")
        self.animation = Animation(bird_frames, 100)  # 100ms per frame

    def update(self, dt):
        super().update()
        self.animation.update(dt)

    def draw(self, screen):
        current_frame = self.animation.get_current_frame()
        screen.blit(current_frame, (self.x - 20, self.y - 20))
