import cv2
import numpy as np

# Open video file
cap = cv2.VideoCapture('video.mp4')

# Check if the video file is opened successfully
if not cap.isOpened():
    print("Error: Unable to open video file")
    exit()

# Read the first frame
ret, prev_frame = cap.read()
if not ret:
    print("Error: Unable to read the first frame from the video")
    exit()

# Convert the first frame to grayscale
prev_frame_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert current frame to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate dense optical flow using Farneback's method
    flow = cv2.calcOpticalFlowFarneback(prev_frame_gray, frame_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    # Compute the magnitude and angle of the 2D vectors
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])

    # Normalize the magnitude to range 0 to 1
    magnitude_norm = cv2.normalize(magnitude, None, 0, 1, cv2.NORM_MINMAX)

    # Angle of the vectors in degrees
    angle_deg = angle * (180 / np.pi / 2)

    # Create an HSV image where:
    # - Hue represents the direction of the flow
    # - Saturation is set to maximum
    # - Value represents the magnitude (speed) of the flow
    hsv = np.zeros_like(frame)
    hsv[..., 0] = angle_deg
    hsv[..., 1] = 255
    hsv[..., 2] = magnitude_norm * 255
    hsv = np.array(hsv, dtype=np.uint8)

    # Convert the HSV image to RGB for display
    rgb_flow = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

    # Display the resulting frame
    cv2.imshow('Dense Optical Flow in RGB', rgb_flow)

    # Update the previous frame to the current one for the next iteration
    prev_frame_gray = frame_gray

    # Break the loop if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()