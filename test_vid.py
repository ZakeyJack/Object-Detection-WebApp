import os
from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt

image_dir = "C:\\Users\\PC\\Downloads\\CCTV_Folder\\Simpang_Jlagran_day.mp4"
output_dir = "results"

best_model = YOLO('best.pt')
result = best_model.predict(image_dir, save=True, project='./results')