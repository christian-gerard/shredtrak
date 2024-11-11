import cv2
import numpy as np

def main():
   # Initialize video capture object

    cap = cv2.VideoCapture(0)

    face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )


    while True:

        ret, frame = cap.read()

        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face = face_classifier.detectMultiScale(
            gray_image, scaleFactor=1.1, minNeighbors=9, minSize=(100, 100)
        )

        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)


        # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), -1)  # Blue overlay
        # alpha = 0.4  # Transparency factor
        # image = cv2.addWeighted(frame, alpha, , 1 - alpha, 0)

        cv2.imshow('Laptop Cam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()

    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()