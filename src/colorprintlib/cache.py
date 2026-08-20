"""Simple TTL cache used across ColorPrintLib."""

import threading
import time


class TTLCache:
 def __init__(self, ttl=300, max_size=1024):
 self.ttl = ttl
 self.max_size = max_size
 self._data = {}
 self._lock = threading.Lock()

 def get(self, key):
 with self._lock:
 item = self._data.get(key)
 if item is None:
 return None
 value, expires = item
 if time.time() > expires:
 del self._data[key]
 return None
 return value

 def set(self, key, value, ttl=None):
 ttl = ttl or self.ttl
 with self._lock:
 if len(self._data) >= self.max_size and key not in self._data:
 self._evict_one()
 self._data[key] = (value, time.time() + ttl)

 def delete(self, key):
 with self._lock:
 self._data.pop(key, None)

 def clear(self):
 with self._lock:
 self._data.clear()

 def _evict_one(self):
 oldest = min(self._data.items(), key=lambda kv: kv[1][1])
 del self._data[oldest[0]]

 def keys(self):
 with self._lock:
 now = time.time()
 return [k for k, (v, e) in self._data.items() if e > now]

 def stats(self):
 with self._lock:
 return {"size": len(self._data), "max": self.max_size, "ttl": self.ttl}