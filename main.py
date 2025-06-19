import cv2
import os

# Load cascade
cascade = cv2.CascadeClassifier('cascade/cascade.xml')

# Path to ground truth file
txt_file = 'validation/truth.txt'

# Read and validate
with open(txt_file, 'r') as f:
    lines = f.readlines()

correct = 0
total = 0

for line in lines:
    path, label = line.strip().split()
    path = os.path.join('validation', path)
    label = int(label)
    
    img = cv2.imread(path)
    if img is None:
        print(f'[ERROR] Cannot read: {path}')
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detections = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    
    detected = int(len(detections) > 0)
    is_correct = detected == label
    if is_correct:
        correct += 1
    total += 1

    result = 'CORRECT' if is_correct else 'WRONG'
    print(f'{path} | GT: {label} | Detected: {detected} | {result}')

# Report accuracy
if total > 0:
    accuracy = correct / total * 100
    print(f'\nAccuracy: {correct}/{total} = {accuracy:.2f}%')
else:
    print('No valid samples processed.')