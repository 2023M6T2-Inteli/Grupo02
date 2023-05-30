# import the opencv library
import cv2
from ultralytics import YOLO
import time
model = YOLO("./model_filtered.pt")

# define a video capture object
vid = cv2.VideoCapture(0)
saved_images = []
while (True):
    time.sleep(1/30)
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    results = model.predict(frame, conf=0.6)

    # Display the resulting frame

    if len(results[0]) > 0:

        saved_images.append(results[0].plot())

    image = results[0].plot()
    cv2.imshow('frame', image)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()


for i in range(len(saved_images)):

    cv2.imshow(f'frame {i} de len', saved_images[i])
    if cv2.waitKey(0) & 0xFF == ord('a'):
        break

    cv2.destroyAllWindows()
