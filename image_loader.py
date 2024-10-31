from PIL import Image

def load_image(filename):
    img = Image.open(filename)
    return img
