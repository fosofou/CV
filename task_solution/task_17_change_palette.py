import cv2
from .utils import save_img
import numpy as np


def change_palette(img_path: str, palette_diff: (float, float, float) = (0, 0, 0)):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Разделение каналов
    b, g, r = cv2.split(img)

    # Изменение цветовой палитры
    res = cv2.merge((
        np.clip((b.astype(np.int16) + palette_diff[2]), 0, 255).astype(np.uint8),
        np.clip((g.astype(np.int16) + palette_diff[1]), 0, 255).astype(np.uint8),
        np.clip((r.astype(np.int16) + palette_diff[0]), 0, 255).astype(np.uint8)
    ))

    # Сохранение результата
    save_img(res, "17_change_palette")
    return res
