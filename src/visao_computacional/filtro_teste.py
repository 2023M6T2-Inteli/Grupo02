import cv2
import numpy as np
import os

def filter(db):
    dataset = os.listdir(db)

    for name in dataset:
        image = cv2.imread(f"{db}/{name}")
        print(f"{db}/{name}")
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        kernel2 = np.array([[2.0, 0.0, -1.0],
        [0.0, 1.0, 0.0],
        [2.0, 0.0, -2.0]], dtype=np.float32)
        filtered = cv2.filter2D(gray_image, -1, kernel2)
        
        cv2.imwrite(f'{db}/{name}', filtered)
        print("filtro aplicado" +db+name)



