import decode.decodeHeader as dcH
import decode.Video_ext as dcE
import math


file ="myImage.bin"
bin_file = open(file,"rb")
sizeOFile = bin_file.seek(0,2)
#with open(file, "rb") as f:
#    byte = f.read(1)
#    while byte != b"":
        # Do stuff with byte.
#        byte = f.read(1)
#        print(byte)

#bin_data = bin_file.read()

print('Data length: ', sizeOFile, 'bytes')

header = dcH.decodeHeader(bin_file,sizeOFile)
value = 2040*80*32
new_val = math.floor(value/8)
sep_list = []
i = 0
while i <= sizeOFile:
    
    video = dcE.videoExt(bin_file,sizeOFile, i)
    sep_list.append(video)
    i = i + new_val
print (sep_list)
    
    
    

