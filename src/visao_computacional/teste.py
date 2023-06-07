import cv2
from ultralytics import YOLO

# Load a model

# load a pretrained model (recommended for training)
model = YOLO("./model_filtered.pt")


# predict on an image
results = model.predict(
    "https://www.zapimoveis.com.br/blog/wp-content/uploads/2015/03/shutterstock_147905213.jpg", conf=0.6)

# save result
image = results[0].plot()
print(results.__len__())

cv2.imshow("teste", image)
cv2.waitKey(0)
