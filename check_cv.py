import cv2

# Check if 'detectMultiScale' function is available in cv2
if 'detectMultiScale' in dir(cv2):
    print("detectMultiScale function is available in cv2")
else:
    print("detectMultiScale function is not available in cv2")
