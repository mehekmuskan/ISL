"""
ISL Connect: Indian Sign Language Communication & Learning Platform
Main Application Script
"""

import base64
import html
import io
import os
import random
import time
from typing import Dict, List, Optional

import streamlit as st
from gtts import gTTS

import isl_data
import isl_signs

# Page Configuration
st.set_page_config(
    page_title="ISL Connect - Indian Sign Language Platform",
    page_icon="🤟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Healthcare & Modern Design)
st.markdown("""
<style>
    /* Global Styling */
    .main {
        background-color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    /* Header branding */
    .app-header {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        color: white;
        padding: 1.5rem 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .app-header h1 {
        color: white !important;
        margin: 0;
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.025em;
    }
    .app-header p {
        color: #e0f2fe;
        margin-top: 0.5rem;
        font-size: 1.05rem;
        margin-bottom: 0;
    }

    /* Cards & Containers */
    .feature-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 1.25rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .feature-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
    }

    .emergency-card {
        background: #fef2f2;
        border: 2px solid #ef4444;
        border-radius: 12px;
        padding: 1.25rem;
        margin-bottom: 1rem;
    }

    /* Hospital Phrase Box */
    .phrase-box {
        background: white;
        border: 1px solid #cbd5e1;
        border-left: 5px solid #0284c7;
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin-bottom: 0.75rem;
    }
    .phrase-box.high-urgency {
        border-left: 5px solid #ef4444;
        background: #fff5f5;
    }

    /* Badges */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.6rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
    }
    .badge-urgent { background: #fee2e2; color: #dc2626; }
    .badge-medium { background: #fef3c7; color: #d97706; }
    .badge-low { background: #e0f2fe; color: #0284c7; }

    /* Sign Sequence Tag */
    .sign-token {
        display: inline-block;
        background: #e0f2fe;
        color: #0369a1;
        padding: 0.2rem 0.5rem;
        border-radius: 6px;
        margin: 2px 4px;
        font-weight: 600;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if "language" not in st.session_state:
    st.session_state.language = "English"
if "accumulated_words" not in st.session_state:
    st.session_state.accumulated_words = []
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
if "quiz_answered" not in st.session_state:
    st.session_state.quiz_answered = False
if "tts_cache" not in st.session_state:
    st.session_state.tts_cache = {}


def generate_tts_audio(text: str, lang_code: str = "en") -> Optional[bytes]:
    """Generates audio bytes using gTTS with caching."""
    if not text.strip():
        return None
    cache_key = f"{lang_code}_{text}"
    if cache_key in st.session_state.tts_cache:
        return st.session_state.tts_cache[cache_key]
    try:
        tts = gTTS(text=text, lang=lang_code, slow=False)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        audio_bytes = fp.read()
        st.session_state.tts_cache[cache_key] = audio_bytes
        return audio_bytes
    except Exception as e:
        st.warning(f"Audio generation notice: {e}")
        return None


def get_lang_code(language_name: str) -> str:
    """Returns ISO 639-1 code for selected language."""
    mapping = {
        "English": "en",
        "Hindi (हिंदी)": "hi",
        "Kannada (ಕನ್ನಡ)": "kn"
    }
    return mapping.get(language_name, "en")


# Navigation Sidebar
with st.sidebar:
    st.image("https://api.iconify.design/solar:hand-shake-bold.svg?color=%230284c7", width=60)
    st.title("ISL Connect")
    st.caption("Empowering Deaf & Hard of Hearing Communication")

    st.markdown("---")

    selected_language = st.selectbox(
        "🌐 Choose Interface Language",
        ["English", "Hindi (हिंदी)", "Kannada (ಕನ್ನಡ)"],
        index=["English", "Hindi (हिंदी)", "Kannada (ಕನ್ನಡ)"].index(
            st.session_state.language if st.session_state.language in ["English", "Hindi (हिंदी)", "Kannada (ಕನ್ನಡ)"] else "English"
        )
    )
    st.session_state.language = selected_language

    st.markdown("---")
    st.subheader("📌 Navigation")

    nav_options = [
        "🏠 Home & Overview",
        "🏥 Hospital Communication Mode",
        "📹 Sign-to-Text Recognition",
        "🗣️ Speech-to-Sign Translation",
        "🔊 Text-to-Speech (TTS)",
        "🎓 Learn ISL Studio"
    ]

    chosen_page = st.radio("Go to:", nav_options, index=0)

    st.markdown("---")
    st.markdown("""
    **Quick Emergency Help**
    - 🚨 *Call Nurse*: Tap in Hospital Mode
    - 🏥 *Emergency*: 108 / 112
    """)
    st.caption("Version 2.0 • Designed for Hospital & Everyday Accessibility")


# Render App Banner Header
lang_labels = {
    "English": ("ISL Connect – Indian Sign Language Platform", "Bridging the gap between deaf individuals, healthcare workers, and everyday society."),
    "Hindi (हिंदी)": ("आईएसएल कनेक्ट – भारतीय सांकेतिक भाषा मंच", "बधिर व्यक्तियों, स्वास्थ्य कर्मियों और समाज के बीच की दूरी को मिटाना।"),
    "Kannada (ಕನ್ನಡ)": ("ಐಎಸ್ಎಲ್ ಕನೆಕ್ಟ್ – ಭಾರತೀಯ ಸಂಕೇತ ಭಾಷಾ ಸಂವಹನ ವೇದಿಕೆ", "ಕಿವುಡ ವ್ಯಕ್ತಿಗಳು, ಆಸ್ಪತ್ರೆಯ ವೈದ್ಯರು ಮತ್ತು ಸಾರ್ವಜನಿಕರ ನಡುವೆ ಸಂವಹನ ಸೇತುವೆ.")
}
hdr_title, hdr_sub = lang_labels.get(selected_language, lang_labels["English"])

st.markdown(f"""
<div class="app-header">
    <h1>🤟 {hdr_title}</h1>
    <p>{hdr_sub}</p>
</div>
""", unsafe_allow_html=True)

# Import module views
import hospital_mode
import sign_to_text
import speech_to_sign
import text_to_speech
import learn_isl

# Page Routing
if "Home" in chosen_page:
    st.markdown("## 🌟 Welcome to ISL Connect")
    st.markdown("""
    ISL Connect is an all-in-one accessible communication ecosystem designed to empower
    deaf and hard-of-hearing individuals, particularly within healthcare and hospital environments.
    """)

    # Feature Metrics
    vocab_data = isl_data.load_vocabulary()
    hosp_data = isl_data.load_hospital_phrases()

    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    with m_col1:
        st.metric("ISL Vocabulary Words", f"{vocab_data.get('total_entries', 206)}+", "10 Categories")
    with m_col2:
        st.metric("Hospital Phrases", f"{hosp_data.get('total_phrases', 115)}+", "12 Clinical Wards")
    with m_col3:
        st.metric("Supported Languages", "3", "English, हिंदी, ಕನ್ನಡ")
    with m_col4:
        st.metric("Recognition Modes", "Continuous", "Video & Speech")

    st.markdown("---")
    st.subheader("🚀 Platform Modules & Quick Access")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="feature-card">
            <h3>🏥 Hospital Communication Mode</h3>
            <p>Dedicated medical interface containing emergency communication, 115+ clinical phrases across 12 wards, visual 0-10 pain scale, and doctor-patient dialogue tools.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Hospital Mode ➔", use_container_width=True, type="primary"):
            st.info("Please select '🏥 Hospital Communication Mode' in the sidebar navigation.")

        st.markdown("""
        <div class="feature-card">
            <h3>📹 Sign-to-Text Recognition</h3>
            <p>Continuous video capture and gesture recognition that accumulates individual signs into meaningful, grammatically complete spoken sentences.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Sign Recognition ➔", use_container_width=True):
            st.info("Please select '📹 Sign-to-Text Recognition' in the sidebar navigation.")

    with c2:
        st.markdown("""
        <div class="feature-card">
            <h3>🗣️ Speech-to-Sign Translation</h3>
            <p>Converts spoken medical instructions and questions into structured Indian Sign Language visual sequences with high-resolution demonstrations.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Speech Translation ➔", use_container_width=True):
            st.info("Please select '🗣️ Speech-to-Sign Translation' in the sidebar navigation.")

        st.markdown("""
        <div class="feature-card">
            <h3>🎓 Learn ISL Studio</h3>
            <p>Interactive learning environment with fingerspelling alphabet A-Z, numbers, daily healthcare gestures, and interactive quizzes.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Learn ISL ➔", use_container_width=True):
            st.info("Please select '🎓 Learn ISL Studio' in the sidebar navigation.")

elif "Hospital" in chosen_page:
    hospital_mode.render_hospital_mode(generate_tts_audio, selected_language)

elif "Sign-to-Text" in chosen_page:
    sign_to_text.render_sign_to_text(generate_tts_audio, selected_language)

elif "Speech-to-Sign" in chosen_page:
    speech_to_sign.render_speech_to_sign(generate_tts_audio, selected_language)

elif "Text-to-Speech" in chosen_page:
    text_to_speech.render_text_to_speech(generate_tts_audio, selected_language)

elif "Learn ISL" in chosen_page:
    learn_isl.render_learn_isl(generate_tts_audio, selected_language)
