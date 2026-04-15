from __future__ import annotations

from dataclasses import dataclass
from nltk import data
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk


def _ensure_vader() -> None:
    try:
        data.find("sentiment/vader_lexicon.zip")
    except LookupError:
        nltk.download("vader_lexicon", quiet=True)


_ensure_vader()
_analyzer = SentimentIntensityAnalyzer()


@dataclass
class EmotionResult:
    emotion: str
    intensity: float


def detect_emotion(text: str) -> EmotionResult:
    score = _analyzer.polarity_scores(text)["compound"]
    intensity = abs(score)
    stripped = text.strip()

    if "?" in stripped:
        emotion = "inquisitive"
    elif intensity >= 0.65:
        emotion = "surprised"
    elif score >= 0.12:
        emotion = "happy"
    elif score <= -0.12:
        emotion = "frustrated"
    else:
        emotion = "neutral"

    return EmotionResult(emotion=emotion, intensity=round(intensity, 3))
