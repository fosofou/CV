import cv2
from .utils import save_img
import numpy as np


def move_right_10(img_path: str):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Получение размеров изображения
    height, width, channels = img.shape

    # Создание матрицы для смещения вправо на 10 пикселей
    translation_matrix = np.float32([[1, 0, 10], [0, 1, 0]])

    # Применение аффинного преобразования для смещения
    moved_image = cv2.warpAffine(img, translation_matrix, (width, height))

    # Сохранение результата
    save_img(moved_image, "10_move_right_10")
    return moved_image
