# Empathy Engine

## Overview

The Empathy Engine is an emotion-aware text-to-speech system that enhances traditional voice output by making it more expressive and human-like. It takes text as input, analyzes the underlying sentiment using VADER, and classifies it into emotions such as happy, frustrated, neutral, surprised, and inquisitive.

Based on the detected emotion and its intensity, the system dynamically adjusts speech parameters like rate (speed) and volume (loudness). It also applies text preprocessing techniques such as adding pauses and emphasizing key words to improve delivery.

The result is a more natural and engaging audio output compared to standard monotonic TTS systems.

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

Design Choices and Emotion-to-Voice Mapping
1. Emotion Detection

The system uses VADER sentiment analysis to extract a compound score between -1 and +1. This score is used to determine both:

Emotion category (happy, frustrated, neutral, etc.)
Intensity of the emotion
2. Emotion Classification Logic
Positive score → Happy
Negative score → Frustrated
Near zero → Neutral
High magnitude → Surprised
Presence of question mark → Inquisitive

This allows the system to go beyond basic sentiment and capture more nuanced emotional states.

3. Voice Parameter Modulation

The system modifies two main parameters:

Rate (speech speed)
Volume (loudness)

Mapping:

Happy:
Higher rate
Higher volume
→ Creates energetic and engaging tone
Frustrated:
Lower rate
Lower volume
→ Produces slower, heavier speech
Neutral:
Default rate and volume
→ Maintains standard delivery
Surprised:
Very high rate
Medium volume
→ Adds urgency and variation
Inquisitive:
Slightly higher rate
Medium volume
→ Creates a questioning tone
4. Intensity Scaling

The compound sentiment score controls how strongly the parameters are adjusted.

Example:

Low score (0.2) → small changes
High score (0.9) → large changes

This ensures emotion is continuous rather than binary.

5. Text Enhancement (SSML-like Simulation)

Since pyttsx3 has limited emotional control, the system enhances text before speech generation:

Adds pauses using punctuation (e.g., "..." )
Emphasizes important words
Modifies sentence structure

This improves expressiveness even with a basic TTS engine.

6. Why This Approach
pyttsx3 allows offline execution and fast prototyping
VADER is lightweight and effective for short text
Combining parameter modulation with text enhancement compensates for TTS limitations

This design balances simplicity, performance, and expressive output.

---

