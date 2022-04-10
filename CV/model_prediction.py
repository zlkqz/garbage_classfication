from utils import MODEL_SAVE_PATH, LABEL2NAME_PATH
import pickle
from data_processing import preprocess
import tensorflow as tf
from model_train import ImgModel
from flask import Flask, request
import base64
from flask_cors import CORS
import datetime

app = Flask(__name__)
image_save_path = "test_image.jpg"
CORS(app)

transfrom_dict = {
    "harmful": "有害垃圾",
    "kitchen": "厨余垃圾",
    "other": "其他垃圾",
    "recyclable": "可回收垃圾"
}


def create_model():
    model = ImgModel()
    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.0001),
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=["accuracy"])
    model.load_weights(MODEL_SAVE_PATH)

    return model


img_model = create_model()


@app.route('/predict', methods=['POST'])
def prediction():
    # 获取base64
    img = request.json["img"]

    # 将base64转为图片并储存
    imgdata = base64.b64decode(img)
    with open(image_save_path, "wb") as f:
        f.write(imgdata)

    image, _ = preprocess(image_save_path, 0)
    image = tf.reshape(image, (1, 224, 224, 3))
    output = img_model.call(image)
    result = int(tf.argmax(output, axis=1))

    with open(LABEL2NAME_PATH, "rb") as f:
        label2name = pickle.load(f)

    return transfrom_dict[label2name[result]]


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")