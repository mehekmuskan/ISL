"""
ISL Data Module
Provides data structures, loader functions, search capabilities,
multilingual translations (English, Hindi, Kannada), and helper methods
for the ISL Connect platform.
"""

import json
import os
from typing import Dict, List, Optional, Tuple

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VOCAB_FILE = os.path.join(BASE_DIR, "speech_to_sign_vocab.json")
HOSPITAL_FILE = os.path.join(BASE_DIR, "hospital_phrases.json")


def load_vocabulary() -> Dict:
    """Loads and returns speech-to-sign vocabulary data."""
    if not os.path.exists(VOCAB_FILE):
        return {"total_entries": 0, "categories": [], "vocabulary": []}
    with open(VOCAB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_hospital_phrases() -> Dict:
    """Loads and returns hospital phrases dataset."""
    if not os.path.exists(HOSPITAL_FILE):
        return {"total_phrases": 0, "total_categories": 0, "categories": [], "phrases": []}
    with open(HOSPITAL_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# Cached data instances for performance
VOCAB_CACHE = load_vocabulary()
HOSPITAL_CACHE = load_hospital_phrases()


def get_categories_vocab() -> List[str]:
    """Returns list of vocabulary category identifiers."""
    return VOCAB_CACHE.get("categories", [])


def get_categories_hospital() -> List[str]:
    """Returns list of hospital phrase category identifiers."""
    return HOSPITAL_CACHE.get("categories", [])


def get_phrases_by_category(category: str) -> List[Dict]:
    """Retrieves all hospital phrases for a given clinical category."""
    all_phrases = HOSPITAL_CACHE.get("phrases", [])
    if category == "all" or not category:
        return all_phrases
    return [p for p in all_phrases if p.get("category") == category]


def search_hospital_phrases(query: str, category: Optional[str] = None) -> List[Dict]:
    """Searches hospital phrases across English, Hindi, Kannada, and keywords."""
    query = (query or "").strip().lower()
    phrases = get_phrases_by_category(category or "all")
    if not query:
        return phrases

    results = []
    for p in phrases:
        match = (
            query in p.get("english", "").lower()
            or query in p.get("hindi", "").lower()
            or query in p.get("kannada", "").lower()
            or query in p.get("sign_sequence", "").lower()
            or any(query in kw for kw in p.get("keywords", []))
        )
        if match:
            results.append(p)
    return results


def search_vocabulary(query: str, category: Optional[str] = None) -> List[Dict]:
    """Searches sign vocabulary entries matching a query string."""
    query = (query or "").strip().lower()
    vocab = VOCAB_CACHE.get("vocabulary", [])
    if category and category != "all":
        vocab = [v for v in vocab if v.get("category") == category]

    if not query:
        return vocab

    results = []
    for item in vocab:
        match = (
            query in item.get("word", "").lower()
            or query in item.get("hindi", "").lower()
            or query in item.get("kannada", "").lower()
            or query in item.get("sign_description", "").lower()
            or any(query in kw for kw in item.get("keywords", []))
        )
        if match:
            results.append(item)
    return results


def find_sign_for_word(word: str) -> Optional[Dict]:
    """Finds exact or best match vocabulary entry for a single word."""
    word_clean = word.strip().lower()
    for item in VOCAB_CACHE.get("vocabulary", []):
        if item.get("word").lower() == word_clean:
            return item
    return None


def translate_sentence_to_signs(sentence: str) -> List[Dict]:
    """
    Parses a sentence into a sequence of ISL sign units.
    First tries phrase matching, then multi-word, then individual words,
    and falls back to fingerspelling letters.
    """
    cleaned = sentence.strip().lower()
    if not cleaned:
        return []

    tokens = [t.strip(".,!?\"'") for t in cleaned.split() if t.strip(".,!?\"'")]
    sign_sequence = []
    i = 0
    vocab_items = VOCAB_CACHE.get("vocabulary", [])
    vocab_dict = {v["word"].lower(): v for v in vocab_items}

    while i < len(tokens):
        # Try 3-word match
        if i + 3 <= len(tokens):
            three_word = f"{tokens[i]} {tokens[i+1]} {tokens[i+2]}"
            if three_word in vocab_dict:
                sign_sequence.append(vocab_dict[three_word])
                i += 3
                continue

        # Try 2-word match
        if i + 2 <= len(tokens):
            two_word = f"{tokens[i]} {tokens[i+1]}"
            if two_word in vocab_dict:
                sign_sequence.append(vocab_dict[two_word])
                i += 2
                continue

        # Try 1-word match
        one_word = tokens[i]
        if one_word in vocab_dict:
            sign_sequence.append(vocab_dict[one_word])
            i += 1
            continue

        # Fallback: create dynamic fingerspelling representation
        fallback_item = {
            "id": -1,
            "category": "fingerspelling",
            "word": one_word,
            "hindi": one_word,
            "kannada": one_word,
            "sign_description": f"Fingerspell letters: {' - '.join(list(one_word.upper()))}",
            "is_fingerspelled": True,
            "letters": list(one_word.lower())
        }
        sign_sequence.append(fallback_item)
        i += 1

    return sign_sequence


# Clinical Category Display Names
CATEGORY_NAMES = {
    "emergency_urgent": "🚨 Emergency & Urgent Care",
    "symptoms_pain": "🩺 Symptoms & Pain Evaluation",
    "doctor_patient_dialogue": "👨‍⚕️ Doctor-Patient Dialogue",
    "nursing_assistance": "🧑‍⚕️ Nursing & Assistance",
    "medication_pharmacy": "💊 Medication & Pharmacy",
    "diagnostic_tests": "🔬 Diagnostic & Lab Tests",
    "vital_signs_monitoring": "📊 Vital Signs Monitoring",
    "food_diet": "🍲 Food & Nutrition Support",
    "mobility_comfort": "🦽 Mobility, Rest & Comfort",
    "hygiene_restroom": "🧼 Hygiene & Restroom Needs",
    "discharge_admin": "📋 Discharge & Administration",
    "pediatric_maternal": "👶 Pediatric & Maternal Care"
}

VOCAB_CATEGORY_NAMES = {
    "greetings_social": "👋 Greetings & Social",
    "medical_emergency": "🏥 Medical & Emergency",
    "daily_needs": "💧 Daily Needs",
    "family_people": "👨‍👩‍👧 Family & People",
    "emotions_feelings": "😊 Emotions & Feelings",
    "questions": "❓ Question Words",
    "time_numbers": "⏰ Time & Numbers",
    "actions_verbs": "🏃 Actions & Common Verbs",
    "food_nutrition": "🍎 Food & Nutrition",
    "alphabet_signs": "🔤 ISL Alphabet A-Z"
}
