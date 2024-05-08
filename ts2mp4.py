import subprocess
from IPython.display import HTML
import os

folder_path = "C:\\Users\\zakin\\Documents\\GitHub\\Object-Detection-WebApp"
output_format = ".mp4"

for file in os.listdir(folder_path):
    if file.endswith(".mkv"):  # Check if the file is a TS file (the input format)
        video_file = os.path.join(folder_path, file)
        output_file = os.path.join(folder_path, file.replace(".mkv", output_format))
        
        # Use FFmpeg to convert the video
        command = f"ffmpeg -i {video_file} -c:v libx264 -crf 18 -c:a aac -b:a 128k {output_file}"
        print(f"Converting {file} to MP4...")
        os.system(command)