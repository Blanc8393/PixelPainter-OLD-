import os
from PIL import Image

directory = "Input"

for file in os.listdir(directory):
    userInput = input(f"Enter block dimensions for {file} (w h) or \"s\" to skip:\n")
    dimensions = userInput.split()
    if(dimensions[0] != "s"):
        width = int(dimensions[0]) * 16
        height = int(dimensions[1]) * 16
        image = Image.open("Input/" + file)
        image = image.resize((width, height), resample=Image.Resampling.BILINEAR)
        image = image.resize((width * 128, height * 128), Image.Resampling.NEAREST)
        image.save("Output/MCPaint_" + file)