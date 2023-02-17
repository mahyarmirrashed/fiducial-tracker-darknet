import glob
import os

files = glob.glob("*.JPG")
label = "a"

for i, file in enumerate(files):
  os.rename(file, f"qr_code_{label}_{i:03d}.jpg")
