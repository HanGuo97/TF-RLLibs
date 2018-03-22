
import numpy as np
import tensorflow as tf

from IPython.display import display
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error


def create_scope(name):
    with tf.variable_scope(name) as scope:
        pass
    return scope


def random_integers(low, high, shape, dtype=tf.int32):
    randint = np.random.randint(low=low, high=high, size=shape)
    randint = tf.convert_to_tensor(randint, dtype=dtype)
    return randint
    
    
def random_tensor(shape, *args, **kargs):
    return tf.random_normal(shape=shape, *args, **kargs)


def random_vector(shape, *args, **kargs):
    return np.random.normal(size=shape, *args, **kargs)


# check equalities
def check_equality(A, B, descip="", tolerance=1e-7):
    if isinstance(A, (list, tuple, np.ndarray)):
        diff = L2_distance(A, B)
    else:
        diff = np.square(A - B)
    print("SSE: %.11f\t%s: %r" % (diff, descip, diff < tolerance))


def check_inequality(A, B, descip="", tolerance=1e-3):
    if isinstance(A, (list, tuple, np.ndarray)):
        diff = L2_distance(A, B)
    else:
        diff = np.square(A - B)
    print("SSE: %.11f\t%s: %r" % (diff, descip, diff > tolerance))


def check_set_equality(set_A, set_B):
    if not isinstance(set_A, set):
        raise TypeError("set_A is not a set")
    if not isinstance(set_B, set):
        raise TypeError("set_B is not a set")
    if set_A.difference(set_B):
        raise ValueError("set_A - set_B != 0")
    if set_B.difference(set_A):
        raise ValueError("set_B - set_A != 0")
    print("PASSED")


def check_dict_equality(dict_A, dict_B):
    if not isinstance(dict_A, dict):
        raise TypeError("dict_A is not a dict")
    if not isinstance(dict_B, dict):
        raise TypeError("dict_B is not a dict")



def tensor_is_zero(sess, tensor, msg=None):
    is_zero = (sess.run(tensor) == 0).all()
    if msg:
        print(" ".join([msg, "= 0 %s" % ("PASSED" if is_zero else "FAILED")]))
    
    return is_zero


def L2_distance(X, Y, mean=False):
    # MSE = doubled_l2 / batch_size
    # L2 = doubled_l2 / 2
    if mean:
        doubled_l2 = np.mean(np.square(X - Y))
    else:
        doubled_l2 = np.sum(np.square(X - Y))
    
    # follow TF's implementation
    return doubled_l2 / 2


def test_message(msg):
    print("\n\n\nTESTING:\t" + msg + "\n\n\n")


class DictClass(object):
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)
