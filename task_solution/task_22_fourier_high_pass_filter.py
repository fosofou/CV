import cv2
from .utils import save_img
import numpy as np


def fourier_high_pass_filter(image_path: str):
    # Загрузка изображения
    img = cv2.imread(image_path)

    # Применение двумерного Фурье-преобразования
    dft = np.fft.fft2(img, axes=(0, 1))
    dft_shift = np.fft.fftshift(dft)

    # Создание маски высоких частот (high-pass filter)
    mask = create_high_pass_filter_mask(img.shape[:2])

    # Применение маски к каждому каналу изображения
    dft_shift_masked = np.zeros_like(dft_shift)

    if len(img.shape) == 3:
        mask = np.stack([mask] * img.shape[2], axis=-1)

    dft_shift_masked = np.multiply(dft_shift, mask) / 255

    # Обратное Фурье-преобразование
    back_ishift_masked = np.fft.ifftshift(dft_shift_masked)
    img_filtered = np.fft.ifft2(back_ishift_masked, axes=(0, 1))

    # Получение амплитуды и преобразование обратно в изображение
    img_filtered = np.abs(img_filtered).clip(0, 255).astype(np.uint8)

    save_img(img_filtered, "22_fourier_high_pass_filter")
    return img_filtered


def create_high_pass_filter_mask(shape):
    mask = np.zeros(shape[:2], dtype=np.uint8)

    # Параметры маски
    radius = 128
    cy, cx = mask.shape[0] // 2, mask.shape[1] // 2

    # Создание круговой маски
    cv2.circle(mask, (cx, cy), radius, (255, 255, 255), -1)

    mask = 255 - mask
    mask = cv2.GaussianBlur(mask, (19, 19), 0)

    return mask
