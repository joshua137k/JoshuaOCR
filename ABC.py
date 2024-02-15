import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2

def create_folders(root_folder):
    if not os.path.exists(root_folder):
        os.makedirs(root_folder)

    for letter in range(65, 91):
        folder_name = chr(letter)
        folder_path = os.path.join(root_folder, folder_name)
        os.makedirs(folder_path)
        print(f"Folder '{folder_name}' created in '{root_folder}'.")

def create_image_with_letter(folder):
    letters = [chr(letter) for letter in range(65, 91)]
    font = ImageFont.truetype('arial.ttf', size=24)

    for letter in letters:
        folder_path = os.path.join(folder, letter)
        os.makedirs(folder_path, exist_ok=True)

        image_pil = Image.new('RGB', (100, 100), color=(255, 255, 255))
        draw = ImageDraw.Draw(image_pil)
        text_width, text_height = draw.textsize(letter, font=font)
        draw.text(((100 - text_width) // 2, (100 - text_height) // 2), letter, font=font, fill=(0, 0, 0))

        image_cv = np.array(image_pil)
        image_cv = image_cv[:, :, ::-1].copy()

        gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
        _, binarized = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

        contours, _ = cv2.findContours(binarized, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        x, y, w, h = cv2.boundingRect(contours[0])

        cropped_image = image_cv[y:y+h, x:x+w]

        image_path = os.path.join(folder_path, f'{letter}.png')
        cv2.imwrite(image_path, cropped_image)

if __name__ == "__main__":
    root_folder = "ABC"
    #create_folders(root_folder)
    create_image_with_letter(root_folder)

