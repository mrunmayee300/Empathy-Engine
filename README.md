# Empathy Engine

## Overview

The Empathy Engine is a text-to-speech system that enhances traditional voice output by incorporating emotion-aware modulation. It analyzes input text, detects the underlying sentiment, and dynamically adjusts speech parameters such as rate and volume to produce more natural and expressive audio.

The goal is to reduce the robotic nature of standard TTS systems and create a more human-like interaction experience.

---

## Key Features

### Emotion Detection

* Uses VADER sentiment analysis
* Classifies text into:

  * Happy (Positive)
  * Frustrated (Negative)
  * Neutral
  * Surprised
  * Inquisitive
* Extracts intensity using compound sentiment score

---

### Emotion-Based Voice Modulation

Speech output is modified using:

* Rate (speed of speech)
* Volume (loudness)

Mapping logic:

* Happy → faster, louder
* Frustrated → slower, softer
* Neutral → default tone
* Surprised → faster with pauses
* Inquisitive → slightly faster with questioning tone

---

### Intensity Scaling

The strength of the emotion affects how much the voice parameters change.

* Mild sentiment → subtle modulation
* Strong sentiment → noticeable variation in rate and volume

---

### Text Enhancement (SSML-like Simulation)

To improve expressiveness:

* Adds pauses using punctuation
* Emphasizes key words
* Modifies sentence structure for better delivery

---

### Minimal Web Interface

* Text input field
* Generate button
* Emotion display
* Audio playback

---

### CLI Support

```bash id="x0z41n"
python cli.py "Your text here"
```

---

## Tech Stack

* Python
* FastAPI
* NLTK (VADER)
* pyttsx3 (offline TTS)
* HTML (minimal UI)

---

## Setup Instructions

### 1. Clone Repository

```bash id="p3l8if"
git clone <your-repo-link>
cd empathy-engine
```

---

### 2. Create Virtual Environment

```bash id="wz1r3z"
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash id="g9g6a8"
pip install -r requirements.txt
```

---

### 4. Run Application

```bash id="ptp5h3"
uvicorn main:app --reload
```

---

### 5. Open UI

```id="6d0k3l"
http://127.0.0.1:8000/
```

---

## API Usage

### Endpoint:

POST /speak

### Request:

```json id="9b6v7c"
{
  "text": "I am really excited about this!"
}
```

### Response:

```json id="b9v6c1"
{
  "emotion": "happy",
  "intensity": 0.82,
  "audio_file": "static/output.wav"
}
```

---

## Emotion to Voice Mapping

| Emotion     | Rate          | Volume  |
| ----------- | ------------- | ------- |
| Happy       | High          | High    |
| Frustrated  | Low           | Low     |
| Neutral     | Default       | Default |
| Surprised   | Very High     | Medium  |
| Inquisitive | Slightly High | Medium  |

---


## Example Outputs

| Input                    | Emotion     |
| ------------------------ | ----------- |
| "This is amazing!"       | Happy       |
| "This is not working..." | Frustrated  |
| "What just happened?"    | Inquisitive |

---


---

