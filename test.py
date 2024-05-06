import os
from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt

best_model = YOLO('best.pt')

image_dir = "C:\\Users\\PC\\Downloads\\Bus.jpg"
output_dir = "/results"

img = Image.open(image_dir)
result = best_model.predict(img, save=True)