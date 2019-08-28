import struct
import math

def decodeHeader(bin_file,byte):
    """
    This function will parse the data in the binary video
    The function will not detect any parameters it will only parse the data
    based on the given template.
    header data = 11 * 32bit (I unsigned int) + 6 * 32 bit (f float)
    note that each header name is actually 64 bits, however due to unkown coding
    on the part if the video capture program the 2nd half of each 64 bit packet 
    is actually junk data. So we read in packs of 32, and ignore every other data 
    packet. Luckily just by looking at the values you can tell what is real data. 
    Note the with the gain value, it wasn't actually 0, due to some sort of 
    percision problem it was 10**-35 which I just set equal to 0. 
    
    INPUT:
        The actual data to be  decoded (you dont need to send in the full file,
        technically the first 544 bits(68 bytes) are needed for the header data.)
    OUTPUT:
        A dictionary type with the header names and their respective values.
        Note vid_duration is actually calculated by the program.
        
        Sample:
            Data length:  68 bytes
            bitDepth : 16
            rangeMax : 4095
            width : 2040
            height : 80
            numFrame : 4202
            vDecim : 1
            exposure : 0
            gain : 0
            blackLevel : 0
            fps : 840*
            
            *fps is at the end of the file and is a double type (64 bit)
    Possible error: 
        Basically if the input file isnt correct nothing will work propery & most
        likely you will get very large and non-sence numbers.
        If the error is: 
            unpack_from requires a buffer of at least 24 bytes (or any other number)
        You have most likely inputed less than 68 bytes from the file (so check you file) as
        it may be corrupted, or you just changed the file.read() function in main.
        
    """
    #Header will be  loaded in two parts the first 6 are u-int format
    #the last 3 will be float 
    #note that the data is comprised of the first 32 bits as data and the second 
    #is junk. 
    #we will only read the minimum amount of data 
    bin_file.seek(0,0)
    data = bin_file.read(68)
    temp = struct.unpack('11I',data[4*0:4*11])
    #np.set_printoptions(4,1000,3,75,True,'int') Only needed if we are using np
    # it will remove the sci-not. 
    header = []
    for i in temp[0:11:2]:
        header.append(i)
        
    temp = struct.unpack_from('6f',data[:4*17],11*4)
    for i in temp[1:6:2]:
        header.append(i)
        
    x = 0    
    for i in header:
        if -0.01<i and i<0.01:
            header[x] =abs(0)
        x = x+1
    bin_file.seek(-8,2)
    data = bin_file.read()
    temp = struct.unpack('d',data[:])
    header.append(math.floor(temp[0]))
    header.append(round(header[4]/header[9],2)) #numFrame / fps
    
    header_name = []
    header_name.append('bitDepth')
    header_name.append('rangeMax')
    header_name.append('width')
    header_name.append('height')
    header_name.append('numFrame')
    header_name.append('vDecim')
    header_name.append('exposure')
    header_name.append('gain')
    header_name.append('blackLevel')
    header_name.append('fps')
    header_name.append('vid_dur')
    header = dict(zip(header_name,header))
    for x in header:
        print(x,':',header[x])
        
        
    return header
