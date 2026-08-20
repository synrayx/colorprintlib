"""Typed exceptions for ColorPrintLib."""


class colorprintlibError(Exception):
 """Base error for the whole package."""

 exit_code = 1


class ConfigurationError(colorprintlibError):
 """Raised when configuration is invalid or missing."""

 exit_code = 2


class ValidationError(colorprintlibError):
 """Raised when input data fails validation."""

 exit_code = 3


class NotFoundError(colorprintlibError):
 """Raised when a requested resource does not exist."""

 exit_code = 4


class ConflictError(colorprintlibError):
 """Raised when an operation conflicts with existing state."""

 exit_code = 5


class RateLimitError(colorprintlibError):
 """Raised when a rate limit is exceeded."""

 exit_code = 6


class TimeoutError(colorprintlibError):
 """Raised when an operation takes too long."""

 exit_code = 7


class UnsupportedError(colorprintlibError):
 """Raised for unsupported inputs or platforms."""

 exit_code = 8


class StateError(colorprintlibError):
 """Raised when internal state is inconsistent."""

 exit_code = 9


def guard(condition, message, exc=ValidationError):
 """Raise exc(message) when condition is False."""
 if not condition:
 raise exc(message)