from trdg.generators import GeneratorFromDict
import cv2
import numpy as np

generator = GeneratorFromDict(count = 10)
with open("filenames.txt", 'w') as fileObj:
    for img, lbl in generator:
        fileObj.write(img[1] + " " + lbl + "\n")

    

