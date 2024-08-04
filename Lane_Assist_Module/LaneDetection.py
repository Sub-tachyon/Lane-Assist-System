import cv2
import numpy as np
import utlis
from WebcamModule import getImg  # Import the getImg function from WebCamModule.py

curveList = []
avgVal = 10


def getLaneCurve(img, display=2):
    # Step 1
    imgcopy = img.copy()
    imgResult = img.copy()
    imgThreshold = utlis.thresholding(img)

    # Step 2
    hT, wT, c = img.shape   # height, width , no.of.channels
    points = utlis.valTrackbars()
    imgWarp = utlis.warpImg(imgThreshold, points, wT, hT)
    imgWarpPoints = utlis.drawpoints(imgcopy, points) # applies the points to copy of img

    # Step 3
    # This middle point serves as a reference for determining the position of the vehicle relative to the center of the lane.
    middlePoint, imgHist = utlis.getHistogram(imgWarp, display=True, minPer=0.5, region=4)
    # curvature of the lane
    curveAveragePoint, imgHist = utlis.getHistogram(imgWarp, display=True, minPer=0.9)
    curveRaw = curveAveragePoint - middlePoint

    # Step 4
    # We're doing average for smooth transition
    curveList.append(curveRaw)
    if len(curveList) > avgVal:
        curveList.pop(0)
    curve = int(sum(curveList) / len(curveList))

    # Step 5
    if display != 0:
        imgInvWarp = utlis.warpImg(imgWarp, points, wT, hT, inv=True)
        imgInvWarp = cv2.cvtColor(imgInvWarp, cv2.COLOR_GRAY2BGR)
        imgInvWarp[0:hT // 3, 0:wT] = 0, 0, 0
        imgLaneColor = np.zeros_like(img)
        imgLaneColor[:] = 0, 255, 0
        imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
        imgResult = cv2.addWeighted(imgResult, 1, imgLaneColor, 1, 0)
        midY = 450
        cv2.putText(imgResult, str(curve), (wT // 2 - 80, 85), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 3)
        cv2.line(imgResult, (wT // 2, midY), (wT // 2 + (curve * 3), midY), (255, 0, 255), 5)
        cv2.line(imgResult, ((wT // 2 + (curve * 3)), midY - 25), (wT // 2 + (curve * 3), midY + 25), (0, 255, 0), 5)
        for x in range(-30, 30):
            w = wT // 20
            cv2.line(imgResult, (w * x + int(curve // 50), midY - 10),
                     (w * x + int(curve // 50), midY + 10), (0, 0, 255), 2)

    if display == 2:
        imgStacked = utlis.stackImages(0.7, ([img, imgWarpPoints, imgWarp],
                                             [imgHist, imgLaneColor, imgResult]))
        cv2.imshow('ImageStack', imgStacked)
    elif display == 1:
        cv2.imshow('Resutlt', imgResult)
    curve = curve / 100
    if curve > 1:
        curve == 1  # normalization value lies between -1 to 1
    if curve < -1:
        curve == -1
    return curve


if __name__ == '__main__':
    # Create a VideoCapture object for the USB camera (device index 0)
    cap = cv2.VideoCapture(0)

    initialTrackBarVals = [102, 80, 20, 214]
    utlis.initializeTrackbars(initialTrackBarVals)

    frameCounter = 0
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0
        success, img = cap.read()  # Get the image (read the frames)
        img = cv2.resize(img, (480, 240))  # Resize
        curve = getLaneCurve(img, display=2)  # Display the video
        print(curve)
        cv2.imshow('vid', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
