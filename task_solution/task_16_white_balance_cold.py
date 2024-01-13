import cv2
from .utils import save_img
import numpy as np


def white_balance_cold(img_path: str, coldness: float = 20):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Разделение каналов
    b, g, r = cv2.split(img)
    res = cv2.merge((
        np.clip((b.astype(np.int16) + coldness), 0, 255).astype(np.uint8),
        g,
        np.clip((r.astype(np.int16) - coldness), 0, 255).astype(np.uint8)
    ))

    # Коррекция баланса белого для "холодного" эффекта
    save_img(res, "16_white_balance_cold")
    return res
