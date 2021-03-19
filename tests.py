from trdg.generators import GeneratorFromDict
import multiprocessing
import time
import os
import sys
import cv2
import numpy as np
numProcess = int(sys.argv[1])
numImageGen = int(sys.argv[2])
generator = [None] * numProcess
def gen(index):
    print("PID {0}: {1}".format(index, os.getpid()))
    count = numImageGen // numProcess
    if index == 0:
        count = count + (numImageGen % numProcess)
    generator[index] = GeneratorFromDict(count=count)
    with open("filenames.txt", 'a') as fileObj:
        for img, lbl in generator[index]:
            fileObj.write(img[1] + " " + lbl + "\n")

if __name__ == "__main__":
    t = time.time()
    print("Generating {0} image with {1} processes.".format(numImageGen, numProcess))
    mylist = []
    for i in range(numProcess):
        mylist.append(i)

    p = multiprocessing.Pool(numProcess)

    p.imap(gen, mylist)
    p.close()
    p.join()

    print("Elapse time: ", time.time() - t)