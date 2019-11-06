# Python program implementing Image Steganography 
import binascii
# PIL module is used to extract 
# pixels of image and modify it 
from PIL import Image 
  
def decode_image(file_location):
    ##################################### OUTPUT BINARY ##############################
    st = "ictf{Sirf_L0sB_se_Kaam_nhI_chlta}"
    ob = ""
    for o in st:
        m = ord(o)
        n = bin(m)[2:].zfill(8)
        ob = ob + n
    ob_length = len(ob)
    ob = ob + "000"
    ob_itr = 0


    #################################### IMAGE OPENING ################################
    i = Image.open(file_location)
    i = i.convert('RGB')
    x_size = i.width
    y_size = i.height
    print(x_size, y_size)
    #p = list(i.getdata())
    newimg = i.copy()
    p = ""

    for y in range(y_size):
        for x in range(x_size):
            r,g,b = newimg.getpixel((x,y))

            if ob_itr == ob_length:
                break

            b1 = bin(r)[2:].zfill(8)
            b2 = bin(g)[2:].zfill(8)
            b3 = bin(b)[2:].zfill(8)

            b1 = b1[:4] + ob[ob_itr] + b1[5:]
            b1 = int(b1,2)
            ob_itr+=1

            b2 = b2[:4] + ob[ob_itr] + b2[5:]
            b2 = int(b2,2)
            ob_itr+=1

            b3 = b3[:4] + ob[ob_itr] + b3[5:]
            b3 = int(b3,2)
            ob_itr+=1
            b4 = (b1,b2,b3)
            newimg.putpixel((x,y),b4)
    '''
    for i in range(0,len(p)-8,8):
        print(chr(int(p[i:i+8],2)),end="")
    img.save("newimg.png")
    '''
    newimg.save("newimg.png")
          
# Driver Code 
if __name__ == '__main__' : 
      
    # Calling main function 
    decode_image("forensics_1.jpg")