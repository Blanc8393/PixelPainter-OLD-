import os
from PIL import Image

directory = "Input"

def FileExists(filename):
    try:
        Image.open(filename)
        return True
    except:
        print("Invalid file name, please enter a valid file.\n")
        return False

def GetBlockDimensions(filename):
    userInput = input(f"Enter block dimensions for {filename} (w h) or \"s\" to skip:\n")
    if(userInput[0] == 's'):
        return 's'
    while(len(userInput) != 3):
        print(len(userInput))
        userInput = input("Only 2 arguments allowed. Enter width and height (w h)\n")
    return userInput.split()

def ConvertToPainting(dimensions, input):
    width = int(dimensions[0]) * 16
    height = int(dimensions[1]) * 16
    image = Image.open("Input/" + input)
    image = image.resize((width, height), Image.Resampling.BILINEAR)
    image = image.resize((width * 8, height * 8), Image.Resampling.NEAREST)
    noExt = input.partition(".")[0]
    image.save("Output/PXLPNT_" + noExt + ".png")

def SingleImage(filename):
    if(FileExists(filename)):
        dimensions = GetBlockDimensions()
        image = Image.open(filename)
        ConvertToPainting(dimensions, image)

def MultipleImages():
    for file in os.listdir(directory):
        dimensions = GetBlockDimensions(file)
        ConvertToPainting(dimensions, file)

def main():
    modePrompt = input("Single File (s) or Multiple Files (m)?\n")
    if(modePrompt == 's'):
        filename = input("Image name in Input folder:\n")
        SingleImage(filename)
    elif(modePrompt == 'm'):
        MultipleImages()
    else:
        print("Please select 's' or 'm'\n")
        

if(__name__ == "__main__"):
    main()