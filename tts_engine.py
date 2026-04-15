from __future__ import annotations

from pathlib import Path
import pyttsx3
import subprocess
import sys

from ssml_utils import enhance_text


OUTPUT_PATH = Path("static/output.wav")
BASE_RATE = 180
BASE_VOLUME = 0.9


def _emotion_profile(emotion: str, intensity: float) -> tuple[int, float]:
    i = abs(float(intensity))
    if emotion == "happy":
        return int(BASE_RATE + 75 * i + 15), min(1.0, BASE_VOLUME + 0.18 * i)
    if emotion == "frustrated":
        return int(BASE_RATE - 85 * i - 10), max(0.35, BASE_VOLUME - 0.35 * i)
    if emotion == "surprised":
        return int(BASE_RATE + 95 * i + 20), min(1.0, BASE_VOLUME + 0.2 * i)
    if emotion == "inquisitive":
        return int(BASE_RATE + 35 * i + 8), min(1.0, BASE_VOLUME + 0.08 * i)
    return int(BASE_RATE - 10 * i), max(0.7, BASE_VOLUME - 0.08 * i)


def generate_speech(text: str, emotion: str, intensity: float) -> str:
    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    cmd = [
        sys.executable,
        __file__,
        "--speak-text",
        text,
        "--emotion",
        emotion,
        "--intensity",
        str(intensity),
    ]
    subprocess.run(
        cmd,
        check=True,
        timeout=20,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return str(OUTPUT_PATH).replace("\\", "/")


def text_to_speech_file(text: str, emotion: str, intensity: float) -> str:
    return generate_speech(text, emotion, intensity)


def _speak_in_process(text: str, emotion: str, intensity: float) -> None:
    rate, volume = _emotion_profile(emotion, intensity)
    enhanced = enhance_text(text, emotion, intensity)
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)
    voices = engine.getProperty("voices")
    if voices:
        engine.setProperty("voice", voices[0].id)
    engine.save_to_file(enhanced, str(OUTPUT_PATH))
    engine.runAndWait()
    engine.stop()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--speak-text", required=True)
    parser.add_argument("--emotion", required=True)
    parser.add_argument("--intensity", type=float, required=True)
    args = parser.parse_args()
    _speak_in_process(args.speak_text, args.emotion, args.intensity)
