"""
Test Suite for ISL Connect Platform
Validates:
- Dataset integrity and schema conformity (speech_to_sign_vocab.json, hospital_phrases.json)
- Multilingual translations presence (English, Hindi, Kannada)
- Category counts and urgency classifications
- Search and translation tokenization helpers
- Visual SVG sign generation for alphabets and key medical signs
- Audio TTS synthesis for English, Hindi, and Kannada
"""

import json
import os
import pytest
import isl_data
import isl_signs
from gtts import gTTS


def test_vocab_dataset_structure():
    """Verify speech_to_sign_vocab.json format, counts, and non-empty multilingual fields."""
    data = isl_data.load_vocabulary()
    assert "total_entries" in data
    assert "categories" in data
    assert "vocabulary" in data

    entries = data["vocabulary"]
    assert len(entries) >= 200, f"Expected at least 200 vocabulary entries, got {len(entries)}"
    assert len(data["categories"]) == 10, f"Expected 10 categories, got {len(data['categories'])}"

    for item in entries:
        assert "id" in item
        assert "word" in item and item["word"].strip() != ""
        assert "hindi" in item and item["hindi"].strip() != ""
        assert "kannada" in item and item["kannada"].strip() != ""
        assert "sign_description" in item and len(item["sign_description"]) > 5
        assert "category" in item and item["category"] in data["categories"]


def test_hospital_phrases_dataset():
    """Verify hospital_phrases.json format, counts, categories, and urgency tags."""
    data = isl_data.load_hospital_phrases()
    assert "total_phrases" in data
    assert "total_categories" in data
    assert "phrases" in data

    phrases = data["phrases"]
    assert len(phrases) >= 113, f"Expected at least 113 hospital phrases, got {len(phrases)}"
    assert len(data["categories"]) == 12, f"Expected 12 categories, got {len(data['categories'])}"

    urgency_levels = {"High", "Medium", "Low"}
    for phrase in phrases:
        assert "english" in phrase and phrase["english"].strip() != ""
        assert "hindi" in phrase and phrase["hindi"].strip() != ""
        assert "kannada" in phrase and phrase["kannada"].strip() != ""
        assert "sign_sequence" in phrase and len(phrase["sign_sequence"]) > 0
        assert phrase.get("urgency") in urgency_levels
        assert phrase.get("category") in data["categories"]


def test_search_and_filter_helpers():
    """Test search helper functions in isl_data.py."""
    # Search English keyword
    results_water = isl_data.search_hospital_phrases("water")
    assert len(results_water) >= 1
    assert any("water" in p["english"].lower() for p in results_water)

    # Search Hindi keyword
    results_hi = isl_data.search_hospital_phrases("दर्द")
    assert len(results_hi) >= 1

    # Search Kannada keyword
    results_kn = isl_data.search_hospital_phrases("ವೈದ್ಯ")
    assert len(results_kn) >= 1

    # Filter by category
    results_cat = isl_data.get_phrases_by_category("emergency_urgent")
    assert len(results_cat) >= 10
    assert all(p["category"] == "emergency_urgent" for p in results_cat)


def test_sentence_to_signs_translation():
    """Test natural language sentence decomposition into sign sequences."""
    sentence = "Please call a doctor"
    tokens = isl_data.translate_sentence_to_signs(sentence)
    assert len(tokens) >= 2
    words = [t["word"].lower() for t in tokens]
    assert "please" in words or "doctor" in words


def test_svg_sign_generation():
    """Verify SVG rendering for all alphabets and medical gestures."""
    # Alphabets
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        svg = isl_signs.get_sign_svg(char)
        assert svg.startswith("<svg") and svg.endswith("</svg>")
        assert f">{char}<" in svg or f"Letter: {char}" in svg

    # Medical Signs
    for sign in ["doctor", "nurse", "emergency", "pain", "medicine", "water", "help"]:
        svg = isl_signs.get_sign_svg(sign)
        assert "<svg" in svg and "</svg>" in svg
        assert "linearGradient" in svg


def test_tts_synthesis():
    """Test that gTTS generates valid audio data for English, Hindi, and Kannada."""
    from app import generate_tts_audio

    # Test English
    audio_en = generate_tts_audio("Hello doctor", "en")
    assert audio_en is not None
    assert len(audio_en) > 100

    # Test Hindi
    audio_hi = generate_tts_audio("नमस्ते डॉक्टर", "hi")
    assert audio_hi is not None
    assert len(audio_hi) > 100

    # Test Kannada
    audio_kn = generate_tts_audio("ನಮಸ್ಕಾರ ವೈದ್ಯರೇ", "kn")
    assert audio_kn is not None
    assert len(audio_kn) > 100
