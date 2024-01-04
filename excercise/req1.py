import sys
from PIL import Image

images=[]

for arv in sys.argv[1:]:
    image=Image.open(arv)
    images.append(image)

Image.SAVE("gifs.gif",save_all=True,append_image=[images[1]],duration=200,loop=0)