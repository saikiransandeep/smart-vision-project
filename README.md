# 🔍 Smart Vision Projects

This repository contains a collection of mini computer vision applications built using **Python** and **OpenCV**. Each project demonstrates a unique visual detection or tracking capability — ranging from color segmentation and hand detection to pose estimation and interactive visual tools.

## 🚀 Projects Overview

### 🎨 ColourSegmentation.py  
Detects the red color in a real-time video stream using the HSV color model.

- Converts the frame to HSV color space.
- Applies a red color mask using `cv2.inRange`.
- Shows both the original and filtered output side-by-side.

> Press `q` to exit the video stream.

### ✋ handdetect.py  
Detects hands using contours and convexity defects to identify fingers.

- Uses thresholding and contour detection to locate the hand.
- Calculates the number of fingers using convex hulls and defects.
- Displays visual feedback on the live feed.

### 📏 HandDistanceBeep.py  
Calculates the distance between two points (e.g., fingers) and produces a beep if they are too close.

- Ideal for gesture control or touchless interaction.
- Measures proximity and triggers an audio beep when the threshold is reached.

### 🧥 invisible.py  
Implements an "invisibility cloak" illusion using background subtraction.

- Captures a static background at the start.
- Detects a specific color (like a red cloak).
- Replaces that color region with the background, creating a transparency effect.

### 🕺 posesegmentation.py  
Segments and visualizes human body poses using MediaPipe Pose.

- Detects landmarks like shoulders, elbows, knees, etc.
- Can be extended for fitness apps, gesture control, or motion tracking.

## 🛠️ Installation

Ensure Python 3.7+ is installed. Then run the following:

```bash
git clone 
cd 
pip install -r requirements.txt
