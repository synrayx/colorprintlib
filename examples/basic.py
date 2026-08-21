"""Minimal example for ColorPrintLib."""

from colorprintlib import colorprintlib


def main():
 runner = colorprintlib({"name": "ColorPrintLib", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()