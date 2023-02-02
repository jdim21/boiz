from PIL import Image
from colors import colorsDict, backgroundLookup
from traitEncodings import TRAIT_ENCODINGS

def drawTophat(im, primaryColor, primaryColorShade, strapColor, strapColorShade, buckleColor, backgroundColor):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    imNew.putpixel((7, 2), colorsDict["black"])
    imNew.putpixel((8, 2), colorsDict["black"])
    imNew.putpixel((9, 2), colorsDict["black"])
    imNew.putpixel((10, 2), colorsDict["black"])
    imNew.putpixel((11, 2), colorsDict["black"])
    imNew.putpixel((12, 2), colorsDict["black"])
    imNew.putpixel((13, 2), colorsDict["black"])
    imNew.putpixel((14, 2), colorsDict["black"])
    imNew.putpixel((15, 2), colorsDict["black"])
    imNew.putpixel((16, 2), colorsDict["black"])

    imNew.putpixel((6, 3), colorsDict["black"])
    imNew.putpixel((7, 3), colorsDict[primaryColorShade])
    imNew.putpixel((8, 3), colorsDict[primaryColor])
    imNew.putpixel((9, 3), colorsDict[primaryColor])
    imNew.putpixel((10, 3), colorsDict[primaryColor])
    imNew.putpixel((11, 3), colorsDict[primaryColor])
    imNew.putpixel((12, 3), colorsDict[primaryColor])
    imNew.putpixel((13, 3), colorsDict[primaryColor])
    imNew.putpixel((14, 3), colorsDict[primaryColor])
    imNew.putpixel((15, 3), colorsDict[primaryColor])
    imNew.putpixel((16, 3), colorsDict[primaryColor])
    imNew.putpixel((17, 3), colorsDict["black"])

    imNew.putpixel((5, 4), backgroundLookup[backgroundColor])
    imNew.putpixel((6, 4), colorsDict["black"])
    imNew.putpixel((7, 4), colorsDict[primaryColorShade])
    imNew.putpixel((8, 4), colorsDict[primaryColor])
    imNew.putpixel((9, 4), colorsDict[primaryColor])
    imNew.putpixel((10, 4), colorsDict[primaryColor])
    imNew.putpixel((11, 4), colorsDict[primaryColor])
    imNew.putpixel((12, 4), colorsDict[primaryColor])
    imNew.putpixel((13, 4), colorsDict[primaryColor])
    imNew.putpixel((14, 4), colorsDict[primaryColor])
    imNew.putpixel((15, 4), colorsDict[primaryColor])
    imNew.putpixel((16, 4), colorsDict[primaryColor])
    imNew.putpixel((17, 4), colorsDict["black"])
    imNew.putpixel((18, 4), backgroundLookup[backgroundColor])

    imNew.putpixel((4, 5), backgroundLookup[backgroundColor])
    imNew.putpixel((5, 5), backgroundLookup[backgroundColor])
    imNew.putpixel((6, 5), colorsDict["black"])
    imNew.putpixel((7, 5), colorsDict[primaryColorShade])
    imNew.putpixel((8, 5), colorsDict[primaryColor])
    imNew.putpixel((9, 5), colorsDict[primaryColor])
    imNew.putpixel((10, 5), colorsDict[primaryColor])
    imNew.putpixel((11, 5), colorsDict[primaryColor])
    imNew.putpixel((12, 5), colorsDict[primaryColor])
    imNew.putpixel((13, 5), colorsDict[primaryColor])
    imNew.putpixel((14, 5), colorsDict[primaryColor])
    imNew.putpixel((15, 5), colorsDict[primaryColor])
    imNew.putpixel((16, 5), colorsDict[primaryColor])
    imNew.putpixel((17, 5), colorsDict["black"])
    imNew.putpixel((18, 5), backgroundLookup[backgroundColor])
    imNew.putpixel((19, 5), backgroundLookup[backgroundColor])

    imNew.putpixel((4, 6), backgroundLookup[backgroundColor])
    imNew.putpixel((5, 6), backgroundLookup[backgroundColor])
    imNew.putpixel((6, 6), colorsDict["black"])
    imNew.putpixel((7, 6), colorsDict[primaryColorShade])
    imNew.putpixel((8, 6), colorsDict[primaryColor])
    imNew.putpixel((9, 6), colorsDict[primaryColor])
    imNew.putpixel((10, 6), colorsDict[primaryColor])
    imNew.putpixel((11, 6), colorsDict[primaryColor])
    imNew.putpixel((12, 6), colorsDict[primaryColor])
    imNew.putpixel((13, 6), colorsDict[primaryColor])
    imNew.putpixel((14, 6), colorsDict[primaryColor])
    imNew.putpixel((15, 6), colorsDict[primaryColor])
    imNew.putpixel((16, 6), colorsDict[primaryColor])
    imNew.putpixel((17, 6), colorsDict["black"])
    imNew.putpixel((18, 6), backgroundLookup[backgroundColor])
    imNew.putpixel((19, 6), backgroundLookup[backgroundColor])

    imNew.putpixel((4, 7), backgroundLookup[backgroundColor])
    imNew.putpixel((5, 7), backgroundLookup[backgroundColor])
    imNew.putpixel((6, 7), colorsDict["black"])
    imNew.putpixel((7, 7), colorsDict[strapColorShade])
    imNew.putpixel((8, 7), colorsDict[strapColor])
    imNew.putpixel((9, 7), colorsDict[strapColor])
    imNew.putpixel((10, 7), colorsDict[strapColor])
    imNew.putpixel((11, 7), colorsDict[buckleColor])
    imNew.putpixel((12, 7), colorsDict[strapColor])
    imNew.putpixel((13, 7), colorsDict[buckleColor])
    imNew.putpixel((14, 7), colorsDict[strapColor])
    imNew.putpixel((15, 7), colorsDict[strapColor])
    imNew.putpixel((16, 7), colorsDict[strapColor])
    imNew.putpixel((17, 7), colorsDict["black"])
    imNew.putpixel((18, 7), backgroundLookup[backgroundColor])
    imNew.putpixel((19, 7), backgroundLookup[backgroundColor])

    imNew.putpixel((4, 8), backgroundLookup[backgroundColor])
    imNew.putpixel((5, 8), backgroundLookup[backgroundColor])
    imNew.putpixel((6, 8), colorsDict["black"])
    imNew.putpixel((7, 8), colorsDict["black"])
    imNew.putpixel((8, 8), colorsDict["black"])
    imNew.putpixel((9, 8), colorsDict["black"])
    imNew.putpixel((10, 8), colorsDict["black"])
    imNew.putpixel((11, 8), colorsDict["black"])
    imNew.putpixel((12, 8), colorsDict["black"])
    imNew.putpixel((13, 8), colorsDict["black"])
    imNew.putpixel((14, 8), colorsDict["black"])
    imNew.putpixel((15, 8), colorsDict["black"])
    imNew.putpixel((16, 8), colorsDict["black"])
    imNew.putpixel((17, 8), colorsDict["black"])
    imNew.putpixel((18, 8), backgroundLookup[backgroundColor])
    imNew.putpixel((19, 8), backgroundLookup[backgroundColor])

    imNew.putpixel((4, 9), backgroundLookup[backgroundColor])
    imNew.putpixel((5, 9), colorsDict["black"])
    imNew.putpixel((6, 9), colorsDict[primaryColorShade])
    imNew.putpixel((7, 9), colorsDict[primaryColor])
    imNew.putpixel((8, 9), colorsDict[primaryColor])
    imNew.putpixel((9, 9), colorsDict[primaryColor])
    imNew.putpixel((10, 9), colorsDict[primaryColor])
    imNew.putpixel((11, 9), colorsDict[primaryColor])
    imNew.putpixel((12, 9), colorsDict[primaryColor])
    imNew.putpixel((13, 9), colorsDict[primaryColor])
    imNew.putpixel((14, 9), colorsDict[primaryColor])
    imNew.putpixel((15, 9), colorsDict[primaryColor])
    imNew.putpixel((16, 9), colorsDict[primaryColor])
    imNew.putpixel((17, 9), colorsDict[primaryColor])
    imNew.putpixel((18, 9), colorsDict["black"])
    imNew.putpixel((19, 9), backgroundLookup[backgroundColor])

    imNew.putpixel((5, 10), backgroundLookup[backgroundColor])
    imNew.putpixel((6, 10), colorsDict["black"])
    imNew.putpixel((7, 10), colorsDict["black"])
    imNew.putpixel((8, 10), colorsDict["black"])
    imNew.putpixel((9, 10), colorsDict["black"])
    imNew.putpixel((10, 10), colorsDict["black"])
    imNew.putpixel((11, 10), colorsDict["black"])
    imNew.putpixel((12, 10), colorsDict["black"])
    imNew.putpixel((13, 10), colorsDict["black"])
    imNew.putpixel((14, 10), colorsDict["black"])
    imNew.putpixel((15, 10), colorsDict["black"])
    imNew.putpixel((16, 10), colorsDict["black"])
    imNew.putpixel((17, 10), colorsDict["black"])
    imNew.putpixel((18, 10), backgroundLookup[backgroundColor])

    im.paste(imNew, (0,0), mask=imNew)
