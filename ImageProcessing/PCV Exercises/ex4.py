import matplotlib.pylab as plt
from skimage.io import imread
from skimage.color import rgb2gray
from skimage import filters

im = array(Image.open("dog.jpg").convert('L'))

imx = pl.zeros(im.shape)
filters.sobel(im,1,imx)

imy = pl.zeros(im.shape)
filters.sobel(im,0,imy)

magnitude = pl.sqrt(imx**2+imy**2)

plt.imshow(magnitude)
plt.title('sobel', size=20)
plt.show()
