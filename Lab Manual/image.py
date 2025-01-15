import numpy as np
import imageio
import matplotlib.pyplot as plt
import imageio.v2 as imageio
# Load a colored image
image = imageio.imread('python.png')
# Convert the image to grayscale by averaging the RGB channels
# Weights for the RGB channels for grayscale conversion
weights = [0.2989, 0.5870, 0.1140]
grayscale_image = np.dot(image[..., :3], weights)
# Plot the original and grayscale images side by side
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(grayscale_image, cmap='gray')
plt.title('Grayscale Image')
plt.show()

