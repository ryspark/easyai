
"""

"easyai._advanced._losses"

Advanced keras losses, activity regularizers, and support. Not for use by easyai users-- does not use easyai API.

"""

from easyai.core import *

# SUPPORT FOR CUSTOM LOSS
class Evaluator(object):
  """
  Class used for custom loss and gradient functions. Should be used in conjunction with scipy.optimize.[whatever].
  """

  def __init__(self, obj: object):
    """
    Initializes Evaluator object.

    :param obj: obj that has some function used to evaluate loss and gradients, called "loss_and_grads"
    :raises AssertionError: obj must have loss_and_grads function
    """
    self.obj = obj
    assert hasattr(obj, "loss_and_grads"), "obj must have loss_and_grads function"
    self.reset()

  def f_loss(self, img: np.ndarray):
    """
    Calculates loss.

    :param img: image (array) used to calculate loss.
    :return: loss.
    """
    loss, grads = self.obj.loss_and_grads(img)
    self.loss = loss
    self.grads = grads
    return self.loss

  def f_grads(self, img):
    """
    Calculates gradients.

    :param img: image (array) used to calculate gradients.
    :return: gradients.
    """
    grads = np.copy(self.grads)
    self.reset()
    return grads

  def reset(self):
    self.loss = None
    self.grads = None

# REGULARIZERS FOR NST
class StyleRegularizer(keras.regularizers.Regularizer):

  def __init__(self, style_img, weight):
    self.style_gram = StyleRegularizer.gram_matrix(style_img)
    self.weight = weight
    self.uses_learning_phase = False
    super(StyleRegularizer, self).__init__()

  def __call__(self, x):
    gram_x = StyleRegularizer.gram_matrix(x.output[0])
    return self.weight * K.sum(K.mean(K.square(self.style_gram - gram_x)))
    # x.output[0] is generated by network, x.output[1] is the true label

  @staticmethod
  def gram_matrix(a):
    a = K.batch_flatten(K.permute_dimensions(a, (2, 0, 1)))
    a = K.reshape(a, (K.int_shape(a)[0], -1)) # flattening a
    return K.dot(a, K.transpose(a))

class ContentRegularizer(keras.regularizers.Regularizer):

  def __init__(self, weight):
    self.weight = weight
    self.uses_learning_phase = False
    super(ContentRegularizer, self).__init__()

  def __call__(self, x):
    return self.weight * K.sum(K.mean(K.square(x.output[0] - x.output[1])))

class TVRegularizer(keras.regularizers.Regularizer):

  def __init__(self, weight):
    self.weight = weight
    self.uses_learning_phase = False
    super(TVRegularizer, self).__init__()

  def __call__(self, x):
    shape = K.shape(x.output)
    num_rows, num_cols, channels = shape[0], shape[1], shape[2]
    # tensors are not iterable unless eager execution is enabled
    a = K.square(x.output[:, :num_rows - 1, :num_cols - 1, :] - x.output[:, 1:, :num_cols - 1, :])
    b = K.square(x.output[:, :num_rows - 1, :num_cols - 1, :] - x.output[:, :num_rows - 1, 1:, :])

    return K.sum(K.pow(a + b, 1.25))

# CALLBACKS
class LossHistory(keras.callbacks.Callback):
  """History of loss for a "model.fit" call. Copied from keras example code for callbacks."""

  def on_train_begin(self, logs = {}):
    self.losses = []

  def on_batch_end(self, batch, logs = {}):
    self.losses.append(logs.get("loss"))