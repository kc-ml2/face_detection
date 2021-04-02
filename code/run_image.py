# Under construction

from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, PReLU, Flatten, Softmax
from tensorflow.keras.models import Model

import numpy as np
import tensorflow as tf
from tensorflow import keras
from functools import partial


gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    tf.config.experimental.set_memory_growth(gpus[0], True)

training_data = [r'C:\Users\filmm\github\MTCNN-Tensorflow\prepare_data\pnet_data_for_cls.tfrecords',
                 r'C:\Users\filmm\github\MTCNN-Tensorflow\prepare_data\pnet_data_for_bbx.tfrecords']


# Create a dictionary describing the features.
image_feature_description = {
    'image_raw': tf.io.FixedLenFeature([], tf.string),
    'label_raw': tf.io.FixedLenFeature([], tf.string),
}
AUTOTUNE = tf.data.experimental.AUTOTUNE


def _parse_image_function(example_proto, label_type, shape):
    # Parse the input tf.train.Example proto using the dictionary above.
    features = tf.io.parse_single_example(example_proto, image_feature_description)

    image = tf.io.decode_raw(features['image_raw'], tf.uint8)
    image = tf.cast(image, tf.float32)

    image = (image - 127.5) * (1. / 128.0)
    image.set_shape([shape * shape * 3])
    image = tf.reshape(image, [shape, shape, 3])
    label = tf.io.decode_raw(features['label_raw'], tf.float32)

    if label_type == 'cls':
        image = tf.image.random_flip_left_right(image)
        image = tf.image.random_flip_up_down(image)
        label.set_shape([2])
    elif label_type == 'bbx':
        label.set_shape([4])
    elif label_type == 'pts':
        label.set_shape([10])

    return image, label


dataset_cls = tf.data.TFRecordDataset(training_data[0])
dataset_cls = dataset_cls.map(partial(_parse_image_function, label_type='cls', shape=12))
dataset_cls = dataset_cls.shuffle(2048)
dataset_cls = dataset_cls.prefetch(buffer_size=AUTOTUNE)

dataset_bbox = tf.data.TFRecordDataset(training_data[1])
dataset_bbox = dataset_bbox.map(partial(_parse_image_function, label_type='bbx', shape=12))
dataset_bbox = dataset_bbox.shuffle(2048)
dataset_bbox = dataset_bbox.prefetch(buffer_size=AUTOTUNE)

dataset_cls = dataset_cls.batch(64)
dataset_bbox = dataset_bbox.batch(64)
