"""
Learn ISL Interactive Studio Module
Features:
- ISL Alphabet (A-Z) learning cards with visual SVG illustrations
- Numbers & basic gestures
- Everyday expressions with bilingual translations
- Interactive Multi-question Quiz with score tracking and explanations
- Progress tracking indicators
"""

import streamlit as st
import isl_data
import isl_signs
from typing import Callable, Optional

# Interactive Quiz Questions Database
QUIZ_QUESTIONS = [
    {
        "question": "Which gesture represents the ISL sign for 'DOCTOR'?",
        "options": [
            "Tapping the inside of the wrist with bent fingers to check pulse",
            "Waving an open hand next to the forehead",
            "Rubbing both fists in a circular motion",
            "Snapping fingers twice in the air"
        ],
        "answer_idx": 0,
        "explanation": "In Indian Sign Language, the sign for DOCTOR involves bent fingers (often M-shape) tapping the inner wrist checking radial pulse."
    },
    {
        "question": "What is the correct ISL handshape for the letter 'L'?",
        "options": [
            "A closed fist with thumb across fingers",
            "Index finger upright and thumb extended at a 90-degree right angle",
            "Index and middle fingers crossed over each other",
            "Three fingers held upright forming a W"
        ],
        "answer_idx": 1,
        "explanation": "The letter 'L' in ISL (and many sign systems) is formed by extending the index finger vertically and thumb horizontally at a 90-degree angle."
    },
    {
        "question": "How is the sign for 'WATER' typically executed in ISL?",
        "options": [
            "Flat open palm brushes across chest",
            "W-handshape index finger tapping the chin twice",
            "Two hands interlocking pinky fingers",
            "Index finger pointing directly at the ear"
        ],
        "answer_idx": 1,
        "explanation": "WATER is signed with a W-handshape where the index finger gently taps the chin twice."
    },
    {
        "question": "How is the sign for 'HELP' performed in ISL?",
        "options": [
            "Right closed fist with thumb up resting on a flat left palm, raised upward together",
            "Waving goodbye with both hands",
            "Covering eyes with fingers",
            "Holding index fingers to temples"
        ],
        "answer_idx": 0,
        "explanation": "The sign for HELP uses a supportive gesture: the dominant fist rests on the open non-dominant palm, and both hands are lifted upward together."
    },
    {
        "question": "When signing 'PAIN' in ISL, what movement is accompanied with facial expression?",
        "options": [
            "Fingers waving like fluttering butterflies with a laugh",
            "Both index fingers pointing towards each other and twisting toward the pain location with a pained grimace",
            "Clapping hands together above the head",
            "Thumb and pinky forming a telephone shape"
        ],
        "answer_idx": 1,
        "explanation": "PAIN is signed by pointing both index fingers toward each other and twisting them near the affected area, accompanied by a grimacing facial expression."
    },
    {
        "question": "Which letter is signed by crossing the index and middle fingers?",
        "options": [
            "Letter R",
            "Letter B",
            "Letter T",
            "Letter O"
        ],
        "answer_idx": 0,
        "explanation": "Letter 'R' in sign language is made by crossing the middle finger over the index finger ('fingers crossed')."
    },
    {
        "question": "What does a circular rubbing motion of a closed fist over the heart/chest indicate?",
        "options": [
            "SORRY / Apology",
            "HUNGRY",
            "STOP",
            "FINISH"
        ],
        "answer_idx": 0,
        "explanation": "Circular rubbing on the chest over the heart with a closed fist represents SORRY (apology and remorse)."
    },
    {
        "question": "How do you sign the letter 'I' in the alphabet?",
        "options": [
            "Closed fist with pinky finger pointing straight up",
            "Flat four fingers upright",
            "Fist with thumb resting beside index",
            "Index and middle spread in a V"
        ],
        "answer_idx": 0,
        "explanation": "The letter 'I' is signed with a closed fist where only the pinky (little finger) is extended straight up."
    }
]


def render_learn_isl(generate_tts_audio_fn: Callable[[str, str], Optional[bytes]], selected_language: str):
    st.markdown("## 🎓 Learn Indian Sign Language (ISL) Interactive Studio")
    st.markdown(
        "Interactive learning modules designed for beginners, nurses, doctors, and students to master "
        "ISL alphabet, numbers, healthcare vocabulary, and test knowledge through quizzes."
    )

    learn_tabs = st.tabs(["🔤 ISL Alphabet (A–Z)", "🔢 Numbers (0–9)", "🏥 Common Signs & Words", "🎯 Interactive Quiz & Assessment"])

    # TAB 1: ISL Alphabet (A-Z)
    with learn_tabs[0]:
        st.subheader("Indian Sign Language Fingerspelling Alphabet (A–Z)")
        st.write("Click on any letter card to inspect handshape geometry and sign details:")

        alphabet_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        selected_letter = st.select_slider("Select Alphabet Letter:", options=alphabet_letters, value="A")

        card_col1, card_col2 = st.columns([1, 1.5])
        with card_col1:
            svg = isl_signs.get_sign_svg(selected_letter)
            st.markdown(svg, unsafe_allow_html=True)
        with card_col2:
            st.markdown(f"### Letter: **{selected_letter}**")
            # Lookup description from vocab if available
            sign_info = isl_data.find_sign_for_word(selected_letter.lower())
            desc = sign_info.get("sign_description") if sign_info else "Clear handshape configuration."
            hi = sign_info.get("hindi") if sign_info else selected_letter
            kn = sign_info.get("kannada") if sign_info else selected_letter

            st.write(f"**Hindi Pronunciation:** {hi}")
            st.write(f"**Kannada Pronunciation:** {kn}")
            st.write(f"**Handshape Guide:** {desc}")

            if st.button(f"🔊 Pronounce Letter '{selected_letter}'", key=f"aud_let_{selected_letter}"):
                aud = generate_tts_audio_fn(f"Letter {selected_letter}", "en")
                if aud:
                    st.audio(aud, format="audio/mp3", autoplay=True)

        st.markdown("---")
        st.markdown("#### Complete Visual Alphabet Grid:")
        # Render alphabet cards in rows of 6
        cols = st.columns(6)
        for idx, let in enumerate(alphabet_letters):
            with cols[idx % 6]:
                mini_svg = isl_signs.get_sign_svg(let)
                st.markdown(mini_svg, unsafe_allow_html=True)
                st.caption(f"**Letter {let}**")

    # TAB 2: Numbers (0-9)
    with learn_tabs[1]:
        st.subheader("ISL Numbers (0 – 10)")
        num_items = [
            ("0 (Zero)", "शून्य", "ಶೂನ್ಯ", "Curled fingers forming an 'O' oval.", "O"),
            ("1 (One)", "एक", "ಒಂದು", "Index finger upright, others folded into fist.", "1"),
            ("2 (Two)", "दो", "ಎರಡು", "Index and middle fingers held upright in V shape.", "V"),
            ("3 (Three)", "तीन", "ಮೂರು", "Thumb, index, and middle fingers extended.", "W"),
            ("4 (Four)", "चार", "ನಾಲ್ಕು", "Four fingers upright with thumb folded across palm.", "B"),
            ("5 (Five)", "पाँच", "ಐದು", "All five fingers spread wide open.", "5"),
            ("6 (Six)", "छह", "ಆರು", "Thumb touches pinky, other three fingers upright.", "F"),
            ("7 (Seven)", "सात", "ಏಳು", "Thumb touches ring finger, other fingers upright.", "7"),
            ("8 (Eight)", "आठ", "ಎಂಟು", "Thumb touches middle finger.", "8"),
            ("9 (Nine)", "नौ", "ಒಂಬತ್ತು", "Thumb touches index finger tip forming circle.", "9"),
            ("10 (Ten)", "दस", "ಹತ್ತು", "Both 5-hands flashed or thumb upright shaking gently.", "10")
        ]

        num_cols = st.columns(3)
        for i, (name, hi, kn, desc, sign_key) in enumerate(num_items):
            with num_cols[i % 3]:
                st.markdown(f"""
                <div class="feature-card">
                    <h4 style="margin-top:0; color:#0284c7;">{name}</h4>
                    <p style="margin:2px 0;"><strong>Hindi:</strong> {hi}</p>
                    <p style="margin:2px 0;"><strong>Kannada:</strong> {kn}</p>
                    <p style="color:#64748b; font-size:0.9rem;">{desc}</p>
                </div>
                """, unsafe_allow_html=True)
                svg_num = isl_signs.get_sign_svg(sign_key, title=name)
                st.markdown(svg_num, unsafe_allow_html=True)

    # TAB 3: Common Everyday & Healthcare Expressions
    with learn_tabs[2]:
        st.subheader("Everyday Communication & Healthcare Gestures")
        vocab = isl_data.VOCAB_CACHE.get("vocabulary", [])

        # Category picker
        vocab_cats = list(isl_data.VOCAB_CATEGORY_NAMES.keys())
        cat_labels = [isl_data.VOCAB_CATEGORY_NAMES[k] for k in vocab_cats]
        chosen_cat_idx = st.selectbox("Filter vocabulary category:", range(len(vocab_cats)), format_func=lambda i: cat_labels[i])
        chosen_cat = vocab_cats[chosen_cat_idx]

        filtered = [v for v in vocab if v.get("category") == chosen_cat]
        st.caption(f"Showing **{len(filtered)}** signs in this category.")

        v_cols = st.columns(3)
        for idx, item in enumerate(filtered):
            with v_cols[idx % 3]:
                w = item.get("word")
                st.markdown(f"""
                <div class="feature-card">
                    <h4 style="margin:0; color:#0f172a; text-transform:capitalize;">{w}</h4>
                    <p style="margin:3px 0; color:#475569;"><strong>Hindi:</strong> {item.get('hindi')}</p>
                    <p style="margin:3px 0; color:#475569;"><strong>Kannada:</strong> {item.get('kannada')}</p>
                    <p style="font-size:0.85rem; color:#64748b; margin-top:6px;">{item.get('sign_description')}</p>
                </div>
                """, unsafe_allow_html=True)
                svg = isl_signs.get_sign_svg(w)
                st.markdown(svg, unsafe_allow_html=True)
                if st.button(f"🔊 Listen '{w}'", key=f"learn_aud_{item['id']}"):
                    aud = generate_tts_audio_fn(w, "en")
                    if aud:
                        st.audio(aud, format="audio/mp3", autoplay=True)

    # TAB 4: Interactive Quiz & Assessment
    with learn_tabs[3]:
        st.subheader("🎯 ISL Knowledge Assessment Quiz")
        st.write("Test your Indian Sign Language recognition knowledge across clinical and everyday scenarios.")

        total_q = len(QUIZ_QUESTIONS)
        q_idx = st.session_state.quiz_index % total_q
        current_q = QUIZ_QUESTIONS[q_idx]

        # Progress bar
        progress_val = (q_idx + 1) / total_q
        st.progress(progress_val, text=f"Question {q_idx + 1} of {total_q}")

        st.markdown(f"### Q{q_idx + 1}: {current_q['question']}")

        user_choice = st.radio(
            "Select the correct answer:",
            current_q["options"],
            key=f"quiz_radio_{q_idx}"
        )

        col_submit, col_next, col_reset = st.columns([1, 1, 1])
        with col_submit:
            if st.button("Check Answer", type="primary", use_container_width=True):
                chosen_idx = current_q["options"].index(user_choice)
                if chosen_idx == current_q["answer_idx"]:
                    st.success("🎉 Correct! Excellent job!")
                    st.session_state.quiz_score += 1
                else:
                    correct_text = current_q["options"][current_q["answer_idx"]]
                    st.error(f"❌ Not quite right. The correct answer is: **{correct_text}**")

                st.info(f"💡 **Explanation:** {current_q['explanation']}")
                st.session_state.quiz_answered = True

        with col_next:
            if st.button("Next Question ➡️", use_container_width=True):
                st.session_state.quiz_index = (st.session_state.quiz_index + 1) % total_q
                st.session_state.quiz_answered = False
                st.rerun()

        with col_reset:
            if st.button("🔄 Reset Quiz", use_container_width=True):
                st.session_state.quiz_index = 0
                st.session_state.quiz_score = 0
                st.session_state.quiz_answered = False
                st.rerun()

        st.metric(label="Current Quiz Score", value=f"{st.session_state.quiz_score} Points")
