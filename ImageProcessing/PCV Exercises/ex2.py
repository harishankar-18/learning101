from PIL import Image
from pylab import *
from scipy.ndimage import filters

img = array(Image.open('dog.jpg').convert('L'))

img_gaussian = filters.gaussian_filter(img, 10)
i = 0.2
while(i <=0.7):
    img_sharp = (img - img_gaussian)*i +img
    x = Image.fromarray(uint8(img_sharp))
    x.save('image'+str(i)+'.jpg')
    i = i+ 0.1
    
