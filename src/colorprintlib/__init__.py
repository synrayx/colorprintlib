"""ColorPrintLib: A small library for colored, formatted terminal output."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]