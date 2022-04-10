import tensorflow as tf
import matplotlib.pyplot as plt
from utils import IMAGE_SAVE_PATH, LABEL2NAME_PATH, NAME2LABEL_PATH
import pickle


def store_dict(name2label, label2name):
    """储存label2name和name2label字典"""
    with open(NAME2LABEL_PATH, "wb") as f:
        pickle.dump(name2label, f)
    with open(LABEL2NAME_PATH, "wb") as f:
        pickle.dump(label2name, f)


def preprocess(x, y):
    """读取并预处理数据"""
    img_raw = tf.io.read_file(x)
    image = tf.image.decode_jpeg(img_raw, channels=3)
    image = tf.image.resize(image, [224, 224])

    image = tf.cast(image, dtype=tf.float32)
    y = tf.cast(y, dtype=tf.int32)

    return image, y


def draw_result(train, test):
    """可视化分类结果"""
    plt.plot(train, label="train")
    plt.plot(test, label="test")
    plt.title("train and test results")
    plt.xlabel("epochs")
    plt.ylabel("accuracy")
    plt.legend()
    plt.savefig(IMAGE_SAVE_PATH)
