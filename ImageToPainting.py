import os
from PIL import Image

def CreateFolders():
    try:
        os.mkdir("Input")
    except FileExistsError:
        pass

    try:
        os.mkdir("Output")
    except FileExistsError:
        pass

def ImageExists(filename):
    try:
        img = Image.open("Input/" + filename)
        return True
    except IOError:
        print(f"\n{filename} is an invalid image.\n")
        return False

def GetBlockDimensions(filename):
    userInput = input(f"Enter block dimensions for {filename} (w h) or \"s\" to skip: ")
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
    if(ImageExists(filename)):
        dimensions = GetBlockDimensions()
        image = Image.open(filename)
        ConvertToPainting(dimensions, image)

def MultipleImages():
    for file in os.listdir("Input"):
        if(ImageExists(file)):
            dimensions = GetBlockDimensions(file)
            ConvertToPainting(dimensions, file)

def main():
    CreateFolders()
    modePrompt = input("Single File (s) or Multiple Files (m)? ")
    if(modePrompt == 's'):
        filename = input("Image name in Input folder:\n")
        SingleImage(filename)
    elif(modePrompt == 'm'):
        MultipleImages()
    else:
        print("Please select 's' or 'm'\n")
        

if(__name__ == "__main__"):
    main()