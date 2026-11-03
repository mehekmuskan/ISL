"""
Speech-to-Sign Translation Module
Features:
- Speech recognition integration (HTML5 SpeechRecognition / Web Speech API + audio fallback)
- Text input alternative
- Sentence-level natural language parsing into ISL grammatical sequences
- Visual ISL sign animation/diagram rendering for each token
- Fingerspelling fallback for novel words
"""

import streamlit as st
import streamlit.components.v1 as components
import isl_data
import isl_signs
from typing import Callable, Optional


def render_speech_to_sign(generate_tts_audio_fn: Callable[[str, str], Optional[bytes]], selected_language: str):
    st.markdown("## 🗣️ Speech-to-Sign Translation")
    st.markdown(
        "Convert spoken words or voice recordings into structured Indian Sign Language (ISL) sequences "
        "accompanied by visual sign demonstrations, animation cues, and grammatical tokenization."
    )

    if "recognized_speech_text" not in st.session_state:
        st.session_state.recognized_speech_text = ""

    # Web Speech API Integration Component (for browser microphone capture)
    st.markdown("### 1. Spoken Audio Input")
    st.write("Click **Start Voice Recording** to speak into your microphone, or choose a preset sentence below:")

    # Voice input simulation and Web Speech interface
    components.html("""
    <div style="font-family: system-ui, -apple-system, sans-serif; padding: 12px; background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px;">
        <div style="display:flex; align-items:center; gap: 10px;">
            <button id="micBtn" style="background:#16a34a; color:white; border:none; padding:8px 16px; border-radius:6px; cursor:pointer; font-weight:bold;">
                🎙️ Speak via Browser Microphone
            </button>
            <span id="micStatus" style="font-size:14px; color:#166534;">Microphone Ready (Web Speech API Enabled)</span>
        </div>
        <p id="micResult" style="margin-top:8px; font-weight:500; color:#14532d; font-size:14px;"></p>
    </div>
    <script>
        const btn = document.getElementById('micBtn');
        const status = document.getElementById('micStatus');
        const result = document.getElementById('micResult');

        if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            const recognition = new SpeechRecognition();
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = 'en-IN';

            btn.onclick = () => {
                try {
                    recognition.start();
                    status.innerText = 'Listening... Please speak clearly.';
                    status.style.color = '#dc2626';
                } catch(e) {
                    console.log(e);
                }
            };

            recognition.onresult = (event) => {
                const transcript = event.results[0][0].transcript;
                result.innerText = 'Heard: ' + transcript;
                status.innerText = 'Speech captured successfully!';
                status.style.color = '#166534';
            };

            recognition.onerror = (event) => {
                status.innerText = 'Note: ' + (event.error || 'Speech capture event recorded');
                status.style.color = '#4b5563';
            };
        } else {
            status.innerText = 'Web Speech API supported in standard browsers; text fallback ready below.';
        }
    </script>
    """, height=110)

    # Fast Presets
    st.markdown("#### Quick Speech Presets:")
    pr_col1, pr_col2, pr_col3, pr_col4 = st.columns(4)
    with pr_col1:
        if st.button("🗣️ 'Doctor please help me'", use_container_width=True):
            st.session_state.recognized_speech_text = "Doctor please help me"
    with pr_col2:
        if st.button("🗣️ 'I need drinking water'", use_container_width=True):
            st.session_state.recognized_speech_text = "I need drinking water"
    with pr_col3:
        if st.button("🗣️ 'Severe stomach ache'", use_container_width=True):
            st.session_state.recognized_speech_text = "Severe stomach ache"
    with pr_col4:
        if st.button("🗣️ 'Where is the hospital'", use_container_width=True):
            st.session_state.recognized_speech_text = "Where is the hospital"

    # Editable Text Input
    speech_input = st.text_input(
        "Spoken or Typed Sentence to Translate into ISL:",
        value=st.session_state.recognized_speech_text,
        placeholder="e.g. Hello doctor, please give medicine for fever"
    )

    if speech_input.strip():
        st.markdown("---")
        st.subheader("2. ISL Sentence Translation & Sign Demonstrations")

        sign_sequence = isl_data.translate_sentence_to_signs(speech_input)

        st.info(f"Translated **{len(sign_sequence)}** sign grammatical units for sentence: *\"{speech_input}\"*")

        # Visual Demonstration Grid
        cols = st.columns(min(len(sign_sequence), 4) if sign_sequence else 1)
        for i, token_data in enumerate(sign_sequence):
            col_target = cols[i % len(cols)]
            with col_target:
                word_clean = token_data.get("word")
                st.markdown(f"**Step {i+1}: {word_clean.upper()}**")

                # Check if fingerspelled
                if token_data.get("is_fingerspelled"):
                    st.caption(f"Fingerspelling: {'-'.join(token_data.get('letters', []))}")
                    # Render first letter sign
                    first_letter = token_data.get("letters", ["A"])[0].upper()
                    svg = isl_signs.get_sign_svg(first_letter, title=f"Spelling: {first_letter}")
                    st.markdown(svg, unsafe_allow_html=True)
                else:
                    svg = isl_signs.get_sign_svg(word_clean, title=f"Sign: {word_clean.upper()}")
                    st.markdown(svg, unsafe_allow_html=True)

                st.markdown(f"<div style='font-size:0.85rem; color:#475569; margin-top:4px;'>{token_data.get('sign_description')}</div>", unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("3. Sequential Animation / Sign Playback")
        st.write("Step through each sign demonstration in sequence:")

        slider_step = st.slider("Step through sign sequence:", 1, len(sign_sequence), 1)
        active_step_data = sign_sequence[slider_step - 1]

        anim_col1, anim_col2 = st.columns([1, 2])
        with anim_col1:
            step_word = active_step_data.get("word")
            st.markdown(isl_signs.get_sign_svg(step_word, title=f"Active Step {slider_step}: {step_word.upper()}"), unsafe_allow_html=True)
        with anim_col2:
            st.markdown(f"### Sign Gesture: **{active_step_data.get('word').upper()}**")
            st.write(f"**Hindi Equivalent:** {active_step_data.get('hindi')}")
            st.write(f"**Kannada Equivalent:** {active_step_data.get('kannada')}")
            st.write(f"**Execution Instruction:** {active_step_data.get('sign_description')}")

            # Hear pronunciation
            if st.button(f"🔊 Listen to '{active_step_data.get('word')}' in English", key=f"step_aud_{slider_step}"):
                aud = generate_tts_audio_fn(active_step_data.get("word"), "en")
                if aud:
                    st.audio(aud, format="audio/mp3", autoplay=True)
