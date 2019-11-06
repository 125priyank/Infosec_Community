# Python program implementing Image Steganography 
import binascii
# PIL module is used to extract 
# pixels of image and modify it 
from PIL import Image 
  
def decode_image(file_location):



    #################################### IMAGE OPENING ################################
    i = Image.open(file_location)
    i = i.convert('RGB')
    x_size = i.width
    y_size = i.height
    print(x_size, y_size)
    #p = list(i.getdata())
    newimg = i.copy()
    p = ""

    y_size = 1
    for y in range(y_size):
        for x in range(x_size):
            r,g,b = newimg.getpixel((x,y))

            b1 = bin(r)[2:].zfill(8)
            b2 = bin(g)[2:].zfill(8)
            b3 = bin(b)[2:].zfill(8)

            p = p + str(b1[4]) + str(b2[4]) + str(b3[4])
    
    for i in range(0,len(p)-8,8):
        print(chr(int(p[i:i+8],2)),end="")
    
    #newimg.save("newimg.png")
          
# Driver Code 
if __name__ == '__main__' : 
      
    # Calling main function 
    decode_image("forensics_1_final.png")