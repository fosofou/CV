import cv2
from .utils import save_img
import numpy as np


def fourier_low_pass_filter(img_path: str):
    # Загрузка изображения
    img = cv2.imread(img_path)

    # Применение двумерного Фурье-преобразования
    dft = np.fft.fft2(img, axes=(0, 1))
    dft_shift = np.fft.fftshift(dft)

    # Создание маски низких частот
    mask = create_low_pass_filter_mask(img.shape[:2])

    if len(img.shape) == 3:
        mask = np.stack([mask] * img.shape[2], axis=-1)

    # Применение маски к Фурье-преобразованию
    dft_shift_masked = np.multiply(dft_shift, mask) / 255

    # Обратное Фурье-преобразование
    back_shift_masked = np.fft.ifftshift(dft_shift_masked)
    img_filtered = np.fft.ifft2(back_shift_masked, axes=(0, 1))

    # Получение амплитуды и преобразование обратно в изображение
    res = np.abs(img_filtered).clip(0, 255).astype(np.uint8)

    save_img(res, "23_fourier_filter_low")
    return res


def create_low_pass_filter_mask(shape):
    mask = np.zeros(shape, dtype=np.uint8)

    # Параметры маски
    radius = 32
    cy, cx = mask.shape[0] // 2, mask.shape[1] // 2

    # Создание круговой маски
    cv2.circle(mask, (cx, cy), radius, (255, 255, 255), -1)

    # Размытие маски
    mask = cv2.GaussianBlur(mask, (19, 19), 0)

    return mask
