import cv2
from .utils import save_img


def histogram_equalize(img_path: str):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Преобразование в оттенки серого
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Выравнивание гистограммы
    img_equalized = cv2.equalizeHist(img_gray)

    # Сохранение результата
    save_img(img_equalized, "14_histogram_equalize")
    return img_equalized
