import matplotlib.pylab as plt
from skimage.io import imread
from skimage.color import rgb2gray
from skimage import filters

im = array(Image.open("dog.jpg").convert('L'))

edges = filters.sobel(im)
plt.imshow(edges)
plt.title('sobel', size=20)
plt.show()
