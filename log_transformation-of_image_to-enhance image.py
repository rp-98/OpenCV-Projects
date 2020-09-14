import cv2
import numpy as np

video=cv2.VideoCapture(0)
while True:
    ret,frame=video.read()
    image=frame
    # Apply log transformation method
    c = 255 / np.log(1 + np.max(image))
    log_image = c * (np.log(image + 1))
    # float value will be converted to int
    log_image = np.array(log_image, dtype=np.uint8)
    cv2.imshow('original',frame)
    cv2.imshow('log_transfored_image',log_image)
    if cv2.waitKey(1)==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
