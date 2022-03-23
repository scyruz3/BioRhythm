from io import BytesIO
from PIL import Image
from bson import binary

# you might need additional operations to transfer
# this image to html templates
def getImageFromBinary(img: binary) -> Image:
    return Image.open(BytesIO(img))
