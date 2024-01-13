import cv2
from .utils import save_img
import numpy as np


def change_brightness(img_path: str, brightness_offset: float = 0):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Преобразование в цветовое пространство HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Разделение каналов HSV
    h, s, v = cv2.split(img_hsv)

    # Изменение яркости канала V
    v_new = v.astype(np.int16) + brightness_offset

    # Ограничение значений в пределах от 0 до 255
    v_new = np.clip(v_new, 0, 255).astype(np.uint8)

    # Обновление канала V
    img_new = cv2.merge((h, s, v_new))

    # Обратное преобразование в BGR
    res = cv2.cvtColor(img_new, cv2.COLOR_HSV2BGR)

    # Сохранение результата
    save_img(res, "11_change_brightness")
    return res
