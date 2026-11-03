"""
ISL Signs Visual Demonstration Generator
Generates clean, professional SVG diagrams for Indian Sign Language (ISL):
- ISL Alphabet (A-Z) handshapes
- Numbers (0-9)
- Common Hospital & Everyday Key Signs (Doctor, Nurse, Medicine, Help, Pain, Water, Emergency, etc.)
- Dynamic fallback visual generator with hand and motion indicator arrows
"""

from typing import Dict, Optional


def _wrap_svg(content: str, width: int = 240, height: int = 240, title: str = "") -> str:
    """Wraps SVG body in a standard responsive SVG container with modern styling."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="max-width: {width}px; background: linear-gradient(135deg, #f8fafc 0%, #edf2f7 100%); border-radius: 12px; border: 1px solid #cbd5e1; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
  <defs>
    <linearGradient id="skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbd38d"/>
      <stop offset="100%" stop-color="#ed8936"/>
    </linearGradient>
    <linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3182ce"/>
      <stop offset="100%" stop-color="#2b6cb0"/>
    </linearGradient>
    <linearGradient id="emergencyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e53e3e"/>
      <stop offset="100%" stop-color="#c53030"/>
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="2" dy="3" stdDeviation="2" flood-opacity="0.15"/>
    </filter>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#3182ce" />
    </marker>
    <marker id="arrowRed" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#e53e3e" />
    </marker>
  </defs>
  {content}
  {f'<text x="{width/2}" y="{height - 12}" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="bold" fill="#4a5568" text-anchor="middle">{title}</text>' if title else ''}
</svg>"""


# Handshape SVG elements dictionary for Alphabets (A-Z)
ALPHABET_SVGS = {
    "A": """
      <!-- Wrist & Palm (Fist with thumb along side) -->
      <rect x="95" y="150" width="50" height="40" rx="8" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="80" y="85" width="70" height="75" rx="16" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Four curled fingers -->
      <rect x="85" y="70" width="14" height="35" rx="7" fill="#dd6b20"/>
      <rect x="101" y="65" width="14" height="40" rx="7" fill="#dd6b20"/>
      <rect x="117" y="68" width="14" height="37" rx="7" fill="#dd6b20"/>
      <rect x="133" y="75" width="13" height="30" rx="6.5" fill="#dd6b20"/>
      <!-- Thumb resting upright alongside index -->
      <rect x="68" y="80" width="16" height="50" rx="8" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Badge label -->
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">A</text>
    """,
    "B": """
      <!-- Open flat hand, 4 straight upright fingers, thumb crossed across palm -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="85" y="105" width="70" height="55" rx="12" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- 4 upright fingers touching -->
      <rect x="86" y="35" width="15" height="75" rx="7.5" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="103" y="25" width="15" height="85" rx="7.5" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="120" y="30" width="15" height="80" rx="7.5" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="137" y="45" width="14" height="65" rx="7" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Thumb folded over palm -->
      <path d="M 85 130 C 105 130, 115 138, 120 135" stroke="#c05621" stroke-width="8" stroke-linecap="round" fill="none"/>
      <!-- Badge label -->
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">B</text>
    """,
    "C": """
      <!-- Curved hand forming C shape -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <!-- Curved arch fingers -->
      <path d="M 155 70 C 110 50, 75 80, 80 120 C 85 160, 120 170, 155 155" stroke="url(#skin)" stroke-width="26" stroke-linecap="round" fill="none" filter="url(#shadow)"/>
      <path d="M 155 70 C 110 50, 75 80, 80 120 C 85 160, 120 170, 155 155" stroke="#dd6b20" stroke-width="4" stroke-dasharray="4,6" fill="none"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">C</text>
    """,
    "D": """
      <!-- Index upright, other fingers form circle with thumb -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <circle cx="110" cy="125" r="28" fill="url(#skin)" stroke="#c05621" stroke-width="3" filter="url(#shadow)"/>
      <circle cx="110" cy="125" r="14" fill="#f8fafc"/>
      <!-- Upright Index -->
      <rect x="88" y="30" width="16" height="85" rx="8" fill="url(#skin)" filter="url(#shadow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">D</text>
    """,
    "E": """
      <!-- All four fingers curved with tips resting on thumb -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="82" y="105" width="76" height="55" rx="14" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Thumb bent horizontal -->
      <rect x="75" y="125" width="80" height="18" rx="9" fill="#dd6b20"/>
      <!-- 4 curved fingertips pressing on thumb -->
      <rect x="85" y="75" width="15" height="35" rx="7.5" fill="url(#skin)"/>
      <rect x="102" y="70" width="15" height="40" rx="7.5" fill="url(#skin)"/>
      <rect x="119" y="73" width="15" height="37" rx="7.5" fill="url(#skin)"/>
      <rect x="136" y="80" width="14" height="30" rx="7" fill="url(#skin)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">E</text>
    """,
    "F": """
      <!-- Index & thumb form circle, other 3 fingers straight up -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="85" y="110" width="70" height="50" rx="12" fill="url(#skin)"/>
      <!-- 3 upright fingers -->
      <rect x="105" y="30" width="15" height="85" rx="7.5" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="122" y="35" width="15" height="80" rx="7.5" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="139" y="48" width="14" height="67" rx="7" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Circle of thumb and index -->
      <circle cx="85" cy="115" r="20" fill="none" stroke="url(#skin)" stroke-width="14" filter="url(#shadow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">F</text>
    """,
    "G": """
      <!-- Fist with index & thumb pointing sideways in parallel -->
      <rect x="100" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="95" y="95" width="60" height="65" rx="16" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Horizontal pointing index & thumb -->
      <rect x="40" y="95" width="70" height="16" rx="8" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="45" y="120" width="65" height="16" rx="8" fill="url(#skin)" filter="url(#shadow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">G</text>
    """,
    "H": """
      <!-- Fist with index & middle pointing sideways together -->
      <rect x="105" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="100" y="95" width="60" height="65" rx="16" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="35" y="95" width="80" height="15" rx="7.5" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="35" y="115" width="80" height="15" rx="7.5" fill="url(#skin)" filter="url(#shadow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">H</text>
    """,
    "I": """
      <!-- Fist with pinky pointing straight up -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="80" y="90" width="70" height="70" rx="16" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Pinky upright -->
      <rect x="135" y="35" width="14" height="75" rx="7" fill="url(#skin)" filter="url(#shadow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">I</text>
    """,
    "J": """
      <!-- Pinky tracing J curve -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="80" y="95" width="70" height="65" rx="16" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="135" y="55" width="14" height="55" rx="7" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- J swoosh arrow -->
      <path d="M 142 55 L 142 85 C 142 110, 110 115, 95 100" stroke="#3182ce" stroke-width="4" fill="none" marker-end="url(#arrow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">J</text>
    """,
    "K": """
      <!-- Index upright, middle forward-up, thumb between them -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="85" y="105" width="65" height="55" rx="14" fill="url(#skin)"/>
      <!-- Index straight up -->
      <rect x="90" y="35" width="15" height="85" rx="7.5" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Middle finger angled forward -->
      <line x1="108" y1="105" x2="135" y2="45" stroke="url(#skin)" stroke-width="16" stroke-linecap="round" filter="url(#shadow)"/>
      <!-- Thumb upright between -->
      <rect x="100" y="80" width="15" height="35" rx="7.5" fill="#dd6b20"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">K</text>
    """,
    "L": """
      <!-- Index straight up, thumb out at 90 degrees forming L -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="90" y="105" width="60" height="55" rx="14" fill="url(#skin)"/>
      <!-- Index vertical -->
      <rect x="92" y="30" width="16" height="90" rx="8" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Thumb horizontal -->
      <rect x="40" y="118" width="65" height="16" rx="8" fill="url(#skin)" filter="url(#shadow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">L</text>
    """,
    "M": """
      <!-- 3 fingers draped over thumb -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="80" y="95" width="75" height="65" rx="14" fill="url(#skin)"/>
      <rect x="85" y="70" width="15" height="50" rx="7.5" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="102" y="65" width="15" height="55" rx="7.5" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="119" y="68" width="15" height="52" rx="7.5" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Thumb peeking below 3rd finger -->
      <circle cx="136" cy="115" r="9" fill="#dd6b20"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">M</text>
    """,
    "N": """
      <!-- 2 fingers draped over thumb -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="80" y="95" width="75" height="65" rx="14" fill="url(#skin)"/>
      <rect x="90" y="65" width="16" height="55" rx="8" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="110" y="65" width="16" height="55" rx="8" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Thumb peeking below 2nd finger -->
      <circle cx="128" cy="115" r="9" fill="#dd6b20"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">N</text>
    """,
    "O": """
      <!-- All fingertips touching thumb forming round O -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <circle cx="120" cy="105" r="35" fill="none" stroke="url(#skin)" stroke-width="20" filter="url(#shadow)"/>
      <circle cx="120" cy="105" r="25" fill="#f8fafc"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">O</text>
    """,
    "P": """
      <!-- K shape pointing downward -->
      <rect x="95" y="65" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="85" y="90" width="65" height="50" rx="12" fill="url(#skin)"/>
      <rect x="90" y="130" width="15" height="75" rx="7.5" fill="url(#skin)" filter="url(#shadow)"/>
      <line x1="108" y1="130" x2="135" y2="185" stroke="url(#skin)" stroke-width="15" stroke-linecap="round" filter="url(#shadow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">P</text>
    """,
    "Q": """
      <!-- G shape pointing downward -->
      <rect x="100" y="65" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="95" y="95" width="60" height="55" rx="14" fill="url(#skin)"/>
      <rect x="50" y="145" width="65" height="15" rx="7.5" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="55" y="168" width="60" height="15" rx="7.5" fill="url(#skin)" filter="url(#shadow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">Q</text>
    """,
    "R": """
      <!-- Crossed index and middle fingers -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="85" y="105" width="65" height="55" rx="14" fill="url(#skin)"/>
      <!-- Crossed fingers -->
      <line x1="100" y1="120" x2="125" y2="30" stroke="url(#skin)" stroke-width="16" stroke-linecap="round" filter="url(#shadow)"/>
      <line x1="120" y1="120" x2="95" y2="30" stroke="url(#skin)" stroke-width="16" stroke-linecap="round" filter="url(#shadow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">R</text>
    """,
    "S": """
      <!-- Fist with thumb folded over front of all fingers -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="80" y="80" width="75" height="80" rx="18" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Curled finger notches -->
      <line x1="82" y1="105" x2="150" y2="105" stroke="#dd6b20" stroke-width="3"/>
      <!-- Thumb wrapped horizontally across front -->
      <rect x="75" y="110" width="82" height="24" rx="12" fill="url(#skin)" stroke="#c05621" stroke-width="2" filter="url(#shadow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">S</text>
    """,
    "T": """
      <!-- Fist with thumb poking up between index & middle -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="80" y="85" width="75" height="75" rx="16" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Thumb between index & middle -->
      <circle cx="105" cy="85" r="14" fill="#dd6b20" filter="url(#shadow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">T</text>
    """,
    "U": """
      <!-- Index & middle held straight up tightly together -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="85" y="105" width="65" height="55" rx="14" fill="url(#skin)"/>
      <rect x="96" y="28" width="16" height="88" rx="8" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="114" y="28" width="16" height="88" rx="8" fill="url(#skin)" filter="url(#shadow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">U</text>
    """,
    "V": """
      <!-- Index & middle spread apart in V shape -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="85" y="105" width="65" height="55" rx="14" fill="url(#skin)"/>
      <line x1="105" y1="120" x2="85" y2="30" stroke="url(#skin)" stroke-width="16" stroke-linecap="round" filter="url(#shadow)"/>
      <line x1="125" y1="120" x2="145" y2="30" stroke="url(#skin)" stroke-width="16" stroke-linecap="round" filter="url(#shadow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">V</text>
    """,
    "W": """
      <!-- Index, middle, ring spread in W shape -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="85" y="105" width="65" height="55" rx="14" fill="url(#skin)"/>
      <line x1="95" y1="120" x2="75" y2="32" stroke="url(#skin)" stroke-width="14" stroke-linecap="round" filter="url(#shadow)"/>
      <line x1="115" y1="120" x2="115" y2="28" stroke="url(#skin)" stroke-width="14" stroke-linecap="round" filter="url(#shadow)"/>
      <line x1="135" y1="120" x2="155" y2="32" stroke="url(#skin)" stroke-width="14" stroke-linecap="round" filter="url(#shadow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">W</text>
    """,
    "X": """
      <!-- Fist with index hooked like question mark -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="80" y="95" width="70" height="65" rx="16" fill="url(#skin)"/>
      <!-- Hooked index finger -->
      <path d="M 98 105 L 98 60 C 98 45, 125 45, 125 65" stroke="url(#skin)" stroke-width="16" stroke-linecap="round" fill="none" filter="url(#shadow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">X</text>
    """,
    "Y": """
      <!-- Thumb and pinky extended, middle 3 fingers curled -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="85" y="90" width="65" height="70" rx="16" fill="url(#skin)"/>
      <!-- Thumb pointing out left -->
      <line x1="95" y1="120" x2="45" y2="90" stroke="url(#skin)" stroke-width="16" stroke-linecap="round" filter="url(#shadow)"/>
      <!-- Pinky pointing out right -->
      <line x1="140" y1="120" x2="190" y2="85" stroke="url(#skin)" stroke-width="14" stroke-linecap="round" filter="url(#shadow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">Y</text>
    """,
    "Z": """
      <!-- Index finger pointing tracing Z in air -->
      <rect x="95" y="155" width="50" height="45" rx="8" fill="url(#skin)"/>
      <rect x="85" y="105" width="65" height="55" rx="14" fill="url(#skin)"/>
      <rect x="92" y="55" width="16" height="60" rx="8" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Z trajectory motion path -->
      <path d="M 60 55 L 140 55 L 70 120 L 150 120" stroke="#3182ce" stroke-width="5" stroke-dasharray="4,4" fill="none" marker-end="url(#arrow)"/>
      <circle cx="40" cy="40" r="22" fill="#3182ce"/>
      <text x="40" y="47" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">Z</text>
    """
}


# Key Clinical & Daily Demonstration SVGs
KEY_SIGNS_SVGS = {
    "doctor": """
      <!-- Checking wrist pulse (doctor) -->
      <rect x="40" y="130" width="100" height="35" rx="10" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Right hand tapping wrist with M / bent fingers -->
      <rect x="110" y="50" width="35" height="60" rx="10" fill="url(#skin)"/>
      <line x1="125" y1="110" x2="105" y2="135" stroke="#3182ce" stroke-width="4" marker-end="url(#arrow)"/>
      <circle cx="105" cy="140" r="8" fill="#e53e3e" opacity="0.6"/>
      <!-- Red Cross Stethoscope badge -->
      <circle cx="190" cy="50" r="25" fill="#e53e3e"/>
      <rect x="186" y="35" width="8" height="30" fill="#ffffff"/>
      <rect x="175" y="46" width="30" height="8" fill="#ffffff"/>
      <text x="120" y="210" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2b6cb0" text-anchor="middle">Tapping Wrist Pulse (DOCTOR)</text>
    """,
    "nurse": """
      <!-- Tapping Cross on Arm / Forehead (Nurse) -->
      <rect x="60" y="110" width="70" height="90" rx="14" fill="url(#skin)"/>
      <!-- Right index & middle drawing cross pattern -->
      <rect x="130" y="60" width="22" height="60" rx="11" fill="url(#skin)" filter="url(#shadow)"/>
      <path d="M 85 130 L 105 130 M 95 120 L 95 140" stroke="#3182ce" stroke-width="5" stroke-linecap="round"/>
      <!-- Nurse Cap badge -->
      <path d="M 160 50 L 200 50 L 210 70 L 150 70 Z" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
      <rect x="176" y="54" width="8" height="12" fill="#e53e3e"/>
      <rect x="174" y="56" width="12" height="8" fill="#e53e3e"/>
      <text x="120" y="210" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2b6cb0" text-anchor="middle">Cross on Arm (NURSE)</text>
    """,
    "help": """
      <!-- Fist with thumb up resting on flat palm raised upward (HELP) -->
      <rect x="50" y="150" width="130" height="24" rx="8" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Fist with upright thumb resting on it -->
      <rect x="90" y="90" width="55" height="55" rx="12" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="85" y="60" width="18" height="40" rx="9" fill="url(#skin)"/>
      <!-- Upward motion arrows -->
      <line x1="75" y1="140" x2="75" y2="70" stroke="#3182ce" stroke-width="5" marker-end="url(#arrow)"/>
      <line x1="165" y1="140" x2="165" y2="70" stroke="#3182ce" stroke-width="5" marker-end="url(#arrow)"/>
      <text x="120" y="210" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2b6cb0" text-anchor="middle">Flat Palm Lifting Fist (HELP)</text>
    """,
    "pain": """
      <!-- Two pointing index fingers twisting towards each other (PAIN) -->
      <line x1="40" y1="110" x2="105" y2="110" stroke="url(#skin)" stroke-width="16" stroke-linecap="round" filter="url(#shadow)"/>
      <line x1="200" y1="110" x2="135" y2="110" stroke="url(#skin)" stroke-width="16" stroke-linecap="round" filter="url(#shadow)"/>
      <!-- Jagged electric pain lightning in center -->
      <path d="M 120 70 L 115 105 L 125 115 L 117 150" stroke="#e53e3e" stroke-width="4" stroke-linecap="round" fill="none"/>
      <!-- Twisting motion indicators -->
      <path d="M 90 85 C 100 80, 110 80, 110 95" stroke="#e53e3e" stroke-width="3" fill="none" marker-end="url(#arrowRed)"/>
      <path d="M 150 135 C 140 140, 130 140, 130 125" stroke="#e53e3e" stroke-width="3" fill="none" marker-end="url(#arrowRed)"/>
      <text x="120" y="210" font-family="sans-serif" font-size="14" font-weight="bold" fill="#c53030" text-anchor="middle">Twisting Index Fingers (PAIN)</text>
    """,
    "medicine": """
      <!-- Grinding middle finger on open palm (MEDICINE) -->
      <ellipse cx="110" cy="140" rx="55" ry="30" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Vertical hand grinding middle finger into palm center -->
      <rect x="100" y="45" width="20" height="75" rx="10" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Circular circular swirl arrow in palm center -->
      <path d="M 105 130 A 15 15 0 1 1 125 135" stroke="#3182ce" stroke-width="3.5" fill="none" marker-end="url(#arrow)"/>
      <circle cx="190" cy="45" r="20" fill="#38a169"/>
      <text x="190" y="52" font-family="sans-serif" font-size="18" fill="#ffffff" text-anchor="middle">Rx</text>
      <text x="120" y="210" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2b6cb0" text-anchor="middle">Grinding Palm Motion (MEDICINE)</text>
    """,
    "water": """
      <!-- W handshape index tapping chin twice (WATER) -->
      <rect x="100" y="150" width="45" height="40" rx="8" fill="url(#skin)"/>
      <rect x="90" y="105" width="60" height="50" rx="12" fill="url(#skin)"/>
      <!-- W three fingers extended -->
      <rect x="85" y="40" width="14" height="70" rx="7" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="105" y="35" width="14" height="75" rx="7" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="125" y="42" width="14" height="68" rx="7" fill="url(#skin)" filter="url(#shadow)"/>
      <!-- Chin tap motion dots -->
      <circle cx="85" cy="25" r="6" fill="#3182ce"/>
      <circle cx="85" cy="15" r="4" fill="#63b3ed"/>
      <text x="120" y="210" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2b6cb0" text-anchor="middle">W-Hand Chin Tap (WATER)</text>
    """,
    "emergency": """
      <!-- Letter E shaken rapidly with alert pulses (EMERGENCY) -->
      <rect x="85" y="105" width="70" height="55" rx="14" fill="url(#skin)" filter="url(#shadow)"/>
      <rect x="80" y="125" width="75" height="16" rx="8" fill="#dd6b20"/>
      <!-- E fingers curved -->
      <rect x="88" y="75" width="14" height="35" rx="7" fill="url(#skin)"/>
      <rect x="104" y="70" width="14" height="40" rx="7" fill="url(#skin)"/>
      <rect x="120" y="73" width="14" height="37" rx="7" fill="url(#skin)"/>
      <!-- Urgent shake indicators -->
      <path d="M 60 110 L 40 110 M 60 130 L 40 130 M 180 110 L 200 110 M 180 130 L 200 130" stroke="#e53e3e" stroke-width="4" stroke-linecap="round"/>
      <circle cx="45" cy="45" r="22" fill="#e53e3e"/>
      <text x="45" y="52" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">SOS</text>
      <text x="120" y="210" font-family="sans-serif" font-size="14" font-weight="bold" fill="#c53030" text-anchor="middle">Rapid E-Shake (EMERGENCY)</text>
    """
}


def get_sign_svg(term: str, title: Optional[str] = None) -> str:
    """
    Returns an SVG illustration string for a word, phrase, or letter.
    Checks exact alphabet match, key clinical signs, or generates a dynamic
    professional ISL diagram.
    """
    clean_term = term.strip().upper()
    display_title = title or clean_term

    # Check alphabet (A-Z)
    if clean_term in ALPHABET_SVGS:
        return _wrap_svg(ALPHABET_SVGS[clean_term], title=f"ISL Letter: {clean_term}")

    # Check key signs
    lower_term = term.strip().lower()
    if lower_term in KEY_SIGNS_SVGS:
        return _wrap_svg(KEY_SIGNS_SVGS[lower_term], title=display_title)

    # Dynamic visual sign badge generator for arbitrary words
    body = f"""
      <rect x="20" y="20" width="200" height="150" rx="16" fill="#ffffff" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>
      <!-- Header banner -->
      <rect x="20" y="20" width="200" height="40" rx="16" fill="url(#accent)"/>
      <rect x="20" y="44" width="200" height="16" fill="url(#accent)"/>
      <text x="120" y="46" font-family="sans-serif" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">ISL SIGN</text>
      <!-- Center gesture symbol -->
      <circle cx="120" cy="115" r="32" fill="#ebf8ff" stroke="#3182ce" stroke-width="2"/>
      <text x="120" y="123" font-family="sans-serif" font-size="24" fill="#2b6cb0" text-anchor="middle">🤟</text>
      <circle cx="80" cy="100" r="10" fill="#bee3f8" opacity="0.6"/>
      <circle cx="160" cy="130" r="14" fill="#bee3f8" opacity="0.6"/>
      <!-- Motion arcs -->
      <path d="M 65 145 C 80 160, 160 160, 175 145" stroke="#3182ce" stroke-width="3" fill="none" stroke-dasharray="4,4" marker-end="url(#arrow)"/>
      <text x="120" y="195" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2d3748" text-anchor="middle">{clean_term[:22]}</text>
    """
    return _wrap_svg(body, title=display_title)
