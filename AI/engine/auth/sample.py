import cv2
import os

# Initialize camera
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 640)  # Width
cam.set(4, 480)  # Height

# Make sure the samples directory exists
samples_dir = os.path.join(os.path.dirname(__file__), 'samples')
os.makedirs(samples_dir, exist_ok=True)

# Load the Haar Cascade for face detection
cascade_path = os.path.join(os.path.dirname(__file__), 'haarcascade_frontalface_default.xml')
detector = cv2.CascadeClassifier(cascade_path)

# Get user input
face_id = input("Enter a Numeric user ID here: ")
print("Taking samples, look at the camera...")

count = 0  # Count of saved samples

while True:
    ret, img = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        face_img = gray[y:y+h, x:x+w]
        
        # Save face sample into the samples folder
        file_path = os.path.join(samples_dir, f"face.{face_id}.{count}.jpg")
        cv2.imwrite(file_path, face_img)

        # Draw rectangle around face
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Show the live image with face rectangle
    cv2.imshow('image', img)

    # Break conditions
    k = cv2.waitKey(100) & 0xff
    if k == 27:  # ESC key to stop
        break
    elif count >= 100:  # 100 face samples per user
        break

# Cleanup
print("Samples taken. Closing the program...")
cam.release()
cv2.destroyAllWindows()
