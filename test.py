from trdg.generators import GeneratorFromDict
import multiprocessing
import time
import os
import cv2
import numpy as np
numThread = 6
generator = [None] * numThread
def gen(index):
    print("PID {0}: {1}".format(index, os.getpid()))
    generator[index-1] = GeneratorFromDict(count=1000)
    with open("filenames.txt", 'w') as fileObj:
        for img, lbl in generator[index-1]:
            pass
            #fileObj.write(img[1] + " " + lbl + "\n")

if __name__ == "__main__":
    t = time.time()
    p1 = multiprocessing.Process(target=gen, args=(1, ))
    p2 = multiprocessing.Process(target=gen, args=(2, ))
    p3 = multiprocessing.Process(target=gen, args=(3, ))
    p4 = multiprocessing.Process(target=gen, args=(4, ))
    p5 = multiprocessing.Process(target=gen, args=(5,))
    p6 = multiprocessing.Process(target=gen, args=(6,))





    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()






    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()





    print("Elapse time: ", time.time() - t)