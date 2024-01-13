import cv2
from .utils import get_screen_size, resize_image, save_img


def orb_features(img_path: str):
    # Загрузка изображения
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Изменение размера изображения
    screen_width, screen_height = get_screen_size()
    img_resized = resize_image(img, screen_width, screen_height)

    orb = cv2.ORB.create()
    kp, des = orb.detectAndCompute(img_resized, None)

    # Рисование только положения ключевых точек, без размера и ориентации
    res = cv2.drawKeypoints(img_resized, kp, None, color=(0, 255, 0), flags=0)

    # Сохранение результата
    save_img(res, "1_orb_features")
    return res
