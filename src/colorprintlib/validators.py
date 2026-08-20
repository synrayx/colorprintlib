"""Input validation helpers for ColorPrintLib."""

import re


def is_required(value, name="value"):
 if value is None or str(value).strip() == "":
 raise ValueError(f"{name} is required")


def is_int(value, name="value"):
 if not str(value).lstrip("-").isdigit():
 raise ValueError(f"{name} must be an integer")
 return int(value)


def is_float(value, name="value"):
 try:
 return float(value)
 except (TypeError, ValueError):
 raise ValueError(f"{name} must be a number")


def is_range(value, low, high, name="value"):
 number = is_int(value, name)
 if not (low <= number <= high):
 raise ValueError(f"{name} must be between {low} and {high}")
 return number


def is_email(value):
 if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", str(value)):
 raise ValueError("not a valid email address")
 return value


def is_url(value):
 if not re.match(r"^https?://", str(value)):
 raise ValueError("not a valid URL")
 return value


def is_slug(value):
 if not re.match(r"^[a-z0-9-]+$", str(value)):
 raise ValueError("must be a lowercase slug")
 return value


def length(value, minimum=0, maximum=1_000_000, name="value"):
 size = len(str(value))
 if not (minimum <= size <= maximum):
 raise ValueError(f"{name} length must be between {minimum} and {maximum}")
 return value