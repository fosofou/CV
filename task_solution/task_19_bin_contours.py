import cv2
from .utils import save_img


def binarize_image_contours(img_path: str):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Преобразование в оттенки серого
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Бинаризация изображения
    _, img_bin = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

    # Поиск контуров
    contours, hierarchy = cv2.findContours(img_bin.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Отрисовка контуров на исходном изображении
    cv2.drawContours(img, contours, -1, (0, 0, 255), 2, cv2.LINE_AA, hierarchy, 1)

    # Сохранение результата
    save_img(img, "19_binarization_contours")
    return img

