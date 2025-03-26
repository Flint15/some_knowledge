# Import necessary libraries
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Read the image using Pillow
image_path = 'image.png' # replace with your image path 
img = Image.open(image_path)

# Convert image to numpy array
img_array = np.array(img)

# function that make convertation
def grayscaling(rgb):
  # Calculate grayscale value
  return int(0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2])

# Create a new list for gray Image
gray_array = np.zeros((img_array.shape[0], img_array.shape[1]), dtype=np.uint8)

# Iterate over each pixel and convert to grayscale
for i in range(img_array.shape[0]):
  for j in range(img_array.shape[1]):
    gray_array[i, j] = grayscaling(img_array[i, j])

# Convert the numpy array back to an image
gray_image = Image.fromarray(gray_array, mode='L')
