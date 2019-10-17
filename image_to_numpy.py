import numpy as np
from PIL import Image
from glob import glob
    
x = np.array([np.array(Image.open(f).resize((200, 200))) for f in glob('photos/*.jpg')])
print(x.shape)

#pix =  glob("photos/*.jpg")

#lst = []
#for x in pix:

#imgarray = np.array(Image.open(x).resize((200, 200)))
#    lst.append(imgarray)

#k = np.array(lst)
#print(k.shape)



