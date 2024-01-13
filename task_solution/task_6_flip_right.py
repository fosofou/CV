import cv2
from .utils import save_img


def flip_right(img_path: str):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Отражение изображения по правой границе
    flipped = cv2.flip(img, 1)

    # Сохранение результата
    save_img(flipped, "6_flip_right")
    return flipped
