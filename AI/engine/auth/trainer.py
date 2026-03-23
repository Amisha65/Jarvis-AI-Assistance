import cv2
import numpy as np
from PIL import Image
import os

# Use absolute paths based on your directory
base_path = r'C:\Users\amish\OneDrive\Desktop\AI'
samples_path = os.path.join(base_path, 'engine', 'auth', 'samples')
cascade_path = os.path.join(base_path, 'engine', 'auth', 'haarcascade_frontalface_default.xml')
trainer_path = os.path.join(base_path, 'engine', 'auth', 'trainer', 'trainer.yml')

# Create face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load Haar cascade
detector = cv2.CascadeClassifier(cascade_path)

# Check if Haar cascade is loaded
if detector.empty():
    print("❌ Error loading Haar cascade. Check the path:", cascade_path)
    exit()

def Images_And_Labels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    print("Found images:", len(imagePaths))

    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        gray_img = Image.open(imagePath).convert('L')  # Grayscale
        img_arr = np.array(gray_img, 'uint8')

        try:
            id = int(os.path.split(imagePath)[-1].split(".")[1])
        except Exception as e:
            print(f"Skipping file (invalid name): {imagePath}")
            continue

        faces = detector.detectMultiScale(img_arr)

        for (x, y, w, h) in faces:
            faceSamples.append(img_arr[y:y + h, x:x + w])
            ids.append(id)

    return faceSamples, ids

print("Training faces. Please wait...")

faces, ids = Images_And_Labels(samples_path)

print("Total faces for training:", len(faces))
if len(faces) == 0:
    print("❌ No faces found. Make sure samples are valid.")
    exit()

# Train and save model
recognizer.train(faces, np.array(ids))
os.makedirs(os.path.dirname(trainer_path), exist_ok=True)
recognizer.write(trainer_path)

# Confirm save
if os.path.exists(trainer_path):
    print("Model trained and saved at:", trainer_path)
else:
    print("Failed to save the model.")
