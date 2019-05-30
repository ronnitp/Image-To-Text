import cv2
import numpy as np
import pytesseract
from PIL import Image
img = Image.open(r'/Users/Ronnit/Downloads/random.png') #Path to the image
#Mention the path to where tesseract has been installed on your system 
pytesseract.pytesseract.tesseract_cmd='/usr/local/Cellar/tesseract/4.0.0_1/bin/tesseract' 
r=pytesseract.image_to_string(img)
print(r)