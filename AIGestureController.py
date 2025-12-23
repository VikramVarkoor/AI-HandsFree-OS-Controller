import cv2
import os
import pyautogui

# Load the built-in Face Detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Mirror view
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    h, w, _ = img.shape
    center_x = w // 2
    deadzone = 50  # Area in the middle where nothing happens

    # Draw the "Deadzone" lines for the demo
    cv2.line(img, (center_x - deadzone, 0), (center_x - deadzone, h), (255, 255, 255), 1)
    cv2.line(img, (center_x + deadzone, 0), (center_x + deadzone, h), (255, 255, 255), 1)

    for (x, y, fw, fh) in faces:
        # Calculate the center of the detected face
        face_center = x + (fw // 2)
        cv2.rectangle(img, (x, y), (x + fw, y + fh), (255, 0, 0), 2)
        cv2.circle(img, (face_center, y + fh // 2), 5, (0, 0, 255), -1)

        # Logic based on head position
        if face_center < center_x - deadzone:
            cv2.putText(img, "<- VOLUME DOWN", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            os.system("osascript -e 'set volume output volume (output volume of (get volume settings) - 5)'")
        elif face_center > center_x + deadzone:
            cv2.putText(img, "VOLUME UP ->", (w - 300, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            os.system("osascript -e 'set volume output volume (output volume of (get volume settings) + 5)'")

    cv2.imshow('Face Gesture Controller', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()