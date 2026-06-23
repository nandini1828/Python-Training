"""
Word counting utility that normalizes case and strips punctuation.
"""
from __future__ import annotations

import re
from typing import Dict


_WORD_RE = re.compile(r"\b\w+\b", flags=re.UNICODE)


def word_count(text: str) -> Dict[str, int]:
    """
    Count words in `text` ignoring case and punctuation.

    Args:
        text: Input string to analyze.

    Returns:
        A dictionary mapping normalized words to their frequency.
    """
    if not text:
        return {}
    words = _WORD_RE.findall(text.lower())
    freqs: Dict[str, int] = {}
    for w in words:
        freqs[w] = freqs.get(w, 0) + 1
    return freqs
