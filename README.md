# Smart Lane Detection 🚗 and Color Picker 🔴🟡🟢

## Overview

This project includes scripts for detecting lanes in video feeds and selecting colors using a trackbar interface. The project is composed of four main Python scripts:

1. **ColorPickerScript.py**: Allows you to pick colors from a video feed using HSV trackbars.
2. **LaneDetection.py**: Detects and tracks lane curves in video feeds from a USB camera.
3. **WebcamModule.py**: Provides functionality to capture images from a USB camera.
4. **utlis.py**: Contains utility functions used by the other scripts.

## Usage

### 1. ColorPickerScript.py

This script helps in selecting colors from a video feed. It provides HSV (Hue, Saturation, Value) trackbars to filter colors.

**Usage:**

1. Connect a camera to your computer.
2. Run the script.
3. Adjust the HSV trackbars to select the desired color.
4. The script will show the original video, the mask of the selected color, and the result of applying the mask.
   
Note: You can also use a video file (vid1.mp4) instead of a live camera feed by modifying the script.

### 2. LaneDetection.py

This script detects lane curves in real-time from a USB camera feed.

**Usage:**

1. Connect a USB camera to your computer.
2. Ensure you have set initial trackbar values in `utlis.py`.
3. Run the script.
4. The script will show the video feed with lane detection and curve information.


### 3. WebcamModule.py

This module provides a function to capture images from a USB camera.

**Usage:**

1. Connect a USB camera to your computer.
2. Import the `getImg` function in your script:
3. Use the getImg function to capture and optionally display images from the camera.

### 4. utlis.py

This file contains utility functions for image processing and lane detection. Functions include:

- **`thresholding(img)`**: Applies a threshold to detect white areas in the image.
- **`warpImg(img, points, w, h, inv=False)`**: Applies a perspective warp to an image.
- **`initializeTrackbars(initialTrackBarVals, wT=480, hT=240)`**: Initializes trackbars for adjusting perspective warp points.
- **`valTrackbars(wT=480, hT=240)`**: Retrieves current values from trackbars.
- **`drawpoints(img, points)`**: Draws perspective warp points on an image.
- **`getHistogram(img, minPer=0.1, display=False, region=1)`**: Computes and optionally displays the histogram for lane detection.
- **`stackImages(scale, imgArray)`**: Stacks multiple images into a single image.


## Thank You, Happy coding!...

   

