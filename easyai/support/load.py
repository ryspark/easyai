
"""

"easyai.support.load.py"

Loads new, user-supplied data.

"""

from io import BytesIO
from typing import Union, List

import requests
from PIL import Image


# GENERAL FUNCTIONS
def load_imgs(*paths) -> Union[List[Image.Image], Image.Image]:
  """
  Loads new images from paths or links. Images will be of shape (width, height, 3) and will have pixel values
  ranging from 0 to 255.

  :param paths: any number of paths or downloadable image links.
  :return: tuple of lists of images as numpy arrays.
  """
  result = []
  for path in paths:
    try:
      result.append(Image.open(path))
    except FileNotFoundError:
      result.append(Image.open(BytesIO(requests.get(path).content)))
  return result[0] if len(result) == 1 else result