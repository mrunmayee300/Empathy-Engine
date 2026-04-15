from __future__ import annotations

import argparse

from emotion import detect_emotion
from tts_engine import text_to_speech_file


def run() -> None:
    parser = argparse.ArgumentParser(description="Empathy Engine CLI")
    parser.add_argument("text", nargs="+", help="Text to convert to expressive speech")
    args = parser.parse_args()
    text = " ".join(args.text).strip()

    result = detect_emotion(text)
    audio_file = text_to_speech_file(text, result.emotion, result.intensity)
    print(f"Emotion: {result.emotion}")
    print(f"Intensity: {result.intensity}")
    print(f"Audio: {audio_file}")


if __name__ == "__main__":
    run()
