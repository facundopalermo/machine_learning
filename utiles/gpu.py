# tensorflow
import tensorflow as tf
print('tensorflow: %s' % tf.__version__)


print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))