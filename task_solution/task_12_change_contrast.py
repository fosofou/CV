import cv2
from .utils import save_img


def change_contrast(img_path: str, alpha: float = 1):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Изменение контраста
    res = cv2.convertScaleAbs(img, alpha=alpha)

    # Сохранение результата
    save_img(res, "12_change_contrast")
    return res
