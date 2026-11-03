"""
Hospital Communication Module
Provides dedicated healthcare interface:
- 12 Clinical categories with quick filtering
- Emergency broadcast cards
- Visual pain assessment scale (0-10) with anatomical location selector
- Bi-directional Doctor <-> Patient communication builder
- Multi-language text & audio playback (English, Hindi, Kannada)
- Visual ISL sign sequences for every hospital phrase
"""

import streamlit as st
import isl_data
import isl_signs
from typing import Callable, Optional


def render_hospital_mode(generate_tts_audio_fn: Callable[[str, str], Optional[bytes]], selected_language: str):
    st.markdown("## 🏥 Dedicated Hospital Communication Mode")
    st.markdown(
        "Specially designed for deaf and hard-of-hearing patients, doctors, and nurses to communicate "
        "medical conditions, symptoms, and requirements without language barriers."
    )

    # Emergency Quick Action Bar
    with st.container():
        st.markdown("""
        <div class="emergency-card">
            <h3 style="color: #b91c1c; margin-top:0;">🚨 Rapid Emergency Patient Broadcast</h3>
            <p style="color: #7f1d1d; margin-bottom: 0.5rem;">
                One-tap priority communication for critical clinical situations.
            </p>
        </div>
        """, unsafe_allow_html=True)

        em_col1, em_col2, em_col3, em_col4 = st.columns(4)
        with em_col1:
            if st.button("🚨 Call Nurse Urgently", use_container_width=True, type="primary"):
                st.toast("🚨 Alert Sent to Nurse Station!", icon="🔔")
                st.error("Priority Call: Nurse assistance requested at bedside!")
                audio = generate_tts_audio_fn("Please call the nurse urgently!", "en")
                if audio:
                    st.audio(audio, format="audio/mp3", autoplay=True)
        with em_col2:
            if st.button("🫁 Breathing Difficulty", use_container_width=True):
                st.toast("🚨 Respiratory distress reported!", icon="🫁")
                st.error("Patient cannot breathe properly! Oxygen support needed.")
                audio = generate_tts_audio_fn("I cannot breathe properly. Oxygen needed.", "en")
                if audio:
                    st.audio(audio, format="audio/mp3", autoplay=True)
        with em_col3:
            if st.button("⚡ Severe Chest Pain", use_container_width=True):
                st.toast("🚨 Chest pain alert triggered!", icon="⚡")
                st.error("Severe chest pain reported! Immediate ECG / Doctor required.")
                audio = generate_tts_audio_fn("Severe chest pain! Please call a doctor immediately.", "en")
                if audio:
                    st.audio(audio, format="audio/mp3", autoplay=True)
        with em_col4:
            if st.button("💧 Water & Hydration", use_container_width=True):
                st.toast("Request sent: Water needed", icon="💧")
                st.info("Patient requests drinking water.")
                audio = generate_tts_audio_fn("Please give me drinking water.", "en")
                if audio:
                    st.audio(audio, format="audio/mp3", autoplay=True)

    st.markdown("---")

    # Tabs: 1. Clinical Category Phrases, 2. Interactive Pain Scale, 3. Custom Doctor-Patient Builder
    hosp_tabs = st.tabs(["📋 Clinical Phrases (115+)", "🎯 Visual Pain Scale & Body Map", "💬 Custom Doctor-Patient Builder"])

    # TAB 1: Clinical Categories & Search
    with hosp_tabs[0]:
        st.subheader("Clinical Phrases across 12 Healthcare Categories")

        col_search, col_cat = st.columns([2, 2])
        with col_search:
            search_query = st.text_input("🔍 Search clinical phrases or signs:", placeholder="e.g. oxygen, headache, urine, discharge")
        with col_cat:
            cat_keys = ["all"] + list(isl_data.CATEGORY_NAMES.keys())
            cat_display = ["🌟 All 12 Categories"] + [isl_data.CATEGORY_NAMES[k] for k in cat_keys[1:]]
            selected_cat_idx = st.selectbox(
                "Filter by Clinical Department:",
                range(len(cat_keys)),
                format_func=lambda i: cat_display[i]
            )
            selected_cat = cat_keys[selected_cat_idx]

        phrases = isl_data.search_hospital_phrases(search_query, selected_cat)
        st.caption(f"Showing **{len(phrases)}** hospital communication phrases.")

        # Display phrases in organized cards
        for phrase in phrases:
            urgency = phrase.get("urgency", "Low")
            urgency_class = "badge-urgent" if urgency == "High" else ("badge-medium" if urgency == "Medium" else "badge-low")
            box_class = "phrase-box high-urgency" if urgency == "High" else "phrase-box"

            with st.container():
                st.markdown(f"""
                <div class="{box_class}">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span class="badge {urgency_class}">{urgency} Urgency</span>
                        <span style="font-size:0.8rem; color:#64748b;">Category: {phrase.get('category').replace('_', ' ').title()}</span>
                    </div>
                    <h4 style="margin: 0.5rem 0 0.25rem 0; color:#0f172a;">{phrase.get('english')}</h4>
                    <p style="margin: 0; color:#334155; font-size:1.05rem;"><strong>हिंदी:</strong> {phrase.get('hindi')}</p>
                    <p style="margin: 0 0 0.5rem 0; color:#334155; font-size:1.05rem;"><strong>ಕನ್ನಡ:</strong> {phrase.get('kannada')}</p>
                    <div style="margin-top:0.5rem;">
                        <strong>ISL Sequence:</strong>
                        {' '.join([f'<span class=\"sign-token\">{token.strip()}</span>' for token in phrase.get('sign_sequence', '').split('+')])}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Interactive Action Bar for each phrase
                btn_col1, btn_col2, btn_col3, btn_col4 = st.columns([1, 1, 1, 2])
                with btn_col1:
                    if st.button("🔊 English", key=f"tts_en_{phrase['id']}", use_container_width=True):
                        audio = generate_tts_audio_fn(phrase.get("english"), "en")
                        if audio:
                            st.audio(audio, format="audio/mp3", autoplay=True)
                with btn_col2:
                    if st.button("🔊 हिंदी", key=f"tts_hi_{phrase['id']}", use_container_width=True):
                        audio = generate_tts_audio_fn(phrase.get("hindi"), "hi")
                        if audio:
                            st.audio(audio, format="audio/mp3", autoplay=True)
                with btn_col3:
                    if st.button("🔊 ಕನ್ನಡ", key=f"tts_kn_{phrase['id']}", use_container_width=True):
                        audio = generate_tts_audio_fn(phrase.get("kannada"), "kn")
                        if audio:
                            st.audio(audio, format="audio/mp3", autoplay=True)
                with btn_col4:
                    with st.expander("👁️ View Sign Visual"):
                        tokens = [t.strip().lower() for t in phrase.get("sign_sequence", "").split("+") if t.strip()]
                        cols = st.columns(min(len(tokens), 3) if tokens else 1)
                        for idx, tok in enumerate(tokens[:3]):
                            with cols[idx % len(cols)]:
                                svg_content = isl_signs.get_sign_svg(tok)
                                st.markdown(svg_content, unsafe_allow_html=True)
                                st.caption(f"Sign: **{tok.upper()}**")

    # TAB 2: Visual Pain Scale & Anatomical Body Region
    with hosp_tabs[1]:
        st.subheader("🎯 Visual Wong-Baker Style Pain Assessment (0 - 10)")
        st.write("Facilitates immediate non-verbal pain communication for deaf patients.")

        pain_level = st.slider("Select Pain Level (0 = No Pain, 10 = Worst Unbearable Pain):", 0, 10, 5)

        pain_descriptions = {
            0: ("😄 No Pain", "#10b981", "Patient is relaxed, comfortable, smiling."),
            1: ("🙂 Very Mild", "#34d399", "Noticeable pain but does not interfere with activities."),
            2: ("🙂 Mild Pain", "#38bdf8", "Noticeable discomfort, easily tolerated."),
            3: ("😐 Moderate Discomfort", "#60a5fa", "Pain is distracting but manageable."),
            4: ("😐 Annoying Pain", "#fbbf24", "Pain interferes somewhat with concentration."),
            5: ("😣 Distressing Pain", "#f59e0b", "Pain interrupts basic comfort and activities."),
            6: ("😣 Intense Pain", "#fb923c", "Significantly impacts posture and sleep."),
            7: ("😫 Severe Pain", "#ea580c", "Difficult to focus, breathing or movement hurt."),
            8: ("😫 Intense Agony", "#dc2626", "Patient in visible distress, clenching."),
            9: ("😭 Unbearable Pain", "#b91c1c", "Unable to speak or move comfortably."),
            10: ("😱 Maximum Pain Ever", "#7f1d1d", "Emergency immediate intervention needed.")
        }
        title, color, detail = pain_descriptions[pain_level]

        p_col1, p_col2 = st.columns([1, 2])
        with p_col1:
            st.markdown(f"""
            <div style="background: {color}; color: white; padding: 2rem; border-radius: 12px; text-align: center; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
                <h1 style="font-size: 3.5rem; margin:0; color:white;">{pain_level}</h1>
                <h3 style="color:white; margin: 0.5rem 0;">{title}</h3>
                <p style="margin:0; font-size: 0.95rem;">{detail}</p>
            </div>
            """, unsafe_allow_html=True)

            # Broadcast Pain Level
            if st.button("📢 Broadcast Pain Level to Medical Staff", use_container_width=True, type="primary"):
                msg = f"Patient reports pain level {pain_level} out of 10: {title}."
                st.success(f"Reported: {msg}")
                audio = generate_tts_audio_fn(msg, "en")
                if audio:
                    st.audio(audio, format="audio/mp3", autoplay=True)

        with p_col2:
            st.markdown("#### Select Anatomical Pain Area:")
            body_parts = [
                "Head / Temples 🧠", "Chest / Heart 🫀", "Stomach / Abdomen 🤰",
                "Lower Back / Spine 🦴", "Throat / Neck 🗣️", "Left Arm / Shoulder 💪",
                "Right Arm / Shoulder 💪", "Left Leg / Knee 🦵", "Right Leg / Knee 🦵",
                "Teeth / Jaw 🦷", "Eyes / Vision 👁️", "Full Body / All Over 🧍"
            ]
            selected_body_parts = st.multiselect("Pain is located at:", body_parts, default=["Chest / Heart 🫀"])

            st.markdown("#### Pain Characteristics:")
            pain_types = st.pills("Type of pain sensation:", ["Sharp / Stabbing 🗡️", "Dull Ache ⏳", "Throbbing / Pulsing 💓", "Burning / Tingling 🔥", "Cramping 🌀"], default="Sharp / Stabbing 🗡️")

            if st.button("Generate Pain Summary Report"):
                summary = f"Pain Level: {pain_level}/10 ({title}). Location: {', '.join(selected_body_parts)}. Sensation: {pain_types}."
                st.info(f"**Medical Summary:** {summary}")
                tts_audio = generate_tts_audio_fn(summary, "en")
                if tts_audio:
                    st.audio(tts_audio, format="audio/mp3", autoplay=True)

    # TAB 3: Bi-directional Doctor <-> Patient Builder
    with hosp_tabs[2]:
        st.subheader("💬 Doctor-Patient Bi-Directional Dialogue Builder")
        st.write("Construct messages quickly with instant ISL sign translation and multi-language audio.")

        role = st.radio("I am communicating as:", ["Patient (Deaf / Hard of Hearing)", "Doctor / Nurse (Healthcare Provider)"], horizontal=True)

        if "Patient" in role:
            preset_options = [
                "I am having trouble sleeping because of the pain.",
                "When will I be allowed to drink water?",
                "Can my family member visit me inside?",
                "The medicine makes me feel nauseous.",
                "I need help walking to the bathroom.",
                "My intravenous cannula needle is loose."
            ]
        else:
            preset_options = [
                "Please do not move while I check your vitals.",
                "Take this tablet with warm water now.",
                "Your test reports are good and improving.",
                "Are you allergic to penicillin or any drugs?",
                "We need to take a blood sample now.",
                "You will be discharged tomorrow morning."
            ]

        chosen_preset = st.selectbox("Select standard clinical phrase:", ["-- Select or Type Custom --"] + preset_options)
        custom_input = st.text_input("Or type custom medical message:", value="" if chosen_preset.startswith("--") else chosen_preset)

        if custom_input.strip():
            st.markdown("#### Translation & ISL Sign Representation:")
            sign_seq = isl_data.translate_sentence_to_signs(custom_input)

            # Display visual signs
            if sign_seq:
                st.markdown("**Sequence of ISL Signs:**")
                sign_cols = st.columns(min(len(sign_seq), 4))
                for idx, item in enumerate(sign_seq[:4]):
                    with sign_cols[idx % 4]:
                        svg = isl_signs.get_sign_svg(item.get("word"))
                        st.markdown(svg, unsafe_allow_html=True)
                        st.caption(f"**{item.get('word').upper()}**")
                        st.caption(f"{item.get('sign_description')[:60]}...")

            st.markdown("---")
            st.markdown("#### Spoken Audio Feedback:")
            aud_col1, aud_col2, aud_col3 = st.columns(3)
            with aud_col1:
                if st.button("🔊 Play in English", key="bld_en"):
                    aud = generate_tts_audio_fn(custom_input, "en")
                    if aud:
                        st.audio(aud, format="audio/mp3", autoplay=True)
            with aud_col2:
                if st.button("🔊 Play in Hindi (हिंदी)", key="bld_hi"):
                    # Check if preset has hindi mapping
                    matched = isl_data.search_hospital_phrases(custom_input)
                    hi_text = matched[0]["hindi"] if matched else custom_input
                    aud = generate_tts_audio_fn(hi_text, "hi")
                    if aud:
                        st.audio(aud, format="audio/mp3", autoplay=True)
            with aud_col3:
                if st.button("🔊 Play in Kannada (ಕನ್ನಡ)", key="bld_kn"):
                    matched = isl_data.search_hospital_phrases(custom_input)
                    kn_text = matched[0]["kannada"] if matched else custom_input
                    aud = generate_tts_audio_fn(kn_text, "kn")
                    if aud:
                        st.audio(aud, format="audio/mp3", autoplay=True)
