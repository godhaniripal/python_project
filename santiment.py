from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float


    def get_mood(input_text: str, *, sensitivity: float) -> Mood:
        polarity: float = TextBlob(input_text).sentiment.polarity

        friendly_threshold: float = sensitivity