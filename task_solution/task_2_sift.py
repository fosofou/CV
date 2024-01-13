import cv2
from .utils import save_img


def sift_features(img_path: str):
    # Загрузка изображения в оттенках серого
    gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Проверка наличия ключевых точек
    sift = cv2.SIFT.create()
    kp = sift.detect(gray, None)

    # Отображение ключевых точек
    result_image = cv2.drawKeypoints(gray, kp, None,
                                     flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Сохранение результата
    save_img(result_image, "2_sift_features")
    return result_image
