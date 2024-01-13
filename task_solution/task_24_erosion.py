import cv2
from .utils import save_img
import numpy as np


def erosion_operation(img_path: str):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Создание ядра для эрозии
    kernel = np.ones((5, 5), 'uint8')

    # Применение операции эрозии
    res = cv2.erode(img, kernel, iterations=1)

    # Сохранение результата
    save_img(res, "24_erosion")
    return res
