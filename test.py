import os
from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt

image_dir = "C:\\Users\\PC\\Downloads\\Bus.jpg"
output_dir = "results"

best_model = YOLO('best.pt')
result = best_model(image_dir)

output_path = os.path.join(output_dir, "image_result.jpg")
print(output_path)

for i, r in enumerate (result):
    im_bgr = r.plot()
    im_rgb = Image.fromarray(im_bgr[..., ::-1]) # BGR to RGB
    r.show()
    r.save(output_path)