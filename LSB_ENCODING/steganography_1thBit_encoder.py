# Python program implementing Image Steganography 
import binascii
# PIL module is used to extract 
# pixels of image and modify it 
from PIL import Image 
  
file_location = "forensics_3.png"
qr_location = "qrcode.png"

#################################### IMAGE OPENING ################################
i = Image.open(file_location)
qr_img = Image.open(qr_location)


##################################### OUTPUT BINARY ##############################
'''
st = "ictf{Sirf_L0sB_se_Kaam_nhI_chlta}"
ob = ""
for o in st:
    m = ord(o)
    n = bin(m)[2:].zfill(8)
    ob = ob + n
ob_length = len(ob)
ob = ob + "000"
ob_itr = 0
'''
ob = ""
qr_byte = (list(qr_img.getdata()))
qr_length = len(qr_byte)
for ii in range(qr_length):
    ob = ob + bin(qr_byte[ii])[2:]
ob_length = len(ob)
ob = ob + "000"
ob_itr=0


i = i.convert('RGB')
x_size = i.width
y_size = i.height
print(x_size, y_size)
#p = list(i.getdata())
newimg = i.copy()
p = ""

y_size = 2
for y in range(y_size):
    for x in range(x_size):
        r,g,b = newimg.getpixel((x,y))

        if ob_itr == ob_length:
            break

        b1 = bin(r)[2:].zfill(8)
        b2 = bin(g)[2:].zfill(8)
        b3 = bin(b)[2:].zfill(8)

        b1 = b1[:7] + ob[ob_itr]
        b1 = int(b1,2)
        ob_itr+=1

        b2 = b2[:7] + ob[ob_itr]
        b2 = int(b2,2)
        ob_itr+=1

        b3 = b3[:7] + ob[ob_itr]
        b3 = int(b3,2)
        ob_itr+=1
        b4 = (b1,b2,b3)
        newimg.putpixel((x,y),b4)
'''
for i in range(0,len(p)-8,8):
    print(chr(int(p[i:i+8],2)),end="")
img.save("newimg.png")
'''
newimg.save("forensics_3_merged_qr.png")
      
