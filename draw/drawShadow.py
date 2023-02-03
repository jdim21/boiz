from PIL import Image
from colors import colorsDict, backgroundLookup

def drawShadow(im):
    imNew = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
    imNew.putpixel((9, 21), colorsDict["blobShadow"])
    imNew.putpixel((22, 21), colorsDict["blobShadow"])

    imNew.putpixel((8, 22), colorsDict["blobShadowLight"])
    imNew.putpixel((9, 22), colorsDict["blobShadowLight"])
    imNew.putpixel((10, 22), colorsDict["blobShadow"])
    imNew.putpixel((21, 22), colorsDict["blobShadow"])
    imNew.putpixel((22, 22), colorsDict["blobShadowLight"])
    imNew.putpixel((23, 22), colorsDict["blobShadowLight"])

    imNew.putpixel((9, 23), colorsDict["blobShadowLight"])
    imNew.putpixel((10, 23), colorsDict["blobShadowLight"])
    imNew.putpixel((11, 23), colorsDict["blobShadow"])
    imNew.putpixel((12, 23), colorsDict["blobShadow"])
    imNew.putpixel((13, 23), colorsDict["blobShadow"])
    imNew.putpixel((14, 23), colorsDict["blobShadow"])
    imNew.putpixel((15, 23), colorsDict["blobShadow"])
    imNew.putpixel((16, 23), colorsDict["blobShadow"])
    imNew.putpixel((17, 23), colorsDict["blobShadow"])
    imNew.putpixel((18, 23), colorsDict["blobShadow"])
    imNew.putpixel((19, 23), colorsDict["blobShadow"])
    imNew.putpixel((20, 23), colorsDict["blobShadow"])
    imNew.putpixel((21, 23), colorsDict["blobShadowLight"])
    imNew.putpixel((22, 23), colorsDict["blobShadowLight"])

    imNew.putpixel((11, 24), colorsDict["blobShadowLight"])
    imNew.putpixel((12, 24), colorsDict["blobShadowLight"])
    imNew.putpixel((13, 24), colorsDict["blobShadowLight"])
    imNew.putpixel((14, 24), colorsDict["blobShadowLight"])
    imNew.putpixel((15, 24), colorsDict["blobShadowLight"])
    imNew.putpixel((16, 24), colorsDict["blobShadowLight"])
    imNew.putpixel((17, 24), colorsDict["blobShadowLight"])
    imNew.putpixel((18, 24), colorsDict["blobShadowLight"])
    imNew.putpixel((19, 24), colorsDict["blobShadowLight"])
    imNew.putpixel((20, 24), colorsDict["blobShadowLight"])

    im.paste(imNew, (0,0), mask=imNew)