"""Core data models for ColorPrintLib."""

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone


def now_iso():
 return datetime.now(timezone.utc).isoformat()


@dataclass
class Item:
 id: str = field(default_factory=lambda: uuid.uuid4().hex)
 created_at: str = field(default_factory=now_iso)
 updated_at: str = field(default_factory=now_iso)
 metadata: dict = field(default_factory=dict)

 def to_dict(self):
 return {
 "id": self.id,
 "created_at": self.created_at,
 "updated_at": self.updated_at,
 "metadata": self.metadata,
 }


@dataclass
class Result:
 ok: bool = True
 value: object = None
 error: str = None
 duration_ms: float = 0.0

 def to_dict(self):
 return {"ok": self.ok, "value": self.value, "error": self.error, "duration_ms": self.duration_ms}


@dataclass
class Event:
 kind: str
 payload: dict = field(default_factory=dict)
 ts: str = field(default_factory=now_iso)