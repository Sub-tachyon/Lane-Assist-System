import cv2

# Specify the device index for the USB camera (usually starts from 0)
# If you have multiple USB cameras, adjust the index accordingly
cap = cv2.VideoCapture(0)

def getImg(display=False, size=[480, 240]):
    _, img = cap.read()
    img = cv2.resize(img, (size[0], size[1]))
    if display:
        cv2.imshow('IMG', img)
    return img

if __name__ == '__main__':
    while True:
        img = getImg(True)
        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the VideoCapture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
