import cv2
from .utils import save_img


def convert_to_hsv(img_path: str):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Преобразование в цветовое пространство HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Сохранение результата
    save_img(img_hsv, "4_hsv")

    return img_hsv
