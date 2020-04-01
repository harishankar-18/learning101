from PIL import Image
from scipy.ndimage import filters

img = array(Image.open('dog.jpg').convert('L'))

img_blur = filters.gaussian_filter(img, 20)

q_img = img/ img_blur

x = Image.fromarray(uint8(q_img))
x.save('Quotient_image.jpg')
