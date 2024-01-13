import cv2
from .utils import save_img


def grayscale(img_path: str):
    # Загрузка изображения в оттенках серого
    grayscale_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Сохранение результата
    save_img(grayscale_img, "5_grayscale")

    return grayscale_img
