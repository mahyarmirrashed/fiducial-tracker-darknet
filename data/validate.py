from pathlib import Path
from pyzbar import pyzbar
from re import compile
from typing import Union

import cv2 as cv

from logger import logger

PATTERN = compile(r"qr_code_([a-c])_\d\d\d\.jpg")

files = Path().glob("**/*.jpg")
decoder = lambda obj: obj.data.decode("utf-8")


def extract_letter(filename) -> Union[str, None]:
  matches = PATTERN.match(filename)

  return matches.group(1) if matches else None


for file in files:
  if letter := extract_letter(file.name):
    for data in map(decoder, pyzbar.decode(cv.imread(file.as_posix()))):
      if letter == data:
        logger.info(f'Found "{letter}" successfully')
      else:
        logger.error(f'Expected "{letter}", found "{data}"')
  else:
    logger.warning(f'File "{file.name}" did not match pattern.')
