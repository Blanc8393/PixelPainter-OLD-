import os
import tkinter as tk
from tkinter import filedialog

from PIL import Image

INPUT_FOLDER = ""
INPUT_IMAGE = ""
OUTPUT_FOLDER = ""
NAME_EACH = ""
IS_FOLDER = ""

#Setting to folder or single mode
def SetIsFolder():

    global IS_FOLDER
    selection = input("Folder of images, single image, or cancel?\nf/s/c: ")
    
    while(True):
        if(selection == 'f'):
            IS_FOLDER = True
            return

        elif(selection == 's'):
            IS_FOLDER = False
            return

        elif(selection == 'c'):
            print("Cancelling...")
            exit()

        else:
            print("Please choose 'f', 's', or 'c'")

#Setting naming mode
def SetNameEach():

    global NAME_EACH
    selection = input("Would you like to rename your image(s)?\ny/n: ")
    
    while(True):
        
        if(selection == 'y'):
            NAME_EACH = True
            return
        elif(selection == 'n'):
            NAME_EACH = False
            return
        else:
            selection = input("Please enter 'y' or 'n': ")

def ValidateImage():
    try:
        Image.open(INPUT_IMAGE)
        return True
    except IOError:
        print(f"\n{INPUT_IMAGE} is not a valid image.\n")
        return False

#Set input FOLDER or IMAGE (Image is validated)
def SetInput():
    global IS_FOLDER
    global INPUT_FOLDER
    global INPUT_IMAGE

    root = tk.Tk()
    root.withdraw()

    if(IS_FOLDER):
        print("Choose a folder")
        INPUT_FOLDER = filedialog.askdirectory()
        return
    else:
        print("Choose a file")
        while(True):
            INPUT_IMAGE = filedialog.askopenfile().name
            if(ValidateImage() == True):
                return

#Set Output Folder  
def SetOutput():
    global OUTPUT_FOLDER
    print("Choose an output folder")
    OUTPUT_FOLDER = filedialog.askdirectory()
    return

#Get desired dimensions (in blocks) of final painting
def GetBlockDimensions(path):
    filename = os.path.basename(path)
    userInput = input(f"Enter block dimensions for {filename} (w h) or \"s\" to skip: ")

    if(userInput[0] == 's'):
        return 's'
    while(len(userInput) != 3):
        print(len(userInput))
        userInput = input("Only 2 arguments allowed. Enter width and height (w h)\n")
    return userInput.split()

def ImageToPainting(dimensions, file):
    filename = os.path.basename(file)
    noExt = filename.partition(".")[0]
    image = Image.open(file)
    width = int(dimensions[0]) * 16
    height = int(dimensions[1]) * 16
    painting = image.resize((width, height), Image.Resampling.BILINEAR)
    painting = painting.resize((width * 8, height * 8), Image.Resampling.NEAREST)

    if(NAME_EACH == True):
        newName = input("Enter new name for \"" + filename + "\", excluding file extensions: ")
        painting.save(OUTPUT_FOLDER + "/PXLPNT_" + newName + ".png")
        return
    painting.save(OUTPUT_FOLDER + "/PXLPNT_" + noExt + ".png")

def ConvertAndSave():
    global IS_FOLDER
    global INPUT_FOLDER
    global OUTPUT_FOLDER
    global INPUT_IMAGE

    if(IS_FOLDER):
        for file in os.listdir(INPUT_FOLDER):
            dimensions = GetBlockDimensions(file)
            if(dimensions != 's'):
                ImageToPainting(dimensions, INPUT_FOLDER + "/" + file)
    else:
        file = INPUT_IMAGE
        dimensions = GetBlockDimensions(INPUT_IMAGE)
        if(dimensions != 's'):
                ImageToPainting(dimensions, file)

def main():
    SetIsFolder()
    SetInput()
    SetOutput()
    SetNameEach()
    ConvertAndSave()
        

if(__name__ == "__main__"):
    main()