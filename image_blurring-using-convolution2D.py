import cv2
import numpy as np
video=cv2.VideoCapture(0)
while True:
    ret,frame=video.read()
    # Write Python3 code here
    image=frame
    # making filter of 3 by 3 filled with 1 divide
    # by 9 for normalization
    blur_filter1 = np.ones((3, 3), np.float) / (9.0)

    # making filter of 5 by 5 filled with 1 divide
    # by 25 for normalization
    blur_filter2 = np.ones((5, 5), np.float) / (25.0)

    # making filter of 7 by 7 filled with 1 divide
    # by 49 for normalization
    blur_filter3 = np.ones((7, 7), np.float) / (49.0)

    image_blur1 = cv2.filter2D(image, -1, blur_filter1)
    image_blur2 = cv2.filter2D(image, -1, blur_filter2)
    image_blur3 = cv2.filter2D(image, -1, blur_filter3)

    cv2.imshow('geek', image)
    cv2.imshow('geek_blur1', image_blur1)
    cv2.imshow('geek_blur2', image_blur2)
    cv2.imshow('geek_blur3', image_blur3)

    cv2.imshow('ravi',frame)
    if cv2.waitKey(1)==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
