import cv2
import numpy as np
video=cv2.VideoCapture(0)
while True:
    ret,frame=video.read()
    image=frame
    # Store height and width of the image
    height, width = image.shape[:2]

    quarter_height, quarter_width = height / 4, width / 4

    T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])

    # We use warpAffine to transform
    # the image using the matrix, T
    img_translation = cv2.warpAffine(image, T, (width, height))


    cv2.imshow('shifted',img_translation)

    cv2.imshow('ravi',frame)
    if cv2.waitKey(1)==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
