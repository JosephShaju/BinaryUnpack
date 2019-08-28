import numpy as np
import cv2


file ="myImage.bin"
listval = []

def bytes_from_file(filename, chunksize=8192):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break

# example:
                
for b in bytes_from_file(file):
    listval.append(b)   
    
print (len(listval))