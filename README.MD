# Color Detection Using OpenCV in HSV Color Space

## Overview

This project demonstrates color detection using OpenCV in the HSV (Hue, Saturation, Value) color space. It captures video from a webcam or camera and identifies specific colors within the frame, highlighting them with bounding boxes.

![hsv colorspace](images/hsv.jfif)

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Color Detection](#color-detection)
- [Demo](#demo)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Webcam or camera (for live color detection)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/color-detection.git
   ```

2. Navigate to the project directory:

   ```bash
   cd color-detection
   ```

3. Install the required Python libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the color detection script:

   ```bash
   python color_detection.py
   ```

   This will open a window displaying the video feed from your webcam or camera.

2. Point the camera towards objects of the color you want to detect. The script will highlight those colors with bounding boxes.

3. To exit the script, press the 'Q' key.

## Color Detection

In this project, color detection is performed in the following steps:

1. Capture video from the webcam or camera.

2. Convert each frame to the HSV color space using `cv2.cvtColor()`.

3. Define the lower and upper HSV color bounds for the color you want to detect.

4. Create a mask using `cv2.inRange()` to isolate pixels within the color range.

5. Find contours in the mask and draw bounding boxes around the detected areas.

6. Display the original frame with bounding boxes on the objects of the detected color.

