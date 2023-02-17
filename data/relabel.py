from pathlib import Path

import os

files = Path().glob("*.jpg")
label = "a"

for i, file in enumerate(files):
  os.rename(file, f"qr_code_{label}_{i:03d}.jpg")
