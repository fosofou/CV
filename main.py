from task_solution import *


def main():
    img_path = "./images/city_1.jpg"

    # Task 1: ORB Features
    orb_result = orb_features(img_path)

    # Task 2: SIFT Features
    sift_result = sift_features(img_path)

    # Task 3: Canny Edges
    canny_result = canny_edges(img_path)

    # Task 4: Convert to HSV
    hsv_result = convert_to_hsv(img_path)

    # Task 5: Convert to Grayscale
    grayscale_result = grayscale(img_path)

    # Task 6: Flip Right
    flip_right_result = flip_right(img_path)

    # Task 7: Flip Bottom
    flip_bottom_result = flip_bottom(img_path)

    # Task 8: Rotate 45 Degrees
    rotate_45_result = rotate_45(img_path)

    # Task 9: Rotate 30 Degrees Around a Point
    rotate_30_result = rotate_30_point(img_path, rotation_point=(50, 100))

    # Task 10: Move Right by 10 Pixels
    move_right_10_result = move_right_10(img_path)

    # Task 11: Change Brightness
    change_brightness_result = change_brightness(img_path, brightness_offset=100)

    # Task 12: Change Contrast
    change_contrast_result = change_contrast(img_path, alpha=3)

    # Task 13: Gamma Correction
    gamma_correction_result = gamma_correction(img_path, gamma=3)

    # Task 14: Histogram Equalization
    histogram_equalize_result = histogram_equalize(img_path)

    # Task 15: White Balance Warm
    white_balance_warm_result = white_balance_warm(img_path)

    # Task 16: White Balance Cold
    white_balance_cold_result = white_balance_cold(img_path, coldness=30)

    # Task 17: Change Palette
    change_palette_result = change_palette(img_path, palette_diff=(10, -10, 5))

    # Task 18: Binarization
    binarization_result = binarize_image(img_path)

    # Task 19: Binarization with Contours
    binarization_contours_result = binarize_image_contours(img_path)

    # Task 20: Sobel Contours
    sobel_contours_result = sobel_contours(img_path)

    # Task 21: Blur
    blur_result = blur_image(img_path)

    # Task 22: Fourier High Pass Filter
    fourier_high_pass_result = fourier_high_pass_filter(img_path)

    # Task 23: Fourier Low Pass Filter
    fourier_low_pass_result = fourier_low_pass_filter(img_path)

    # Task 24: Erosion
    erosion_result = erosion_operation(img_path)

    # Task 25: Dilation
    dilation_result = dilation_operation(img_path)


if __name__ == "__main__":
    main()
