import cv2
import numpy as np

def main():
   # Initialize video capture object

    cap = cv2.VideoCapture(0)



    while True:

        # Capture frame-by-frame

        ret, frame = cap.read()



        # Display the resulting frame

        cv2.imshow('Webcam', frame)



        # Press 'q' to exit

        if cv2.waitKey(1) & 0xFF == ord('q'):

            break



    # Release capture

    cap.release()

    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()