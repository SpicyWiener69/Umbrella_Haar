import cv2
import os

input_folder = 'raw_c'
output_folder = 'positive_c'
os.makedirs(output_folder, exist_ok=True)

for fname in os.listdir(input_folder):
    if not fname.lower().endswith(('.jpg', '.png', '.jpeg', '.bmp')):
        continue
    img_path = os.path.join(input_folder, fname)
    img = cv2.imread(img_path)
    resized = cv2.resize(img, (1080, 1920))  # Width × Height
    cv2.imwrite(os.path.join(output_folder, fname), resized)