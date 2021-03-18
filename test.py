from trdg.generators import GeneratorFromDict
import cv2
import numpy as np

generator = GeneratorFromDict()

for img, lbl in generator:
    pass
    #im = np.array(img)
    #cv2.imshow("img", im)
    #cv2.waitKey(2000)
