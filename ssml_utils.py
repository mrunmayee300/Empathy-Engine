from __future__ import annotations

import re
from typing import List


PAUSE_MAP = {
    ",": 120,
    ";": 170,
    ":": 170,
    ".": 220,
    "!": 260,
    "?": 260,
}


def emphasize_caps(text: str) -> str:
    def _emphasis(match: re.Match) -> str:
        word = match.group(0)
        return f"{word} {word.lower()}"

    return re.sub(r"\b[A-Z]{2,}\b", _emphasis, text)


def inject_pauses(text: str) -> str:
    out = []
    for ch in text:
        out.append(ch)
        if ch in PAUSE_MAP:
            ms = PAUSE_MAP[ch]
            out.append(f" [pause:{ms}] ")
    return "".join(out)


def split_chunks(text: str, max_chunk_size: int = 180) -> List[str]:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    chunks: List[str] = []
    cur = ""

    for part in parts:
        candidate = f"{cur} {part}".strip()
        if len(candidate) > max_chunk_size and cur:
            chunks.append(cur)
            cur = part
        else:
            cur = candidate

    if cur:
        chunks.append(cur)
    return chunks or [text]


def enhance_text(text: str, emotion: str, intensity: float) -> str:
    s = text.strip()
    i = abs(float(intensity))
    s = re.sub(r"\b(very)\b", r"\1...", s, flags=re.IGNORECASE)
    s = s.replace(".", "... ")
    s = s.replace("!", "!!! ")

    s = re.sub(r"\b(really|extremely|so|totally|absolutely)\b", lambda m: m.group(0).upper(), s, flags=re.IGNORECASE)

    if emotion == "happy":
        if "!" not in s:
            s = f"{s}!!!"
        s = re.sub(r"\b(good|great|awesome|love|happy|amazing)\b", lambda m: m.group(0).upper(), s, flags=re.IGNORECASE)
    elif emotion == "frustrated":
        s = re.sub(r"\b(\w{5,})\b", lambda m: m.group(1).upper() if len(m.group(1)) % 2 == 0 else m.group(1), s)
        s = s.replace(",", ", ... ")
        s = s.replace("... ", ".... ")
    elif emotion == "surprised":
        s = f"Wait... {s}"
        if not s.endswith("?!"):
            s = f"{s}?!"
    elif emotion == "inquisitive":
        s = s.rstrip(".! ")
        if not s.endswith("?"):
            s = f"{s}?"

    if i > 0.75:
        s = s.replace("... ", ".... ")
    elif i > 0.45:
        s = s.replace("... ", "...  ")
    return " ".join(s.split())
