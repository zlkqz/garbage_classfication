import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.applications import resnet50, ResNet50
from utils import load_data,  MODEL_SAVE_PATH
from data_processing import preprocess, draw_result, store_dict
from sklearn.model_selection import train_test_split


class ImgModel(tf.keras.Model):
    def __init__(self):
        super(ImgModel, self).__init__()

        self.preprocessing_layer = resnet50.preprocess_input
        self.base_model = ResNet50(input_shape=(224, 224) + (3, ),
                                   weights="imagenet",
                                   include_top=False)
        self.pooling = GlobalAveragePooling2D()
        self.fc = Sequential([
            Dropout(0.5),
            Dense(512, activation="relu"),
            Dropout(0.3),
            Dense(128, activation="relu"),
            Dense(4)
        ])

    def call(self, input_tensor):
        print(input_tensor)
        x = self.preprocessing_layer(input_tensor)
        x = self.base_model(x)
        x = self.pooling(x)

        return self.fc(x)


if __name__ == "__main__":
    # 读取数据并存储索引字典，然后划分数据集再生成dataset
    paths, labels, name2label, label2name = load_data()
    store_dict(name2label, label2name)
    train_paths, test_paths, train_labels, test_labels = train_test_split(
        paths, labels,
        test_size=0.05,
        stratify=labels
    )
    train_ds = tf.data.Dataset.from_tensor_slices((train_paths, train_labels))
    test_ds = tf.data.Dataset.from_tensor_slices((test_paths, test_labels))

    AUTOTUNE = tf.data.AUTOTUNE
    batch_size = 128
    # 设置dataset参数
    train_ds = train_ds.shuffle(5000).map(preprocess).batch(batch_size).prefetch(AUTOTUNE)
    test_ds = test_ds.map(preprocess).batch(batch_size).prefetch(AUTOTUNE)

    # 创建模型
    model = ImgModel()
    # 配置模型
    base_learning_rate = 0.0001
    model.compile(optimizer=tf.keras.optimizers.Adam(lr=base_learning_rate),
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=["accuracy"])
    # 设置early_stop
    es = tf.keras.callbacks.EarlyStopping(
        monitor="val_loss", patience=2, min_delta=0.0001
    )
    # 训练
    history = model.fit(train_ds, epochs=15, validation_data=test_ds, callbacks=[es])
    # 保存模型
    model.save_weights(MODEL_SAVE_PATH, save_format="tf")
    # 保存训练和测试结果图像
    draw_result(history.history["accuracy"], history.history["val_accuracy"])
