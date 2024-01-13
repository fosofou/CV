import cv2
from .utils import save_img
import numpy as np


def sobel_contours(img_path: str):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Ядро для оператора Собеля
    kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    # Применение фильтра Собеля
    res = cv2.filter2D(img, -1, kernel)

    # Сохранение результата
    save_img(res, "20_sobel_contours")
    return res

