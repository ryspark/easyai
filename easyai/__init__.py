# ERROR HANDLING
def suppress_tf_warnings():
  """
  Suppresses tensorflow warnings for tensorflow == 1.14.0 or tensorflow-gpu == 1.8.0.
  """
  import os
  os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

  import warnings
  warnings.simplefilter(action = "ignore", category = FutureWarning)

  import tensorflow as tf
  try:
    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
  except AttributeError:
    tf.logging.set_verbosity(tf.logging.ERROR)
  # compatible with tensorflow == 1.14.0 and tensorflow-gpu == 1.8.0

suppress_tf_warnings()

from . import _advanced
from . import support
from . import applications
from . import core
from . import framework
from . import layers

# Importable from root
from .framework import *
from .core import NN

__version__ = "0.0a"