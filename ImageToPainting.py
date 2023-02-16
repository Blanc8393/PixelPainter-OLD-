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
        image.save("Output/MCPaint_" + file + ".png")
        image = image.resize((width, height), Image.Resampling.BILINEAR)
        image = image.resize((image.width * 8, image.height * 8), Image.Resampling.NEAREST)
        image.save("Output/MCPaint_" + file + ".png")