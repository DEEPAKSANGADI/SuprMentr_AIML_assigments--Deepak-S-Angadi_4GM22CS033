import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image
img = cv2.imread('image.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Edge detection
edges = cv2.Canny(blurred, 100, 200)

# Display before/after
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

axes[0, 0].imshow(img_rgb)
axes[0, 0].set_title('Original')
axes[0, 0].axis('off')

axes[0, 1].imshow(gray, cmap='gray')
axes[0, 1].set_title('Grayscale')
axes[0, 1].axis('off')

axes[1, 0].imshow(blurred, cmap='gray')
axes[1, 0].set_title('Blurred')
axes[1, 0].axis('off')

axes[1, 1].imshow(edges, cmap='gray')
axes[1, 1].set_title('Edges Detected')
axes[1, 1].axis('off')

plt.tight_layout()
plt.show()