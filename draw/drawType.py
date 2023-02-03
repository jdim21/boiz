from PIL import Image
from colors import colorsDict, backgroundLookup
from traitEncodings import TRAIT_ENCODINGS
from draw.drawBaseType import drawBaseType

def drawSolanaBackground(im, backgroundColor):
    for i in range(32):
        for j in range(32):
            im.putpixel((i, j), backgroundLookup[backgroundColor])

def drawType(im, trait, backgroundColor):
    imNew = Image.new('RGBA', (32, 32), (0, 0, 0, 0))


    decodedType = TRAIT_ENCODINGS["type"][trait]
    if decodedType == "Green":
        primaryColor = colorsDict["blobGreen"]
        colorShade = colorsDict["blobGreenShade"]
        colorLight = colorsDict["blobGreenLight"]
        colorBrow = colorsDict["blobGreen"]
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    if decodedType == "Rose":
        primaryColor = colorsDict["blobRose"]
        colorShade = colorsDict["blobRoseShade"]
        colorLight = colorsDict["blobRoseLight"]
        colorBrow = colorsDict["blobRose"]
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    if decodedType == "Yellow":
        primaryColor = colorsDict["blobYellow"]
        colorShade = colorsDict["blobYellowShade"]
        colorLight = colorsDict["blobYellowLight"]
        colorBrow = colorsDict["blobYellow"]
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    if decodedType == "Blue":
        primaryColor = colorsDict["blobBlue"]
        colorShade = colorsDict["blobBlueShade"]
        colorLight = colorsDict["blobBlueLight"]
        colorBrow = colorsDict["blobBlue"]
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    if decodedType == "Purple":
        primaryColor = colorsDict["blobPurple"]
        colorShade = colorsDict["blobPurpleShade"]
        colorLight = colorsDict["blobPurpleLight"]
        colorBrow = colorsDict["blobPurple"]
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    if decodedType == "Orange":
        primaryColor = colorsDict["blobOrange"]
        colorShade = colorsDict["blobOrangeShade"]
        colorLight = colorsDict["blobOrangeLight"]
        colorBrow = colorsDict["blobOrange"]
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    if decodedType == "Orange":
        primaryColor = colorsDict["blobOrange"]
        colorShade = colorsDict["blobOrangeShade"]
        colorLight = colorsDict["blobOrangeLight"]
        colorBrow = colorsDict["blobOrange"]
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    if decodedType == "Normal":
        primaryColor = "typeNormal"
        colorShade = "typeNormalShade"
        colorLight = "typeNormalLight"
        colorBrow = "typeNormalBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    if decodedType == "Rainbow":
        primaryColor = colorsDict["typeDevil"]
        colorShade = colorsDict["typeDevilShade"]
        colorLight = colorsDict["typeDevilLight"]
        colorBrow = colorsDict["typeDevilShade"]
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
        imNew.putpixel((15, 11), colorsDict["blobYellowShade"])
        imNew.putpixel((16, 11), colorsDict["blobYellowShade"])
        imNew.putpixel((17, 11), colorsDict["blobYellowShade"])

        imNew.putpixel((15, 12), colorsDict["blobYellow"])
        imNew.putpixel((16, 12), colorsDict["blobYellow"])
        imNew.putpixel((17, 12), colorsDict["blobYellow"])
        imNew.putpixel((18, 12), colorsDict["blobYellowShade"])
        imNew.putpixel((19, 12), colorsDict["blobGreenShade"])

        imNew.putpixel((15, 13), colorsDict["blobYellow"])
        imNew.putpixel((16, 13), colorsDict["blobYellowLight"])
        imNew.putpixel((17, 13), colorsDict["blobYellowLight"])
        imNew.putpixel((18, 13), colorsDict["blobYellow"])
        imNew.putpixel((19, 13), colorsDict["blobGreen"])
        imNew.putpixel((20, 13), colorsDict["blobGreenShade"])

        imNew.putpixel((14, 14), colorsDict["blobYellow"])
        imNew.putpixel((15, 14), colorsDict["blobYellowLight"])
        imNew.putpixel((16, 14), colorsDict["blobYellowLight"])
        imNew.putpixel((17, 14), colorsDict["blobYellowLight"])
        imNew.putpixel((18, 14), colorsDict["blobGreenLight"])
        imNew.putpixel((19, 14), colorsDict["blobGreen"])
        imNew.putpixel((20, 14), colorsDict["blobGreen"])
        imNew.putpixel((21, 14), colorsDict["blobGreenShade"])

        imNew.putpixel((14, 15), colorsDict["blobYellow"])
        imNew.putpixel((15, 15), colorsDict["blobYellowLight"])
        imNew.putpixel((16, 15), colorsDict["blobYellowLight"])
        imNew.putpixel((17, 15), colorsDict["blobGreenLight"])
        imNew.putpixel((20, 15), colorsDict["blobGreen"])
        imNew.putpixel((21, 15), colorsDict["blobBlueShade"])

        imNew.putpixel((14, 16), colorsDict["blobYellow"])
        imNew.putpixel((15, 16), colorsDict["blobYellow"])
        imNew.putpixel((16, 16), colorsDict["blobYellowLight"])
        imNew.putpixel((17, 16), colorsDict["blobGreenLight"])
        imNew.putpixel((20, 16), colorsDict["blobBlueLight"])
        imNew.putpixel((21, 16), colorsDict["blobBlueLight"])
        imNew.putpixel((22, 16), colorsDict["blobBlueShade"])

        imNew.putpixel((14, 17), colorsDict["blobYellow"])
        imNew.putpixel((15, 17), colorsDict["blobYellow"])
        imNew.putpixel((16, 17), colorsDict["blobGreen"])
        imNew.putpixel((17, 17), colorsDict["blobGreen"])
        imNew.putpixel((20, 17), colorsDict["blobBlueLight"])
        imNew.putpixel((21, 17), colorsDict["blobBlueLight"])
        imNew.putpixel((22, 17), colorsDict["blobBlueShade"])

        imNew.putpixel((13, 18), colorsDict["blobYellow"])
        imNew.putpixel((14, 18), colorsDict["blobYellow"])
        imNew.putpixel((15, 18), colorsDict["blobGreen"])
        imNew.putpixel((16, 18), colorsDict["blobGreen"])
        imNew.putpixel((17, 18), colorsDict["blobGreen"])
        imNew.putpixel((18, 18), colorsDict["blobBlueLight"])
        imNew.putpixel((21, 18), colorsDict["blobPurple"])
        imNew.putpixel((22, 18), colorsDict["blobPurpleShade"])

        imNew.putpixel((10, 19), colorsDict["blobYellowShade"])
        imNew.putpixel((11, 19), colorsDict["blobYellow"])
        imNew.putpixel((12, 19), colorsDict["blobYellow"])
        imNew.putpixel((13, 19), colorsDict["blobYellow"])
        imNew.putpixel((14, 19), colorsDict["blobGreen"])
        imNew.putpixel((17, 19), colorsDict["blobBlueLight"])
        imNew.putpixel((18, 19), colorsDict["blobBlueLight"])
        imNew.putpixel((19, 19), colorsDict["blobBlueLight"])
        imNew.putpixel((20, 19), colorsDict["blobPurple"])
        imNew.putpixel((21, 19), colorsDict["blobPurpleShade"])
        imNew.putpixel((22, 19), colorsDict["blobPurpleShade"])

        imNew.putpixel((10, 20), colorsDict["blobYellowShade"])
        imNew.putpixel((11, 20), colorsDict["blobYellowShade"])
        imNew.putpixel((12, 20), colorsDict["blobYellow"])
        imNew.putpixel((13, 20), colorsDict["blobGreen"])
        imNew.putpixel((14, 20), colorsDict["blobGreen"])
        imNew.putpixel((15, 20), colorsDict["blobGreen"])
        imNew.putpixel((16, 20), colorsDict["blobGreen"])
        imNew.putpixel((17, 20), colorsDict["blobBlueLight"])
        imNew.putpixel((18, 20), colorsDict["blobBlueLight"])
        imNew.putpixel((19, 20), colorsDict["blobPurple"])
        imNew.putpixel((20, 20), colorsDict["blobPurpleShade"])
        imNew.putpixel((21, 20), colorsDict["blobPurpleShade"])

        imNew.putpixel((11, 21), colorsDict["blobYellowShade"])
        imNew.putpixel((12, 21), colorsDict["blobYellowShade"])
        imNew.putpixel((13, 21), colorsDict["blobGreenShade"])
        imNew.putpixel((14, 21), colorsDict["blobGreenShade"])
        imNew.putpixel((15, 21), colorsDict["blobGreenShade"])
        imNew.putpixel((16, 21), colorsDict["blobGreenShade"])
        imNew.putpixel((17, 21), colorsDict["blobBlueShade"])
        imNew.putpixel((18, 21), colorsDict["blobBlueShade"])
        imNew.putpixel((19, 21), colorsDict["blobBlueShade"])
        imNew.putpixel((20, 21), colorsDict["blobPurpleShade"])

    if decodedType == "Solana":
        primaryColor = "typeNormal"
        colorShade = "typeNormalShade"
        colorLight = "typeNormalLight"
        colorBrow = "typeNormalBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
        imNew.putpixel((6, 6), colorsDict["typeSolana6"])
        imNew.putpixel((17, 6), colorsDict["typeSolana6"])

        imNew.putpixel((6, 7), colorsDict["typeSolanaAccent"])
        imNew.putpixel((7, 7), colorsDict["typeSolana7"])
        imNew.putpixel((16, 7), colorsDict["typeSolana7"])
        imNew.putpixel((17, 7), colorsDict["typeSolanaAccent"])

        imNew.putpixel((6, 8), colorsDict["typeSolanaAccent"])
        imNew.putpixel((7, 8), colorsDict["typeSolana8"])
        imNew.putpixel((10, 8), colorsDict["typeSolana8"])
        imNew.putpixel((11, 8), colorsDict["typeSolana8"])
        imNew.putpixel((12, 8), colorsDict["typeSolana8"])
        imNew.putpixel((13, 8), colorsDict["typeSolana8"])
        imNew.putpixel((16, 8), colorsDict["typeSolana8"])
        imNew.putpixel((17, 8), colorsDict["typeSolanaAccent"])

        imNew.putpixel((6, 9), colorsDict["typeSolana9"])
        imNew.putpixel((8, 9), colorsDict["typeSolana9"])
        imNew.putpixel((9, 9), colorsDict["typeSolana9"])
        imNew.putpixel((10, 9), colorsDict["typeSolana9"])
        imNew.putpixel((11, 9), colorsDict["typeSolana9"])
        imNew.putpixel((12, 9), colorsDict["typeSolana9"])
        imNew.putpixel((13, 9), colorsDict["typeSolana9"])
        imNew.putpixel((14, 9), colorsDict["typeSolana9"])
        imNew.putpixel((15, 9), colorsDict["typeSolana9"])
        imNew.putpixel((17, 9), colorsDict["typeSolana9"])

        imNew.putpixel((7, 10), colorsDict["typeSolana10"])
        imNew.putpixel((8, 10), colorsDict["typeSolanaAccent"])
        imNew.putpixel((9, 10), colorsDict["typeSolana10"])
        imNew.putpixel((10, 10), colorsDict["typeSolana10"])
        imNew.putpixel((11, 10), colorsDict["typeSolana10"])
        imNew.putpixel((12, 10), colorsDict["typeSolana10"])
        imNew.putpixel((13, 10), colorsDict["typeSolana10"])
        imNew.putpixel((14, 10), colorsDict["typeSolana10"])
        imNew.putpixel((15, 10), colorsDict["typeSolanaAccent"])
        imNew.putpixel((16, 10), colorsDict["typeSolana10"])

        imNew.putpixel((6, 11), colorsDict["typeSolana11"])
        imNew.putpixel((7, 11), colorsDict["typeSolana11"])
        imNew.putpixel((8, 11), colorsDict["typeSolana11"])
        imNew.putpixel((9, 11), colorsDict["typeSolana11"])
        imNew.putpixel((10, 11), colorsDict["typeSolana11"])
        imNew.putpixel((11, 11), colorsDict["typeSolana11"])
        imNew.putpixel((12, 11), colorsDict["typeSolana11"])
        imNew.putpixel((13, 11), colorsDict["typeSolana11"])
        imNew.putpixel((14, 11), colorsDict["typeSolana11"])
        imNew.putpixel((15, 11), colorsDict["typeSolana11"])
        imNew.putpixel((16, 11), colorsDict["typeSolana11"])
        imNew.putpixel((17, 11), colorsDict["typeSolana11"])

        imNew.putpixel((6, 12), colorsDict["typeSolana12"])
        imNew.putpixel((7, 12), colorsDict["typeSolana12"])
        imNew.putpixel((10, 12), colorsDict["typeSolana12"])
        imNew.putpixel((11, 12), colorsDict["typeSolana12"])
        imNew.putpixel((12, 12), colorsDict["typeSolana12"])
        imNew.putpixel((13, 12), colorsDict["typeSolana12"])
        imNew.putpixel((16, 12), colorsDict["typeSolana12"])
        imNew.putpixel((17, 12), colorsDict["typeSolana12"])

        imNew.putpixel((7, 13), colorsDict["typeSolana13"])
        imNew.putpixel((10, 13), colorsDict["typeSolana13"])
        imNew.putpixel((11, 13), colorsDict["typeSolana13"])
        imNew.putpixel((12, 13), colorsDict["typeSolana13"])
        imNew.putpixel((13, 13), colorsDict["typeSolana13"])
        imNew.putpixel((16, 13), colorsDict["typeSolana13"])

        imNew.putpixel((7, 19), colorsDict["typeSolana19Shade"])
        imNew.putpixel((8, 19), colorsDict["typeSolana19"])

        imNew.putpixel((1, 20), colorsDict["typeSolanaAccent"])
        imNew.putpixel((6, 20), colorsDict["typeSolana20Shade"])
        imNew.putpixel((7, 20), colorsDict["typeSolana20"])
        imNew.putpixel((8, 20), colorsDict["typeSolana20"])
        imNew.putpixel((9, 20), colorsDict["typeSolana20"])
        imNew.putpixel((10, 20), colorsDict["typeSolana20"])
        imNew.putpixel((11, 20), colorsDict["typeSolana20"])
        imNew.putpixel((12, 20), colorsDict["typeSolana20"])
        imNew.putpixel((13, 20), colorsDict["typeSolana20"])
        imNew.putpixel((14, 20), colorsDict["typeSolana20"])

        imNew.putpixel((0, 21), colorsDict["typeSolana21"])
        imNew.putpixel((5, 21), colorsDict["typeSolana21Shade"])
        imNew.putpixel((6, 21), colorsDict["typeSolana21"])
        imNew.putpixel((7, 21), colorsDict["typeSolana21"])
        imNew.putpixel((8, 21), colorsDict["typeSolana21"])
        imNew.putpixel((9, 21), colorsDict["typeSolana21"])
        imNew.putpixel((10, 21), colorsDict["typeSolana21"])
        imNew.putpixel((11, 21), colorsDict["typeSolana21"])
        imNew.putpixel((12, 21), colorsDict["typeSolana21"])
        imNew.putpixel((13, 21), colorsDict["typeSolana21"])
        imNew.putpixel((14, 21), colorsDict["typeSolana21"])

        imNew.putpixel((0, 22), colorsDict["typeSolana22"])
        imNew.putpixel((4, 22), colorsDict["typeSolana22Shade"])
        imNew.putpixel((5, 22), colorsDict["typeSolana22"])
        imNew.putpixel((6, 22), colorsDict["typeSolana22"])
        imNew.putpixel((7, 22), colorsDict["typeSolana22"])
        imNew.putpixel((8, 22), colorsDict["typeSolana22"])
        imNew.putpixel((9, 22), colorsDict["typeSolana22"])
        imNew.putpixel((10, 22), colorsDict["typeSolana22"])
        imNew.putpixel((11, 22), colorsDict["typeSolana22"])
        imNew.putpixel((12, 22), colorsDict["typeSolana22"])
        imNew.putpixel((13, 22), colorsDict["typeSolana22"])
        imNew.putpixel((14, 22), colorsDict["typeSolana22"])

        imNew.putpixel((0, 23), colorsDict["typeSolana23"])
        imNew.putpixel((3, 23), colorsDict["typeSolana23Shade"])
        imNew.putpixel((4, 23), colorsDict["typeSolana23"])
        imNew.putpixel((5, 23), colorsDict["typeSolana23"])
        imNew.putpixel((6, 23), colorsDict["typeSolana23"])
        imNew.putpixel((7, 23), colorsDict["typeSolana23"])
        imNew.putpixel((8, 23), colorsDict["typeSolana23"])
        imNew.putpixel((9, 23), colorsDict["black"])
        imNew.putpixel((10, 23), colorsDict["typeSolana23"])
        imNew.putpixel((11, 23), colorsDict["typeSolana23"])
        imNew.putpixel((12, 23), colorsDict["black"])
        imNew.putpixel((13, 23), colorsDict["typeSolana23"])
        imNew.putpixel((14, 23), colorsDict["typeSolana23"])
    elif decodedType == "Snowy":
        primaryColor = "typeSnowy"
        colorShade = "typeSnowyShade"
        colorLight = "typeSnowyLight"
        colorBrow = "typeSnowyBrows"
        imNew.putpixel((1, 18), colorsDict["black"])
        imNew.putpixel((2, 18), colorsDict["black"])

        imNew.putpixel((0, 19), colorsDict["black"])
        imNew.putpixel((1, 19), colorsDict["typeSnowy"])
        imNew.putpixel((2, 19), colorsDict["typeSnowyShade"])
        imNew.putpixel((3, 19), colorsDict["black"])

        imNew.putpixel((0, 20), colorsDict["black"])
        imNew.putpixel((1, 20), colorsDict["typeSnowyShade"])
        imNew.putpixel((2, 20), colorsDict["typeSnowy"])
        imNew.putpixel((3, 20), colorsDict["black"])

        imNew.putpixel((1, 21), colorsDict["black"])
        imNew.putpixel((2, 21), colorsDict["black"])
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    elif decodedType == "Light":
        primaryColor = "typeLight"
        colorShade = "typeLightShade"
        colorLight = "typeLightLight"
        colorBrow = "typeLightBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    elif decodedType == "Dark":
        primaryColor = "typeDark"
        colorShade = "typeDarkShade"
        colorLight = "typeDarkLight"
        colorBrow = "typeDarkBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    elif decodedType == "Brown":
        primaryColor = "typeBrown"
        colorShade = "typeBrownShade"
        colorLight = "typeBrownLight"
        colorBrow = "typeBrownBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    elif decodedType == "DarkBrown":
        primaryColor = "typeDarkBrown"
        colorShade = "typeDarkBrownShade"
        colorLight = "typeDarkBrownLight"
        colorBrow = "typeDarkBrownBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    elif decodedType == "Black":
        primaryColor = colorsDict["typeBlack"]
        colorShade = colorsDict["typeBlackShade"]
        colorLight = colorsDict["typeBlackLight"]
        colorBrow = colorsDict["typeBlackBrows"]
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    elif decodedType == "Ghost":
        primaryColor = colorsDict["typeGhost"]
        colorShade = colorsDict["typeGhostShade"]
        colorLight = colorsDict["typeGhostLight"]
        colorBrow = colorsDict["typeGhostBrows"]
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow, True)
    elif decodedType == "Clear":
        primaryColor = colorsDict["blobClear"]
        colorShade = colorsDict["blobClearShade"]
        colorLight = colorsDict["blobClearLight"]
        colorBrow = colorsDict["blobClearShade"]
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow, False)
    elif decodedType == "Skeleton":
        primaryColor = colorsDict["typeSkeleton"]
        colorShade = colorsDict["typeSkeletonShade"]
        colorLight = colorsDict["typeSkeletonLight"]
        colorBrow = colorsDict["typeSkeletonBrows"]
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
        # imNew.putpixel((6, 5), backgroundLookup[backgroundColor])
        # imNew.putpixel((17, 5), backgroundLookup[backgroundColor])

        # imNew.putpixel((5, 6), backgroundLookup[backgroundColor])
        # imNew.putpixel((6, 6), backgroundLookup[backgroundColor])
        # imNew.putpixel((7, 6), backgroundLookup[backgroundColor])
        # imNew.putpixel((16, 6), backgroundLookup[backgroundColor])
        # imNew.putpixel((17, 6), backgroundLookup[backgroundColor])
        # imNew.putpixel((18, 6), backgroundLookup[backgroundColor])

        # imNew.putpixel((5, 7), backgroundLookup[backgroundColor])
        # imNew.putpixel((6, 7), backgroundLookup[backgroundColor])
        # imNew.putpixel((7, 7), backgroundLookup[backgroundColor])
        # imNew.putpixel((8, 7), backgroundLookup[backgroundColor])
        # imNew.putpixel((15, 7), backgroundLookup[backgroundColor])
        # imNew.putpixel((16, 7), backgroundLookup[backgroundColor])
        # imNew.putpixel((17, 7), backgroundLookup[backgroundColor])
        # imNew.putpixel((18, 7), backgroundLookup[backgroundColor])

        # imNew.putpixel((5, 8), backgroundLookup[backgroundColor])
        # imNew.putpixel((6, 8), backgroundLookup[backgroundColor])
        # imNew.putpixel((7, 8), backgroundLookup[backgroundColor])
        # imNew.putpixel((10, 8), colorsDict["typeSkeletonShade"])
        # imNew.putpixel((11, 8), colorsDict["typeSkeletonShade"])
        # imNew.putpixel((16, 8), backgroundLookup[backgroundColor])
        # imNew.putpixel((17, 8), backgroundLookup[backgroundColor])
        # imNew.putpixel((18, 8), backgroundLookup[backgroundColor])

        # imNew.putpixel((5, 9), backgroundLookup[backgroundColor])
        # imNew.putpixel((6, 9), backgroundLookup[backgroundColor])
        # imNew.putpixel((8, 9), colorsDict["typeSkeletonShade"])
        # imNew.putpixel((9, 9), colorsDict["typeSkeletonShade"])
        # imNew.putpixel((17, 9), backgroundLookup[backgroundColor])
        # imNew.putpixel((18, 9), backgroundLookup[backgroundColor])

        # imNew.putpixel((5, 10), backgroundLookup[backgroundColor])
        # imNew.putpixel((7, 10), colorsDict["typeSkeletonShade"])
        # imNew.putpixel((11, 10), colorsDict["typeSkeletonShade"])
        # imNew.putpixel((18, 10), backgroundLookup[backgroundColor])

        # imNew.putpixel((6, 11), colorsDict["typeSkeletonShade"])
        # imNew.putpixel((10, 11), colorsDict["typeSkeletonShade"])

        # imNew.putpixel((6, 12), colorsDict["typeSkeletonShade"])
        # imNew.putpixel((8, 12), colorsDict["black"])
        # imNew.putpixel((9, 12), colorsDict["black"])
        # imNew.putpixel((14, 12), colorsDict["black"])
        # imNew.putpixel((15, 12), colorsDict["black"])

        # imNew.putpixel((5, 13), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((6, 13), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((8, 13), colorsDict["black"])
        # imNew.putpixel((9, 13), colorsDict["typeSkeleton"])
        # imNew.putpixel((14, 13), colorsDict["black"])
        # imNew.putpixel((15, 13), colorsDict["typeSkeleton"])
        # imNew.putpixel((17, 13), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((18, 13), colorsDict["typeSkeletonLight"])

        # imNew.putpixel((5, 14), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((6, 14), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((7, 14), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((8, 14), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((9, 14), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((10, 14), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((13, 14), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((14, 14), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((15, 14), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((16, 14), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((17, 14), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((18, 14), colorsDict["typeSkeletonLight"])

        # imNew.putpixel((5, 15), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((6, 15), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((7, 15), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((8, 15), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((9, 15), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((10, 15), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((13, 15), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((14, 15), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((15, 15), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((16, 15), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((17, 15), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((18, 15), colorsDict["typeSkeletonLight"])

        # imNew.putpixel((6, 16), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((7, 16), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((8, 16), colorsDict["black"])
        # imNew.putpixel((9, 16), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((10, 16), colorsDict["black"])
        # imNew.putpixel((11, 16), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((12, 16), colorsDict["black"])
        # imNew.putpixel((13, 16), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((14, 16), colorsDict["black"])
        # imNew.putpixel((15, 16), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((16, 16), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((17, 16), colorsDict["typeSkeletonLight"])

        # imNew.putpixel((7, 17), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((8, 17), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((9, 17), colorsDict["black"])
        # imNew.putpixel((10, 17), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((11, 17), colorsDict["black"])
        # imNew.putpixel((12, 17), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((13, 17), colorsDict["black"])
        # imNew.putpixel((14, 17), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((15, 17), colorsDict["black"])
        # imNew.putpixel((16, 17), colorsDict["typeSkeletonLight"])

        # imNew.putpixel((9, 18), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((10, 18), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((11, 18), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((12, 18), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((13, 18), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((14, 18), colorsDict["typeSkeletonLight"])

        # imNew.putpixel((9, 20), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((11, 20), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((13, 20), colorsDict["typeSkeletonLight"])

        # imNew.putpixel((10, 21), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((11, 21), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((12, 21), colorsDict["typeSkeletonLight"])

        # imNew.putpixel((9, 22), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((11, 22), colorsDict["typeSkeletonLight"])
        # imNew.putpixel((13, 22), colorsDict["typeSkeletonLight"])
    elif decodedType == "Alien":
        primaryColor = colorsDict["typeAlien"]
        colorShade = colorsDict["typeAlienShade"]
        colorLight = colorsDict["typeAlienLight"]
        colorBrow = colorsDict["typeAlienBrows"]
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
        imNew.putpixel((12, 15), colorsDict["typeAlienEyes2"])
        imNew.putpixel((13, 15), colorsDict["black"])
        imNew.putpixel((18, 15), colorsDict["typeAlienEyes2"])
        imNew.putpixel((19, 15), colorsDict["black"])

        imNew.putpixel((12, 16), colorsDict["black"])
        imNew.putpixel((13, 16), colorsDict["typeAlienEyes1"])
        imNew.putpixel((18, 16), colorsDict["black"])
        imNew.putpixel((19, 16), colorsDict["typeAlienEyes1"])

        imNew.putpixel((12, 17), colorsDict["typeAlien"])
        imNew.putpixel((13, 17), colorsDict["typeAlien"])
        imNew.putpixel((18, 17), colorsDict["typeAlien"])
        imNew.putpixel((19, 17), colorsDict["typeAlien"])

        imNew.putpixel((11, 18), colorsDict["typeAlienBrows2"])
        imNew.putpixel((12, 18), colorsDict["typeAlienBrows2"])
        imNew.putpixel((19, 18), colorsDict["typeAlienBrows2"])
        imNew.putpixel((20, 18), colorsDict["typeAlienBrows2"])
    elif decodedType == "Zombie":
        primaryColor = colorsDict["typeZombie"]
        colorShade = colorsDict["typeZombieShade"]
        colorLight = colorsDict["typeZombieLight"]
        colorBrow = colorsDict["typeZombieBrows"]
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)

        # imNew.putpixel((10, 9), colorsDict["typeZombieMarks"])
        # imNew.putpixel((13, 9), colorsDict["typeZombieMarks"])
        imNew.putpixel((11, 18), colorsDict["typeZombieBrows"])
        imNew.putpixel((12, 18), colorsDict["typeZombieBrows"])
        imNew.putpixel((19, 18), colorsDict["typeZombieBrows"])
        imNew.putpixel((20, 18), colorsDict["typeZombieBrows"])

        imNew.putpixel((12, 15), colorsDict["typeZombieEyes"])
        imNew.putpixel((18, 15), colorsDict["typeZombieEyes"])

        imNew.putpixel((12, 20), colorsDict["typeZombieMarks"])

        imNew.putpixel((18, 19), colorsDict["typeZombieMarks"])

    elif decodedType == "Devil":
        primaryColor = colorsDict["typeDevil"]
        colorShade = colorsDict["typeDevilShade"]
        colorLight = colorsDict["typeDevilLight"]
        colorBrow = colorsDict["typeDevilShade"]
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
        imNew.putpixel((11, 18), colorsDict["typeDevilBlush"])
        imNew.putpixel((12, 18), colorsDict["typeDevilBlush"])
        imNew.putpixel((19, 18), colorsDict["typeDevilBlush"])
        imNew.putpixel((20, 18), colorsDict["typeDevilBlush"])

        # imNew.putpixel((5, 4), colorsDict["black"])
        # imNew.putpixel((6, 4), colorsDict["black"])
        # imNew.putpixel((17, 4), colorsDict["black"])
        # imNew.putpixel((18, 4), colorsDict["black"])

        # imNew.putpixel((4, 5), colorsDict["black"])
        # imNew.putpixel((5, 5), colorsDict["typeDevilHorns"])
        # imNew.putpixel((6, 5), colorsDict["black"])
        # imNew.putpixel((17, 5), colorsDict["black"])
        # imNew.putpixel((18, 5), colorsDict["typeDevilHorns"])
        # imNew.putpixel((19, 5), colorsDict["black"])

        # imNew.putpixel((4, 6), colorsDict["black"])
        # imNew.putpixel((5, 6), colorsDict["typeDevilHorns"])
        # imNew.putpixel((6, 6), colorsDict["black"])
        # imNew.putpixel((7, 6), colorsDict["black"])
        # imNew.putpixel((16, 6), colorsDict["black"])
        # imNew.putpixel((17, 6), colorsDict["black"])
        # imNew.putpixel((18, 6), colorsDict["typeDevilHorns"])
        # imNew.putpixel((19, 6), colorsDict["black"])

        # imNew.putpixel((4, 7), colorsDict["black"])
        # imNew.putpixel((5, 7), colorsDict["typeDevilHorns"])
        # imNew.putpixel((6, 7), colorsDict["typeDevilHorns"])
        # imNew.putpixel((7, 7), colorsDict["black"])
        # imNew.putpixel((8, 7), colorsDict["black"])
        # imNew.putpixel((10, 7), colorsDict["black"])
        # imNew.putpixel((11, 7), colorsDict["black"])
        # imNew.putpixel((12, 7), colorsDict["black"])
        # imNew.putpixel((13, 7), colorsDict["black"])
        # imNew.putpixel((15, 7), colorsDict["black"])
        # imNew.putpixel((16, 7), colorsDict["black"])
        # imNew.putpixel((17, 7), colorsDict["typeDevilHorns"])
        # imNew.putpixel((18, 7), colorsDict["typeDevilHorns"])
        # imNew.putpixel((19, 7), colorsDict["black"])

        # imNew.putpixel((5, 8), colorsDict["black"])
        # imNew.putpixel((6, 8), colorsDict["typeDevilHorns"])
        # imNew.putpixel((7, 8), colorsDict["typeDevilHorns"])
        # imNew.putpixel((8, 8), colorsDict["black"])
        # imNew.putpixel((15, 8), colorsDict["black"])
        # imNew.putpixel((16, 8), colorsDict["typeDevilHorns"])
        # imNew.putpixel((17, 8), colorsDict["typeDevilHorns"])
        # imNew.putpixel((18, 8), colorsDict["black"])

        # imNew.putpixel((5, 9), backgroundLookup[backgroundColor])
        # imNew.putpixel((6, 9), colorsDict["black"])
        # imNew.putpixel((17, 9), colorsDict["black"])
        # imNew.putpixel((18, 9), backgroundLookup[backgroundColor])

        imNew.putpixel((10, 9), colorsDict["black"])
        imNew.putpixel((21, 9), colorsDict["black"])

        imNew.putpixel((9, 10), colorsDict["black"])
        imNew.putpixel((10, 10), colorsDict["typeDevilHornTip"])
        imNew.putpixel((11, 10), colorsDict["black"])
        imNew.putpixel((20, 10), colorsDict["black"])
        imNew.putpixel((21, 10), colorsDict["typeDevilHornTip"])
        imNew.putpixel((22, 10), colorsDict["black"])

        imNew.putpixel((9, 11), colorsDict["black"])
        imNew.putpixel((10, 11), colorsDict["typeDevilHorns"])
        imNew.putpixel((11, 11), colorsDict["typeDevilHorns"])
        imNew.putpixel((20, 11), colorsDict["typeDevilHorns"])
        imNew.putpixel((21, 11), colorsDict["typeDevilHorns"])
        imNew.putpixel((22, 11), colorsDict["black"])

        imNew.putpixel((9, 12), colorsDict["black"])
        imNew.putpixel((10, 12), colorsDict["typeDevilHorns"])
        imNew.putpixel((21, 12), colorsDict["typeDevilHorns"])
        imNew.putpixel((22, 12), colorsDict["black"])

        # imNew.putpixel((14, 14), colorsDict["typeDevilMarks"])
        # imNew.putpixel((17, 14), colorsDict["typeDevilMarks"])

        imNew.putpixel((12, 15), colorsDict["typeDevilEyes"])
        imNew.putpixel((18, 15), colorsDict["typeDevilEyes"])

        # Overwrite tail

        # imNew.putpixel((0, 17), colorsDict["black"])
        # imNew.putpixel((1, 17), colorsDict["black"])
        # imNew.putpixel((2, 17), colorsDict["black"])
        # imNew.putpixel((3, 17), colorsDict["black"])

        # imNew.putpixel((0, 18), colorsDict["typeDevil"])
        # imNew.putpixel((1, 18), colorsDict["typeDevil"])
        # imNew.putpixel((2, 18), colorsDict["typeDevilShade"])
        # imNew.putpixel((3, 18), colorsDict["black"])

        # imNew.putpixel((0, 19), colorsDict["black"])
        # imNew.putpixel((1, 19), colorsDict["typeDevilShade"])
        # imNew.putpixel((2, 19), colorsDict["typeDevil"])
        # imNew.putpixel((3, 19), colorsDict["black"])

        # imNew.putpixel((1, 20), colorsDict["black"])
        # imNew.putpixel((2, 20), colorsDict["typeDevil"])
        # imNew.putpixel((3, 20), colorsDict["black"])

        # imNew.putpixel((2, 21), colorsDict["black"])
        # imNew.putpixel((3, 21), colorsDict["black"])
    elif decodedType == "AstroDoge":
        primaryColor = "typeNormal"
        colorShade = "typeNormalShade"
        colorLight = "typeNormalLight"
        colorBrow = "typeNormalBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
        imNew.putpixel((9, 2), colorsDict["black"])
        imNew.putpixel((10, 2), colorsDict["black"])
        imNew.putpixel((11, 2), colorsDict["black"])
        imNew.putpixel((12, 2), colorsDict["black"])
        imNew.putpixel((13, 2), colorsDict["black"])
        imNew.putpixel((14, 2), colorsDict["black"])

        imNew.putpixel((6, 3), colorsDict["black"])
        imNew.putpixel((7, 3), colorsDict["black"])
        imNew.putpixel((8, 3), colorsDict["black"])
        imNew.putpixel((9, 3), colorsDict["typeAstronautGlass"])
        imNew.putpixel((10, 3), colorsDict["typeAstronautGlass"])
        imNew.putpixel((11, 3), colorsDict["typeAstronautGlass"])
        imNew.putpixel((12, 3), colorsDict["typeAstronautGlass"])
        imNew.putpixel((13, 3), colorsDict["typeAstronautGlass"])
        imNew.putpixel((14, 3), colorsDict["typeAstronautGlass"])
        imNew.putpixel((15, 3), colorsDict["black"])
        imNew.putpixel((16, 3), colorsDict["black"])
        imNew.putpixel((17, 3), colorsDict["black"])

        imNew.putpixel((5, 4), colorsDict["black"])
        imNew.putpixel((6, 4), colorsDict["typeAstronautGlass"])
        imNew.putpixel((7, 4), colorsDict["typeAstronautGlass"])
        imNew.putpixel((8, 4), colorsDict["typeAstronautGlass"])
        imNew.putpixel((9, 4), colorsDict["typeAstronautGlass"])
        imNew.putpixel((10, 4), colorsDict["typeAstronautGlass"])
        imNew.putpixel((11, 4), colorsDict["typeAstronautGlass"])
        imNew.putpixel((12, 4), colorsDict["typeAstronautGlass"])
        imNew.putpixel((13, 4), colorsDict["typeAstronautGlass"])
        imNew.putpixel((14, 4), colorsDict["typeAstronautGlass"])
        imNew.putpixel((15, 4), colorsDict["typeAstronautGlass"])
        imNew.putpixel((16, 4), colorsDict["typeAstronautGlass"])
        imNew.putpixel((17, 4), colorsDict["typeAstronautGlass"])
        imNew.putpixel((18, 4), colorsDict["black"])

        imNew.putpixel((4, 5), colorsDict["black"])
        imNew.putpixel((5, 5), colorsDict["typeAstronautGlass"])
        imNew.putpixel((6, 5), colorsDict["typeAstronautGlassShine"])
        imNew.putpixel((7, 5), colorsDict["typeAstronautGlassShine"])
        imNew.putpixel((8, 5), colorsDict["typeAstronautGlass"])
        imNew.putpixel((9, 5), colorsDict["typeAstronautGlass"])
        imNew.putpixel((10, 5), colorsDict["typeAstronautGlass"])
        imNew.putpixel((11, 5), colorsDict["typeAstronautGlass"])
        imNew.putpixel((12, 5), colorsDict["typeAstronautGlass"])
        imNew.putpixel((13, 5), colorsDict["typeAstronautGlass"])
        imNew.putpixel((14, 5), colorsDict["typeAstronautGlass"])
        imNew.putpixel((15, 5), colorsDict["typeAstronautGlass"])
        imNew.putpixel((16, 5), colorsDict["typeAstronautGlass"])
        imNew.putpixel((17, 5), colorsDict["typeAstronautGlass"])
        imNew.putpixel((18, 5), colorsDict["typeAstronautGlass"])
        imNew.putpixel((19, 5), colorsDict["black"])

        imNew.putpixel((3, 6), colorsDict["black"])
        imNew.putpixel((4, 6), colorsDict["typeAstronautGlass"])
        imNew.putpixel((5, 6), colorsDict["typeAstronautGlassShine"])
        imNew.putpixel((6, 6), colorsDict["typeAstronautGlassShine"])
        imNew.putpixel((7, 6), colorsDict["typeAstronautGlass"])
        imNew.putpixel((8, 6), colorsDict["typeAstronautGlass"])
        imNew.putpixel((9, 6), colorsDict["typeAstronautGlass"])
        imNew.putpixel((10, 6), colorsDict["typeAstronautGlass"])
        imNew.putpixel((11, 6), colorsDict["typeAstronautGlass"])
        imNew.putpixel((12, 6), colorsDict["typeAstronautGlass"])
        imNew.putpixel((13, 6), colorsDict["typeAstronautGlass"])
        imNew.putpixel((14, 6), colorsDict["typeAstronautGlass"])
        imNew.putpixel((15, 6), colorsDict["typeAstronautGlass"])
        imNew.putpixel((16, 6), colorsDict["typeAstronautGlass"])
        imNew.putpixel((17, 6), colorsDict["typeAstronautGlass"])
        imNew.putpixel((18, 6), colorsDict["typeAstronautGlass"])
        imNew.putpixel((19, 6), colorsDict["typeAstronautGlass"])
        imNew.putpixel((20, 6), colorsDict["black"])

        imNew.putpixel((2, 7), colorsDict["black"])
        imNew.putpixel((3, 7), colorsDict["typeAstronautGlass"])
        imNew.putpixel((4, 7), colorsDict["typeAstronautGlassShine"])
        imNew.putpixel((5, 7), colorsDict["typeAstronautGlassShine"])
        imNew.putpixel((6, 7), colorsDict["typeAstronautGlass"])
        imNew.putpixel((7, 7), colorsDict["typeAstronautGlass"])
        imNew.putpixel((8, 7), colorsDict["typeAstronautGlass"])
        imNew.putpixel((9, 7), colorsDict["typeAstronautGlass"])
        imNew.putpixel((10, 7), colorsDict["typeAstronautGlass"])
        imNew.putpixel((11, 7), colorsDict["typeAstronautGlass"])
        imNew.putpixel((12, 7), colorsDict["typeAstronautGlass"])
        imNew.putpixel((13, 7), colorsDict["typeAstronautGlass"])
        imNew.putpixel((14, 7), colorsDict["typeAstronautGlass"])
        imNew.putpixel((15, 7), colorsDict["typeAstronautGlass"])
        imNew.putpixel((16, 7), colorsDict["typeAstronautGlass"])
        imNew.putpixel((17, 7), colorsDict["typeAstronautGlass"])
        imNew.putpixel((18, 7), colorsDict["typeAstronautGlass"])
        imNew.putpixel((19, 7), colorsDict["typeAstronautGlass"])
        imNew.putpixel((20, 7), colorsDict["typeAstronautGlass"])
        imNew.putpixel((21, 7), colorsDict["black"])

        imNew.putpixel((2, 8), colorsDict["black"])
        imNew.putpixel((3, 8), colorsDict["typeAstronautGlass"])
        imNew.putpixel((4, 8), colorsDict["typeAstronautGlassShine"])
        imNew.putpixel((5, 8), colorsDict["typeAstronautGlassShine"])
        imNew.putpixel((6, 8), colorsDict["typeAstronautGlass"])
        imNew.putpixel((7, 8), colorsDict["typeAstronautGlass"])
        imNew.putpixel((8, 8), colorsDict["typeAstronautGlass"])
        imNew.putpixel((9, 8), colorsDict["typeAstronautGlass"])
        imNew.putpixel((10, 8), colorsDict["typeAstronautGlass"])
        imNew.putpixel((11, 8), colorsDict["typeAstronautGlass"])
        imNew.putpixel((12, 8), colorsDict["typeAstronautGlass"])
        imNew.putpixel((13, 8), colorsDict["typeAstronautGlass"])
        imNew.putpixel((14, 8), colorsDict["typeAstronautGlass"])
        imNew.putpixel((15, 8), colorsDict["typeAstronautGlass"])
        imNew.putpixel((16, 8), colorsDict["typeAstronautGlass"])
        imNew.putpixel((17, 8), colorsDict["typeAstronautGlass"])
        imNew.putpixel((18, 8), colorsDict["typeAstronautGlass"])
        imNew.putpixel((19, 8), colorsDict["typeAstronautGlass"])
        imNew.putpixel((20, 8), colorsDict["typeAstronautGlass"])
        imNew.putpixel((21, 8), colorsDict["black"])

        imNew.putpixel((2, 9), colorsDict["black"])
        imNew.putpixel((3, 9), colorsDict["typeAstronautGlassShine"])
        imNew.putpixel((4, 9), colorsDict["typeAstronautGlassShine"])
        imNew.putpixel((5, 9), colorsDict["typeAstronautGlass"])
        imNew.putpixel((6, 9), colorsDict["typeAstronautGlass"])
        imNew.putpixel((7, 9), colorsDict["typeAstronautGlass"])
        imNew.putpixel((8, 9), colorsDict["typeAstronautGlass"])
        imNew.putpixel((9, 9), colorsDict["typeAstronautGlass"])
        imNew.putpixel((10, 9), colorsDict["typeAstronautGlass"])
        imNew.putpixel((11, 9), colorsDict["typeAstronautGlass"])
        imNew.putpixel((12, 9), colorsDict["typeAstronautGlass"])
        imNew.putpixel((13, 9), colorsDict["typeAstronautGlass"])
        imNew.putpixel((14, 9), colorsDict["typeAstronautGlass"])
        imNew.putpixel((15, 9), colorsDict["typeAstronautGlass"])
        imNew.putpixel((16, 9), colorsDict["typeAstronautGlass"])
        imNew.putpixel((17, 9), colorsDict["typeAstronautGlass"])
        imNew.putpixel((18, 9), colorsDict["typeAstronautGlass"])
        imNew.putpixel((19, 9), colorsDict["typeAstronautGlass"])
        imNew.putpixel((20, 9), colorsDict["typeAstronautGlass"])
        imNew.putpixel((21, 9), colorsDict["black"])

        imNew.putpixel((1, 10), colorsDict["black"])
        imNew.putpixel((2, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((3, 10), colorsDict["typeAstronautGlassShine"])
        imNew.putpixel((4, 10), colorsDict["typeAstronautGlassShine"])
        imNew.putpixel((5, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((6, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((7, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((8, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((9, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((10, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((11, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((12, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((13, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((14, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((15, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((16, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((17, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((18, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((19, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((20, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((21, 10), colorsDict["typeAstronautGlass"])
        imNew.putpixel((22, 10), colorsDict["black"])

        imNew.putpixel((1, 11), colorsDict["black"])
        imNew.putpixel((2, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((3, 11), colorsDict["typeAstronautGlassShine"])
        imNew.putpixel((4, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((5, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((6, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((7, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((8, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((9, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((10, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((11, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((12, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((13, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((14, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((15, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((16, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((17, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((18, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((19, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((20, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((21, 11), colorsDict["typeAstronautGlass"])
        imNew.putpixel((22, 11), colorsDict["black"])

        imNew.putpixel((1, 12), colorsDict["black"])
        imNew.putpixel((2, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((3, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((4, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((5, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((6, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((7, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((8, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((9, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((10, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((11, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((12, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((13, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((14, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((15, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((16, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((17, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((18, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((19, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((20, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((21, 12), colorsDict["typeAstronautGlass"])
        imNew.putpixel((22, 12), colorsDict["black"])

        imNew.putpixel((1, 13), colorsDict["black"])
        imNew.putpixel((2, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((3, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((4, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((5, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((6, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((7, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((8, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((9, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((10, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((11, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((12, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((13, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((14, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((15, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((16, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((17, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((18, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((19, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((20, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((21, 13), colorsDict["typeAstronautGlass"])
        imNew.putpixel((22, 13), colorsDict["black"])

        imNew.putpixel((2, 14), colorsDict["black"])
        imNew.putpixel((3, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((4, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((5, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((6, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((7, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((8, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((9, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((10, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((11, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((12, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((13, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((14, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((15, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((16, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((17, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((18, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((19, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((20, 14), colorsDict["typeAstronautGlass"])
        imNew.putpixel((21, 14), colorsDict["black"])

        imNew.putpixel((2, 15), colorsDict["black"])
        imNew.putpixel((3, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((4, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((5, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((6, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((7, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((8, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((9, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((10, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((11, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((12, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((13, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((14, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((15, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((16, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((17, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((18, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((19, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((20, 15), colorsDict["typeAstronautGlass"])
        imNew.putpixel((21, 15), colorsDict["black"])

        imNew.putpixel((2, 16), colorsDict["black"])
        imNew.putpixel((3, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((4, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((5, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((6, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((7, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((8, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((9, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((10, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((11, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((12, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((13, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((14, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((15, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((16, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((17, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((18, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((19, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((20, 16), colorsDict["typeAstronautGlass"])
        imNew.putpixel((21, 16), colorsDict["black"])

        imNew.putpixel((3, 17), colorsDict["black"])
        imNew.putpixel((4, 17), colorsDict["typeAstronautGlass"])
        imNew.putpixel((5, 17), colorsDict["typeAstronautGlass"])
        imNew.putpixel((6, 17), colorsDict["typeAstronautGlass"])
        imNew.putpixel((7, 17), colorsDict["typeAstronautGlass"])
        imNew.putpixel((8, 17), colorsDict["typeAstronautGlass"])
        imNew.putpixel((9, 17), colorsDict["typeAstronautGlass"])
        imNew.putpixel((10, 17), colorsDict["typeAstronautGlass"])
        imNew.putpixel((11, 17), colorsDict["typeAstronautGlass"])
        imNew.putpixel((12, 17), colorsDict["typeAstronautGlass"])
        imNew.putpixel((13, 17), colorsDict["typeAstronautGlass"])
        imNew.putpixel((14, 17), colorsDict["typeAstronautGlass"])
        imNew.putpixel((15, 17), colorsDict["typeAstronautGlass"])
        imNew.putpixel((16, 17), colorsDict["typeAstronautGlass"])
        imNew.putpixel((17, 17), colorsDict["typeAstronautGlass"])
        imNew.putpixel((18, 17), colorsDict["typeAstronautGlass"])
        imNew.putpixel((19, 17), colorsDict["typeAstronautGlass"])
        imNew.putpixel((20, 17), colorsDict["black"])

        imNew.putpixel((4, 18), colorsDict["black"])
        imNew.putpixel((5, 18), colorsDict["typeAstronautGlass"])
        imNew.putpixel((6, 18), colorsDict["typeAstronautGlass"])
        imNew.putpixel((7, 18), colorsDict["typeAstronautGlass"])
        imNew.putpixel((8, 18), colorsDict["typeAstronautGlass"])
        imNew.putpixel((9, 18), colorsDict["typeAstronautGlass"])
        imNew.putpixel((10, 18), colorsDict["typeAstronautGlass"])
        imNew.putpixel((11, 18), colorsDict["typeAstronautGlass"])
        imNew.putpixel((12, 18), colorsDict["typeAstronautGlass"])
        imNew.putpixel((13, 18), colorsDict["typeAstronautGlass"])
        imNew.putpixel((14, 18), colorsDict["typeAstronautGlass"])
        imNew.putpixel((15, 18), colorsDict["typeAstronautGlass"])
        imNew.putpixel((16, 18), colorsDict["typeAstronautGlass"])
        imNew.putpixel((17, 18), colorsDict["typeAstronautGlass"])
        imNew.putpixel((18, 18), colorsDict["typeAstronautGlass"])
        imNew.putpixel((19, 18), colorsDict["black"])

        imNew.putpixel((5, 19), colorsDict["black"])
        imNew.putpixel((6, 19), colorsDict["typeAstronautGlass"])
        imNew.putpixel((7, 19), (120, 168, 186))
        imNew.putpixel((8, 19), colorsDict["typeAstronautGlassOverWhite"])
        imNew.putpixel((9, 19), colorsDict["typeAstronautGlass"])
        imNew.putpixel((10, 19), colorsDict["typeAstronautGlass"])
        imNew.putpixel((11, 19), colorsDict["typeAstronautGlass"])
        imNew.putpixel((12, 19), colorsDict["typeAstronautGlass"])
        imNew.putpixel((13, 19), colorsDict["typeAstronautGlass"])
        imNew.putpixel((14, 19), colorsDict["typeAstronautGlass"])
        imNew.putpixel((15, 19), colorsDict["typeAstronautGlass"])
        imNew.putpixel((16, 19), colorsDict["typeAstronautGlass"])
        imNew.putpixel((17, 19), colorsDict["typeAstronautGlass"])
        imNew.putpixel((18, 19), colorsDict["black"])

        imNew.putpixel((1, 20), colorsDict["typeAstronautRed"])
        imNew.putpixel((6, 20), colorsDict["black"])
        imNew.putpixel((7, 20), colorsDict["black"])
        imNew.putpixel((8, 20), colorsDict["black"])
        imNew.putpixel((9, 20), colorsDict["typeAstronautGlassOverWhite"])
        imNew.putpixel((10, 20), colorsDict["typeAstronautGlassOverWhite"])
        imNew.putpixel((11, 20), colorsDict["typeAstronautGlassOverWhite"])
        imNew.putpixel((12, 20), colorsDict["typeAstronautGlassOverWhite"])
        imNew.putpixel((13, 20), colorsDict["typeAstronautGlassOverWhite"])
        imNew.putpixel((14, 20), colorsDict["typeAstronautGlassOverWhite"])
        imNew.putpixel((15, 20), colorsDict["black"])
        imNew.putpixel((16, 20), colorsDict["black"])
        imNew.putpixel((17, 20), colorsDict["black"])

        imNew.putpixel((0, 21), colorsDict["white"])
        imNew.putpixel((5, 21), colorsDict["typeAstronautSuitShade"])
        imNew.putpixel((6, 21), colorsDict["white"])
        imNew.putpixel((7, 21), colorsDict["white"])
        imNew.putpixel((8, 21), colorsDict["white"])
        imNew.putpixel((9, 21), colorsDict["black"])
        imNew.putpixel((10, 21), colorsDict["black"])
        imNew.putpixel((11, 21), colorsDict["black"])
        imNew.putpixel((12, 21), colorsDict["black"])
        imNew.putpixel((13, 21), colorsDict["black"])
        imNew.putpixel((14, 21), colorsDict["black"])
        imNew.putpixel((15, 21), colorsDict["black"])

        imNew.putpixel((0, 22), colorsDict["white"])
        imNew.putpixel((4, 22), colorsDict["typeAstronautSuitShade"])
        imNew.putpixel((5, 22), colorsDict["typeAstronautRed"])
        imNew.putpixel((6, 22), colorsDict["white"])
        imNew.putpixel((7, 22), colorsDict["black"])
        imNew.putpixel((8, 22), colorsDict["white"])
        imNew.putpixel((9, 22), colorsDict["black"])
        imNew.putpixel((10, 22), colorsDict["typeAstronautRed"])
        imNew.putpixel((11, 22), colorsDict["white"])
        imNew.putpixel((12, 22), colorsDict["white"])
        imNew.putpixel((13, 22), colorsDict["white"])
        imNew.putpixel((14, 22), colorsDict["typeAstronautRed"])
        imNew.putpixel((15, 22), colorsDict["black"])

        imNew.putpixel((0, 23), colorsDict["white"])
        imNew.putpixel((3, 23), colorsDict["typeAstronautSuitShade"])
        imNew.putpixel((4, 23), colorsDict["white"])
        imNew.putpixel((5, 23), colorsDict["typeAstronautRed"])
        imNew.putpixel((6, 23), colorsDict["white"])
        imNew.putpixel((7, 23), colorsDict["white"])
        imNew.putpixel((8, 23), colorsDict["white"])
        imNew.putpixel((9, 23), colorsDict["black"])
        imNew.putpixel((10, 23), colorsDict["typeAstronautSuitShade"])
        imNew.putpixel((11, 23), colorsDict["typeAstronautSuitShade"])
        imNew.putpixel((12, 23), colorsDict["black"])
        imNew.putpixel((13, 23), colorsDict["typeAstronautSuitShade"])
        imNew.putpixel((14, 23), colorsDict["typeAstronautSuitShade"])
        imNew.putpixel((15, 23), colorsDict["black"])

    elif decodedType == "DiamondDoge":
        primaryColor = "typeDiamondDoge"
        colorShade = "typeDiamondDogeShade"
        colorLight = "typeDiamondDogeShade"
        colorBrow = "typeDiamondDogeBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)

        imNew.putpixel((8, 9), colorsDict["white"])
        imNew.putpixel((7, 10), colorsDict["white"])
        imNew.putpixel((6, 11), colorsDict["white"])

        # imNew.putpixel((19, 4), colorsDict["white"])

        # imNew.putpixel((19, 5), colorsDict["white"])

        # imNew.putpixel((18, 6), colorsDict["white"])
        # imNew.putpixel((20, 6), colorsDict["white"])

        # imNew.putpixel((19, 7), colorsDict["white"])

        # imNew.putpixel((4, 8), colorsDict["white"])
        # imNew.putpixel((6, 8), colorsDict["white"])
        # imNew.putpixel((19, 8), colorsDict["white"])

        # imNew.putpixel((5, 9), colorsDict["white"])

        # imNew.putpixel((4, 10), colorsDict["white"])
        # imNew.putpixel((6, 10), colorsDict["white"])

        imNew.putpixel((1, 20), colorsDict["white"])
        # imNew.putpixel((15, 20), colorsDict["white"])
        # imNew.putpixel((17, 20), colorsDict["white"])

        # imNew.putpixel((16, 21), colorsDict["white"])

        # imNew.putpixel((15, 22), colorsDict["white"])
        # imNew.putpixel((17, 22), colorsDict["white"])

    im.paste(imNew, (0,0), mask=imNew)
