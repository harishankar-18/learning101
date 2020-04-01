from PIL import Image
from pylab import *
from scipy.ndimage import filters

img = array(Image.open('dog.jpg').convert('L'))
gray()

for i in range(1,10):
    img2 = filters.gaussian_filter(img, i)
    imshow(img2)
    x = Image.fromarray(uint8(img2))
    x.save('sigma'+str(i)+'.jpg')
show()
