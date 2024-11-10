import cv2
import numpy as np

def main():
    # Load an image as an example
    img = cv2.imread('../data/sample_image.jpg', cv2.IMREAD_COLOR)
    cv2.imshow('Sample Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()