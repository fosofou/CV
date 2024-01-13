import cv2
from .utils import save_img
import numpy as np


def gamma_correction(img_path: str, gamma: float = 2.5):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Создание таблицы коррекции гаммы
    table = [((i / 255) ** (1 / gamma)) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    # Применение коррекции гаммы с использованием таблицы
    res = cv2.LUT(img, table)

    # Сохранение результата
    save_img(res, "13_gamma_correction")
    return res
