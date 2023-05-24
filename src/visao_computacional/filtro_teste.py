import cv2
import numpy as np

def teste(db):
    dataset = db
    new_db = []
    for i in dataset:
        image = cv2.imread(i)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        kernel2 = np.array([[2.0, 0.0, -1.0],
        [0.0, 1.0, 0.0],
        [2.0, 0.0, -2.0]], dtype=np.float32)
        filtered = cv2.filter2D(gray_image, -1, kernel2)
        new_db.append(filtered)
    return new_db



