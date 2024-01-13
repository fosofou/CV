import cv2
from .utils import save_img


def rotate_30_point(image_path: str, rotation_point: (float, float) = (0, 0)):
    # Загрузка изображения
    original_image = cv2.imread(image_path)

    # Получение размеров изображения
    height, width, _ = original_image.shape

    # Подготовка матрицы преобразования для поворота
    rotation_matrix = cv2.getRotationMatrix2D(rotation_point, 30, 1.0)

    # Применение поворота
    rotated_image = cv2.warpAffine(original_image, rotation_matrix, (width, height))

    # Рисование круга вокруг точки вращения
    cv2.circle(rotated_image, (int(rotation_point[0]), int(rotation_point[1])), radius=3, color=(0, 0, 255),
               thickness=2)

    # Сохранение результата
    save_img(rotated_image, "9_rotate_30_point")
    return rotated_image
