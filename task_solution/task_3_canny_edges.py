import cv2
from .utils import save_img


def canny_edges(img_path: str):
    # Загрузка изображения в оттенках серого
    grayscale_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Обнаружение границ с использованием алгоритма Canny
    edges = cv2.Canny(grayscale_img, 100, 200)

    # Сохранение результата
    save_img(edges, "3_canny_edges")
    return edges
