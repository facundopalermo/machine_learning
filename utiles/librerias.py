# scipy
import scipy
print('scipy: %s' % scipy.__version__)
# numpy
import numpy
print('numpy: %s' % numpy.__version__)
# matplotlib
import matplotlib
print('matplotlib: %s' % matplotlib.__version__)
# pandas
import pandas
print('pandas: %s' % pandas.__version__)
# statsmodels
import statsmodels
print('statsmodels: %s' % statsmodels.__version__)
# scikit-learn
import sklearn
print('sklearn: %s' % sklearn.__version__)
# tensorflow
import tensorflow as tf
print('tensorflow: %s' % tf.__version__)
# keras
import keras
print('keras: %s' % keras.__version__)
# seaborn
import seaborn
print('seaborn %s' % seaborn.__version__)
# imbalanced-learn
import imblearn
print('imblearn %s' % imblearn.__version__)
#scikit-image
import skimage
print('scikit-image %s' %skimage.__version__)


print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))