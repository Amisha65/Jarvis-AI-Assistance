import os
import cv2
import pyautogui as p

def AuthenticateFace():
    flag = ""

    # Local Binary Patterns Histograms recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Read the trained model using a relative path
    model_path = os.path.join(os.path.dirname(__file__), 'engine', 'auth', 'trainer', 'trainer.yml')
    recognizer.read(model_path)

    # Load the Haar cascade file using a relative path
    cascadePath = os.path.join(os.path.dirname(__file__), 'haarcascade_frontalface_default.xml')
    
    # Check if Haar cascade is loaded
    faceCascade = cv2.CascadeClassifier(cascadePath)
    if faceCascade.empty():
        print("Error: Haar cascade file not loaded. Check the path.")
        return 0

    font = cv2.FONT_HERSHEY_SIMPLEX  # Font for text

    names = ['', '','','','Amisha']  # Make sure 'Amisha' matches ID 1
    id = 4  # Dummy initialization

    # Start webcam capture
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)  # width
    cam.set(4, 480)  # height

    # Minimum window size for detection
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()
        if not ret:
            print("Error: Failed to access webcam.")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            id, accuracy = recognizer.predict(gray[y:y+h, x:x+w])
            confidence = 100 - accuracy

            if confidence >= 30:
                name = "Amisha"
                flag = 1
            else:
                name = "unknown"
                flag = 0

            cv2.putText(img, str(name), (x+5, y-5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, f"{round(confidence)}%", (x+5, y+h-5), font, 1, (255, 255, 0), 1)

            cv2.putText(img, str(name), (x+5, y-5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, f"{round(confidence)}%", (x+5, y+h-5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff
        if k == 27 or flag == 1:  # ESC or recognized
            break

    cam.release()
    cv2.destroyAllWindows()
    return flag
