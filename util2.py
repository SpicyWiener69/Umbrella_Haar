import os
import shutil

folder_a = 'raw_a'
folder_b = 'raw_b'
folder_c = 'raw_c'
os.makedirs(folder_c, exist_ok=True)

# Normalize filenames for comparison (case-sensitive or insensitive as needed)
b_files = set(os.listdir(folder_b))

for fname in os.listdir(folder_a):
    if fname not in b_files:
        src_path = os.path.join(folder_a, fname)
        dst_path = os.path.join(folder_c, fname)
        shutil.copy2(src_path, dst_path)