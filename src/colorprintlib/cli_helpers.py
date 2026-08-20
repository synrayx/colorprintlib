"""Shared CLI building blocks for ColorPrintLib."""

import argparse
import os
import sys


def add_common_args(parser):
 parser.add_argument("--config", help="path to a JSON or YAML config file")
 parser.add_argument("--verbose", "-v", action="store_true", help="enable verbose output")
 parser.add_argument("--quiet", "-q", action="store_true", help="suppress non-error output")
 parser.add_argument("--output", "-o", help="write output to a file")
 parser.add_argument("--no-color", action="store_true", help="disable colored output")
 return parser


def env_flag(name, default=False):
 value = os.getenv(name)
 if value is None:
 return default
 return value.lower() in ("1", "true", "yes", "on")


def print_error(message):
 sys.stderr.write(f"error: {message}\n")


def success(message):
 sys.stdout.write(f"{message}\n")


def bool_arg(value):
 return value.lower() in ("1", "true", "yes", "on")