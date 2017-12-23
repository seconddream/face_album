from enum import Enum


class Emotion:

    def __init__(self, emotion_id=None, type=EmotionType.NOTSET):
        self.emotion_id = emotion_id
        self.type = type


class EmotionType(Enum):
    HAPPY: 1
    SAD: 2
    SURPRISE: 3
    NOTSET: 4