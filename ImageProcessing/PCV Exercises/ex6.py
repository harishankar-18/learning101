from PIL import Image
from scipy.ndimage import measurements,morphology
from numpy import *
from pylab import *

img = array(Image.open('dog.jpeg').convert('L'))
img = 1*(im<120)

lbls, nbr_obj = measurements.label(img)
imshow(img)
figure()
hist(img.flatten(),120)
show()
