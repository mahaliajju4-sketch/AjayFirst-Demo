"""Compatibility shim expected by the test file `adding.py`.

Provides:
- `adding(a, b)` : returns sum of a and b
- `divide(a, b)` : delegates to `sum.divide` (keeps error message behavior)
"""
from typing import Any

from sum import divide as _divide


def adding(a: Any, b: Any) -> Any:
    return a + b


def divide(a: Any, b: Any):
    return _divide(a, b)
