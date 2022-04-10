import pathlib

IMAGE_PATH = "E:\\work\\服创\\垃圾分类图片\\garbage_images2"
MODEL_SAVE_PATH = "model_weights"
IMAGE_SAVE_PATH = "result.png"
LABEL2NAME_PATH = "label2name.pk"
NAME2LABEL_PATH = "name2label.pk"


def load_data():
    """读取数据并打乱"""
    image_dir = pathlib.Path(IMAGE_PATH)
    # 获取索引字典
    names = sorted([item.name for item in image_dir.glob("*")])
    name2label = {name:label for label, name in enumerate(names)}
    label2name = {label:name for name, label in name2label.items()}

    # 获取所有图片路径和标签
    all_image_paths = []
    all_image_labels = []
    # 以下三个文件夹中还有子文件夹
    other_names = ["harmful", "kitchen", "other", "recyclable"]
    for path in list(image_dir.glob("*")):
        name = path.name
        if name in other_names:
            paths = list(path.glob("*/*"))
        else:
            paths = list(path.glob("*"))
        labels = [name2label[name]] * len(paths)
        all_image_paths += paths
        all_image_labels += labels

        # 将all_image_paths转换为字符形式
        all_image_paths = [str(path) for path in all_image_paths]

    return all_image_paths, all_image_labels, name2label, label2name
