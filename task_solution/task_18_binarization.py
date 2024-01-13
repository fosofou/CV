import cv2
from .utils import save_img


def binarize_image(img_path: str):
    # Загрузка изображения
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Бинаризация изображения
    _, binary_result = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    save_img(binary_result, "18_binarization_image")
    return binary_result
