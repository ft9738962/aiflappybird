class DifficultySettings:
    EASY = {
        "GRAVITY": 0.2,
        "JUMP_SPEED": -6,
        "PIPE_SPEED": 2,
        "PIPE_GAP": 180,
        "PIPE_FREQUENCY": 2000,
    }

    NORMAL = {
        "GRAVITY": 0.25,
        "JUMP_SPEED": -7,
        "PIPE_SPEED": 3,
        "PIPE_GAP": 150,
        "PIPE_FREQUENCY": 1500,
    }

    HARD = {
        "GRAVITY": 0.3,
        "JUMP_SPEED": -8,
        "PIPE_SPEED": 4,
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
