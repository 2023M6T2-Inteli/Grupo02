# import the opencv library
import cv2
from ultralytics import YOLO
model = YOLO("./model_filtered.pt")

# define a video capture object
vid = cv2.VideoCapture(0)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    results = model.predict(frame, conf=0.7)

    # Display the resulting frame
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
