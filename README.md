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

## Working of the Project

The Empathy Engine follows a structured pipeline that transforms input text into emotionally expressive speech. The process consists of four main stages:

---

### 1. Text Input

The system accepts user input through:

* A **web interface** (textarea input), or
* A **CLI command**

This text acts as the raw input for emotion analysis and speech generation.

---

### 2. Emotion Detection

The input text is processed using **VADER sentiment analysis**, which computes a **compound score** ranging from -1 (very negative) to +1 (very positive).

Based on this score and simple rules:

* The system determines the **emotion category** (happy, frustrated, neutral, surprised, inquisitive)
* It also extracts the **intensity** of the emotion

This step converts raw text into structured emotional information.

---

### 3. Text Enhancement (Preprocessing)

Before generating speech, the text is modified to improve expressiveness. Since the TTS engine has limited emotional capability, this step simulates SSML-like behavior.

Enhancements include:

* Adding pauses using punctuation (e.g., `"..."`)
* Emphasizing important words
* Adjusting sentence structure based on emotion

This prepares the text in a way that makes the output sound more natural.

---

### 4. Emotion-to-Voice Mapping

The detected emotion and its intensity are mapped to speech parameters:

* **Rate (speed of speech)**
* **Volume (loudness)**

Examples:

* Happy → faster and louder speech
* Frustrated → slower and softer speech
* Neutral → default parameters

The **intensity score** controls how strongly these parameters are adjusted.

---

### 5. Speech Generation

The processed text and computed voice parameters are passed to the TTS engine (`pyttsx3`).

The engine:

* Applies the configured rate and volume
* Converts text into speech
* Saves the output as a `.wav` audio file

---

### 6. Output Delivery

The generated audio is:

* Saved in the `static/` folder
* Played in the web interface using an audio player
* Or returned via API/CLI

---

## Summary Flow

Input Text
→ Emotion Detection
→ Text Enhancement
→ Parameter Mapping
→ Speech Generation
→ Audio Output

---

This pipeline ensures that the system not only speaks text but delivers it with **context-aware emotional expression**, improving the overall user experience.


## Design Choices and Emotion-to-Voice Mapping

### 1. Emotion Detection

The system uses **VADER sentiment analysis** to extract a compound score between **-1 and +1**. This score is used to determine:

* Emotion category (happy, frustrated, neutral, etc.)
* Intensity of the emotion

---

### 2. Emotion Classification Logic

* Positive score → **Happy**
* Negative score → **Frustrated**
* Near zero → **Neutral**
* High magnitude → **Surprised**
* Presence of question mark → **Inquisitive**

This approach allows the system to go beyond basic sentiment and capture more nuanced emotional states.

---

### 3. Voice Parameter Modulation

The system modifies two main parameters:

* **Rate** (speech speed)
* **Volume** (loudness)

#### Mapping Logic

**Happy**

* Higher rate
* Higher volume
  → Creates an energetic and engaging tone

**Frustrated**

* Lower rate
* Lower volume
  → Produces slower, heavier speech

**Neutral**

* Default rate and volume
  → Maintains standard delivery

**Surprised**

* Very high rate
* Medium volume
  → Adds urgency and variation

**Inquisitive**

* Slightly higher rate
* Medium volume
  → Creates a questioning tone

---

### 4. Intensity Scaling

The compound sentiment score controls how strongly the parameters are adjusted.

* Low score (0.2) → Small changes
* High score (0.9) → Large changes

This ensures emotion is **continuous rather than binary**, making the output more natural.

---

### 5. Text Enhancement (SSML-like Simulation)

Since `pyttsx3` has limited emotional control, the system enhances text before speech generation:

* Adds pauses using punctuation (e.g., `"..."`)
* Emphasizes important words
* Modifies sentence structure for better delivery

This significantly improves expressiveness even with a basic TTS engine.

---

### 6. Why This Approach

* `pyttsx3` enables offline execution and fast prototyping
* VADER is lightweight and effective for short conversational text
* Combining parameter modulation with text enhancement compensates for TTS limitations

This design balances **simplicity, performance, and expressive output**.
