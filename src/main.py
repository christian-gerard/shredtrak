import cv2
import numpy as np

def main():
   # Initialize video capture object

    cap = cv2.VideoCapture(0)

    face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )



    while True:

        # Capture frame-by-frame

        ret, frame = cap.read()

        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



        # Display the resulting frame

        cv2.imshow('Laptop Cam', gray_image)



        # Press 'q' to exit

        if cv2.waitKey(1) & 0xFF == ord('q'):

            break



    # Release capture

    cap.release()

    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()