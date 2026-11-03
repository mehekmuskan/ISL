"""
Text-to-Speech (TTS) Module
Features:
- Multilingual voice synthesis: English, Hindi (हिंदी), and Kannada (ಕನ್ನಡ)
- Fast preset medical & conversational phrases
- Clear audio playback player
- High reliability via gTTS
"""

import streamlit as st
import isl_data
from typing import Callable, Optional


def render_text_to_speech(generate_tts_audio_fn: Callable[[str, str], Optional[bytes]], selected_language: str):
    st.markdown("## 🔊 Multilingual Text-to-Speech (TTS)")
    st.markdown(
        "Convert typed text or medical instructions into natural spoken audio in "
        "**English**, **Hindi (हिंदी)**, and **Kannada (ಕನ್ನಡ)**."
    )

    col_input, col_presets = st.columns([1.5, 1])

    with col_presets:
        st.subheader("Quick Hospital Presets:")
        preset_lang = st.radio("Preset Language:", ["English", "Hindi (हिंदी)", "Kannada (ಕನ್ನಡ)"], horizontal=True)

        if "English" in preset_lang:
            preset_options = [
                "Please sit down and rest here.",
                "Your doctor is on their way.",
                "Take this medicine after your meal.",
                "Where is the emergency department?",
                "Do you feel any pain in your chest?"
            ]
        elif "Hindi" in preset_lang:
            preset_options = [
                "कृपया यहाँ बैठें और आराम करें।",
                "डॉक्टर जल्द ही आपकी जांच करेंगे।",
                "यह दवा खाना खाने के बाद लें।",
                "आपातकालीन वार्ड किस तरफ है?",
                "क्या आपको सीने में कोई दर्द महसूस हो रहा है?"
            ]
        else:
            preset_options = [
                "ದಯವಿಟ್ಟು ಇಲ್ಲಿ ಕುಳಿತುಕೊಂಡು ವಿಶ್ರಾಂತಿ ಪಡೆಯಿರಿ.",
                "ವೈದ್ಯರು ಶೀಘ್ರದಲ್ಲೇ ನಿಮ್ಮನ್ನು ಪರೀಕ್ಷಿಸುತ್ತಾರೆ.",
                "ಈ ಔಷಧಿಯನ್ನು ಊಟದ ನಂತರ ತೆಗೆದುಕೊಳ್ಳಿ.",
                "ತುರ್ತು ಚಿಕಿತ್ಸಾ ವಿಭಾಗ ಎಲ್ಲಿದೆ?",
                "ನಿಮ್ಮ ಎದೆಯಲ್ಲಿ ಯಾವುದೇ ನೋವು ಕಾಣಿಸಿಕೊಂಡಿದೆಯೇ?"
            ]

        chosen_phrase = st.selectbox("Select a preset:", ["-- Type or Select Preset --"] + preset_options)

    with col_input:
        st.subheader("Type Custom Message:")
        default_val = "" if chosen_phrase.startswith("--") else chosen_phrase
        user_text = st.text_area(
            "Enter text to generate spoken voice:",
            value=default_val,
            height=130,
            placeholder="Type anything in English, Hindi, or Kannada..."
        )

        target_lang = st.selectbox(
            "Voice Accent & Language:",
            ["English (en)", "Hindi / हिंदी (hi)", "Kannada / ಕನ್ನಡ (kn)"],
            index=0 if "English" in preset_lang else (1 if "Hindi" in preset_lang else 2)
        )
        lang_code = "en" if "English" in target_lang else ("hi" if "Hindi" in target_lang else "kn")

        if st.button("🔊 Generate & Play Spoken Audio", type="primary", use_container_width=True):
            if not user_text.strip():
                st.warning("Please type or select a message first.")
            else:
                with st.spinner("Synthesizing audio..."):
                    audio_bytes = generate_tts_audio_fn(user_text, lang_code)
                    if audio_bytes:
                        st.success(f"Audio synthesized successfully in {target_lang}!")
                        st.audio(audio_bytes, format="audio/mp3", autoplay=True)

                        # Download button
                        st.download_button(
                            label="⬇️ Download Voice MP3",
                            data=audio_bytes,
                            file_name=f"isl_connect_speech_{lang_code}.mp3",
                            mime="audio/mp3"
                        )
                    else:
                        st.error("Audio generation failed. Please check network connection.")

    st.markdown("---")
    st.markdown("### 🌐 Multilingual Voice Demonstration:")
    st.write("Hear the same greeting spoken across all 3 supported languages:")

    demo_cols = st.columns(3)
    with demo_cols[0]:
        st.markdown("**English:** *Hello, welcome to ISL Connect.*")
        if st.button("🔊 Play English Greeting", key="g_en"):
            aud = generate_tts_audio_fn("Hello, welcome to ISL Connect.", "en")
            if aud:
                st.audio(aud, format="audio/mp3", autoplay=True)
    with demo_cols[1]:
        st.markdown("**Hindi:** *नमस्ते, आईएसएल कनेक्ट में आपका स्वागत है।*")
        if st.button("🔊 Play Hindi Greeting", key="g_hi"):
            aud = generate_tts_audio_fn("नमस्ते, आईएसएल कनेक्ट में आपका स्वागत है।", "hi")
            if aud:
                st.audio(aud, format="audio/mp3", autoplay=True)
    with demo_cols[2]:
        st.markdown("**Kannada:** *ನಮಸ್ಕಾರ, ಐಎಸ್ಎಲ್ ಕನೆಕ್ಟ್‌ಗೆ ಸುಸ್ವಾಗತ.*")
        if st.button("🔊 Play Kannada Greeting", key="g_kn"):
            aud = generate_tts_audio_fn("ನಮಸ್ಕಾರ, ಐಎಸ್ಎಲ್ ಕನೆಕ್ಟ್‌ಗೆ ಸುಸ್ವಾಗತ.", "kn")
            if aud:
                st.audio(aud, format="audio/mp3", autoplay=True)
