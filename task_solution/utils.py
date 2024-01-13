import tkinter as tk
import cv2
import os

SAVE_IMG_PATH = './result_img/'


def resize_image(img, target_width, target_height):
    aspect_ratio = img.shape[1] / img.shape[0]
    new_width = int(min(target_width, target_height * aspect_ratio))
    new_height = int(min(target_height, target_width / aspect_ratio))
    img_resized = cv2.resize(img, (new_width, new_height))
    return img_resized


def get_screen_size():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height


def save_img(img, filename):
    cv2.imwrite(os.path.join(SAVE_IMG_PATH, filename + ".jpg"), img)
