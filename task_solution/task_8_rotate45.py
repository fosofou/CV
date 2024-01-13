import cv2
from .utils import save_img


def rotate_45(img_path: str):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Получение размеров изображения
    height, width, channels = img.shape

    # Нахождение центра изображения
    center = (width // 2, height // 2)

    # Подготовка матрицы преобразования для поворота на 45 градусов
    rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)

    # Применение поворота
    rotated_image = cv2.warpAffine(img, rotation_matrix, (width, height))

    # Сохранение результата
    save_img(rotated_image, "8_rotate_45")
    return rotated_image
