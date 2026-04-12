import cv2
import numpy as np

# Load the image
image = cv2.imread('image.jpg')

# Print shape
print(f"Shape: {image.shape}")

# Print pixel values (first 5x5 region)
print(f"Pixel values (first 5x5):\n{image[:5, :5]}")

# Print channels
print(f"Number of channels: {image.shape[2]}")
print(f"Channel names: BGR (Blue, Green, Red)")

# Print data type and value range
print(f"Data type: {image.dtype}")
print(f"Min value: {image.min()}, Max value: {image.max()}")

# Explanation
print("\nExplanation:")
print(f"- Shape {image.shape}: (height, width, channels)")
print(f"- Pixel values: integers 0-255 representing color intensity")
print(f"- Channels: 3 channels (B, G, R) - OpenCV uses BGR not RGB")