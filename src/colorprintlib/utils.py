"""Small shared helpers for ColorPrintLib."""

import hashlib
import re
from pathlib import Path


def slugify(text):
 text = text.lower().strip()
 text = re.sub(r"[^a-z0-9]+", "-", text)
 return text.strip("-")


def sha256_file(path):
 digest = hashlib.sha256()
 with open(path, "rb") as fh:
 for block in iter(lambda: fh.read(65536), b""):
 digest.update(block)
 return digest.hexdigest()


def ensure_dir(path):
 Path(path).mkdir(parents=True, exist_ok=True)
 return path