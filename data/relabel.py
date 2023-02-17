from pathlib import Path

files = Path().glob("*.jpg")
label = "a"

for i, file in enumerate(files):
  file.rename(f"qr_code_{label}_{i:03d}.jpg")
