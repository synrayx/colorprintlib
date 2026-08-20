"""Core logic for ColorPrintLib."""

import json
import os
import time
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Options:
 verbose: bool = False
 dry_run: bool = False
 output_dir: str = "./out"
 timeout: int = 30
 extra: dict = field(default_factory=dict)


def run(options: Options):
 """Entry point for the core engine. Returns a result summary."""
 start = time.time()
 out_dir = Path(options.output_dir)
 if not options.dry_run:
 out_dir.mkdir(parents=True, exist_ok=True)

 results = process_payload(options)

 if options.verbose:
 print(f"processed {len(results)} items in {time.time() - start:.2f}s")

 return {"items": len(results), "elapsed": round(time.time() - start, 3), "output": str(out_dir)}


def process_payload(options: Options):
 """Simulates the real workload. Replace internals with project logic."""
 items = []
 for i in range(5):
 items.append({"id": i, "name": f"item-{i}", "ok": True})
 return items


def load_json(path):
 with open(path, "r", encoding="utf-8") as fh:
 return json.load(fh)


def atomic_write(path, data):
 tmp = f"{path}.tmp"
 with open(tmp, "w", encoding="utf-8") as fh:
 json.dump(data, fh, indent=2)
 os.replace(tmp, path)