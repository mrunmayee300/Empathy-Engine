from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from nltk.sentiment import SentimentIntensityAnalyzer
from pydantic import BaseModel, Field
from starlette.requests import Request

from emotion import detect_emotion
from tts_engine import generate_speech


app = FastAPI(title="Empathy Engine")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
_analyzer = SentimentIntensityAnalyzer()


class SpeakRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=1500)


class SpeakResponse(BaseModel):
    emotion: str
    intensity: float
    audio_file: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/speak", response_model=SpeakResponse)
def speak(payload: SpeakRequest) -> SpeakResponse:
    text = payload.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    result = detect_emotion(text)
    intensity = round(_analyzer.polarity_scores(text)["compound"], 3)
    try:
        audio_file = generate_speech(text, result.emotion, intensity)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"TTS generation failed: {exc}") from exc
    return SpeakResponse(
        emotion=result.emotion,
        intensity=intensity,
        audio_file=audio_file,
    )
