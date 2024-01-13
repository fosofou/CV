import cv2
from .utils import save_img


def blur_image(img_path: str):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Размытие изображения
    res = cv2.blur(img, ksize=(10, 10))

    # Сохранение результата
    save_img(res, "21_blur_image")
    return res
