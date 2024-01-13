import cv2
from .utils import save_img
import numpy as np


def white_balance_warm(img_path: str, warmth: float = 20):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Разделение каналов
    b, g, r = cv2.split(img)

    # Коррекция баланса белого для "теплого" эффекта
    res = cv2.merge((
        np.clip((b.astype(np.int16) - warmth), 0, 255).astype(np.uint8),
        g,
        np.clip((r.astype(np.int16) + warmth), 0, 255).astype(np.uint8)
    ))

    # Сохранение результата
    save_img(res, "15_white_balance_warm")
    return res
