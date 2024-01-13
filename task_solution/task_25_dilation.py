import cv2
from .utils import save_img
import numpy as np


def dilation_operation(img_path: str):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Создание ядра для диляции
    kernel = np.ones((5, 5), 'uint8')

    # Применение операции диляции
    res = cv2.dilate(img, kernel, iterations=1)

    # Сохранение результата
    save_img(res, "25_dilation")
    return res
