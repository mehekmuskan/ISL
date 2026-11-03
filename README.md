# ISL Connect – Indian Sign Language Communication & Learning Platform

ISL Connect is an all-in-one web-based communication and interactive learning platform designed to bridge the gap between deaf or hard-of-hearing individuals and people who do not know Indian Sign Language (ISL), with dedicated focus on healthcare and hospital environments.

---

## 🌟 Key Features

1. **🏥 Dedicated Hospital Communication Mode**:
   - 115+ clinical communication phrases categorized across 12 hospital wards.
   - 1-tap Rapid Emergency patient broadcast buttons.
   - Interactive 0–10 visual pain scale (Wong-Baker style) with anatomical body area selector.
   - Bi-directional Doctor-to-Patient and Patient-to-Doctor phrase builder.
   - Instant speech audio playback in English, Hindi, and Kannada.

2. **📹 Sign-to-Text Recognition**:
   - Continuous camera video frame capture and gesture temporal buffering.
   - Gesture confidence estimation.
   - Real-time sentence construction and word accumulator.
   - Multilingual voice synthesis for generated sentences.

3. **🗣️ Speech-to-Sign Translation**:
   - Web Speech API integration for microphone voice input and text fallback.
   - Parses conversational speech into grammatical ISL sequence tokens.
   - Generates visual SVG sign illustrations with handshape configurations and motion arrows.
   - Sequential step-by-step sign playback.

4. **🔊 Multilingual Text-to-Speech (TTS)**:
   - Voice synthesis in **English**, **Hindi (हिंदी)**, and **Kannada (ಕನ್ನಡ)** using gTTS.
   - Built-in audio player and downloadable MP3 audio files.
   - Hospital and everyday conversational presets.

5. **🎓 Learn ISL Interactive Studio**:
   - Complete ISL Alphabet (A–Z) fingerspelling cards with handshape illustrations.
   - ISL Numbers (0–10) and basic gestures.
   - Healthcare and everyday communication vocabulary.
   - Multi-question interactive quiz with explanations, scoring, and progress tracking.

---

## 📁 Project Architecture

```
isl-connect/
├── app.py                      # Main Streamlit web application & navigation
├── hospital_mode.py            # Dedicated hospital interface & clinical tools
├── sign_to_text.py             # Continuous camera gesture recognition & sentence builder
├── speech_to_sign.py           # Speech recognition & visual sign sequence translator
├── text_to_speech.py           # Multilingual voice synthesis (English, Hindi, Kannada)
├── learn_isl.py                # Interactive ISL studio & assessment quizzes
├── isl_data.py                 # Data loader, phrase search, and sentence tokenizers
├── isl_signs.py                # Visual SVG sign generator for alphabets and medical signs
├── speech_to_sign_vocab.json   # 206 vocabulary entries across 10 categories
├── hospital_phrases.json       # 115 hospital phrases across 12 clinical categories
├── generate_datasets.py        # Dataset generation utility
├── requirements.txt            # Python dependencies
├── .streamlit/config.toml      # Streamlit UI configuration and styling
└── tests/
    └── test_dataset.py         # Pytest verification suite
```

---

## 🚀 Getting Started

### Installation
```bash
pip install -r requirements.txt
```

### Running the App
```bash
streamlit run app.py
```

### Running Tests
```bash
python3 -m pytest -v
```
