import cv2
from .utils import save_img


def flip_bottom(img_path: str):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Отражение изображения по нижней границе
    flipped = cv2.flip(img, 0)

    # Сохранение результата
    save_img(flipped, "7_flip_bottom")
    return flipped
