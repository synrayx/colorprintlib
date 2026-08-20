"""Command line interface for ColorPrintLib."""

import argparse
import sys

from .core import Options, run
from . import __version__


def build_parser():
 parser = argparse.ArgumentParser(
 prog="colorprintlib",
 description="ColorPrintLib - A small library for colored, formatted terminal output.",
 )
 parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
 parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose output")
 parser.add_argument("-n", "--dry-run", action="store_true", help="simulate without writing")
 parser.add_argument("-o", "--output-dir", default="./out", help="output directory")
 parser.add_argument("-t", "--timeout", type=int, default=30, help="timeout in seconds")
 parser.add_argument("--config", help="path to a JSON config file")
 return parser


def main(argv=None):
 args = build_parser().parse_args(argv)
 options = Options(
 verbose=args.verbose,
 dry_run=args.dry_run,
 output_dir=args.output_dir,
 timeout=args.timeout,
 )
 if args.config:
 from .core import load_json
 cfg = load_json(args.config)
 options.extra = cfg
 result = run(options)
 if not args.quiet:
 print(json_dump(result))
 return 0


def json_dump(obj):
 import json
 return json.dumps(obj, indent=2)


if __name__ == "__main__":
 sys.exit(main())