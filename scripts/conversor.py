# Converte imagen para preto e branco
from PIL import Image

img = Image.open("img.jpg")

blackWhite = img.convert("L")
blackWhite.save('covertido.jpg')
blackWhite.show()