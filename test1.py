from trdg.generators import (
    GeneratorFromDict,
    GeneratorFromRandom,
    GeneratorFromStrings,
    GeneratorFromWikipedia,
)
import numpy as np
import cv2

# The generators use the same arguments as the CLI, only as parameters
generator = GeneratorFromStrings(
    ['Test1', 'Test2', 'Test3'],
    blur=2,
    count = 10,
    random_blur=True
)

for img, lbl in generator:
    #print(img)
    print(lbl)
    print(np.array(img))
    #print(im)
    #cv2.imshow("img", im)
    #cv2.waitKey(2000)