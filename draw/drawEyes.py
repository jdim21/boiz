from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS

def drawEyes(im, trait, type):
    imNew = Image.new('RGBA', (32, 32), (0, 0, 0, 0))

    typePrimaryColor = "blobGreen"
    typeLightColor = "blobGreenLight"
    if type == "r":
        typePrimaryColor = "blobRose"
        typeLightColor = "blobRoseLight"
    elif type == "y":
        typePrimaryColor = "blobYellow"
        typeLightColor = "blobYellowLight"
    elif type == "b":
        typePrimaryColor = "blobBlue"
        typeLightColor = "blobBlueLight"
    elif type == "p":
        typePrimaryColor = "blobPurple"
        typeLightColor = "blobPurpleLight"
    elif type == "o":
        typePrimaryColor = "blobOrange"
        typeLightColor = "blobOrangeLight"
    elif type == "a":
        typePrimaryColor = "typeAlien"
        typeLightColor = "typeAlienLight"
    elif type == "z":
        typePrimaryColor = "typeZombie"
        typeLightColor = "typeZombieLight"
    elif type == "k":
        typePrimaryColor = "typeBlack"
        typeLightColor = "typeBlackLight"
    elif type == "v":
        typePrimaryColor = "typeDevil"
        typeLightColor = "typeDevilLight"
    elif type == "w":
        typePrimaryColor = "blobGreen"
        typeLightColor = "blobGreenLight"
    # typePrimaryColor = "typeNormal"
    # if type == "l":
    #     typePrimaryColor = "typeLight"
    # elif type == "d":
    #     typePrimaryColor = "typeDark"
    # elif type == "b":
    #     typePrimaryColor = "typeBrown"
    # elif type == "r":
    #     typePrimaryColor = "typeDarkBrown"
    # elif type == "k":
    #     typePrimaryColor = "typeBlack"
    # elif type == "z":
    #     typePrimaryColor = "typeZombie"
    # elif type == "s":
    #     typePrimaryColor = "typeSkeleton"
    # elif type == "v":
    #     typePrimaryColor = "typeDevil"
    # elif type == "a":
    #     typePrimaryColor = "typeAlien"
    # elif type == "w":
    #     typePrimaryColor = "typeSnowy"
    # elif type == "o":
    #     typePrimaryColor = "typeSolana12"

    decodedType = TRAIT_ENCODINGS["eyes"][trait]
    if decodedType == "Vipers":

        imNew.putpixel((12, 14), colorsDict["black"])
        imNew.putpixel((13, 14), colorsDict["black"])
        imNew.putpixel((14, 14), colorsDict["black"])
        imNew.putpixel((15, 14), colorsDict["black"])
        imNew.putpixel((16, 14), colorsDict["black"])
        imNew.putpixel((17, 14), colorsDict["black"])
        imNew.putpixel((18, 14), colorsDict["black"])
        imNew.putpixel((19, 14), colorsDict["black"])
        imNew.putpixel((20, 14), colorsDict["black"])
        imNew.putpixel((21, 14), colorsDict["black"])

        imNew.putpixel((11, 15), colorsDict["black"])
        imNew.putpixel((12, 15), colorsDict["pvGreen"])
        imNew.putpixel((13, 15), colorsDict["pvYellow"])
        imNew.putpixel((14, 15), colorsDict["pvOrange"])
        imNew.putpixel((15, 15), colorsDict["pvRed"])
        imNew.putpixel((16, 15), colorsDict["pvRed"])
        imNew.putpixel((17, 15), colorsDict["pvRed"])
        imNew.putpixel((18, 15), colorsDict["pvOrange"])
        imNew.putpixel((19, 15), colorsDict["pvYellow"])
        imNew.putpixel((20, 15), colorsDict["pvGreen"])
        imNew.putpixel((21, 15), colorsDict["pvBlue"])

        imNew.putpixel((9, 16), colorsDict["black"])
        imNew.putpixel((10, 16), colorsDict["black"])
        imNew.putpixel((11, 16), colorsDict["pvBlue"])
        imNew.putpixel((12, 16), colorsDict["pvGreen"])
        imNew.putpixel((13, 16), colorsDict["pvYellow"])
        imNew.putpixel((14, 16), colorsDict["pvOrange"])
        imNew.putpixel((15, 16), colorsDict["pvRed"])
        imNew.putpixel((17, 16), colorsDict["pvRed"])
        imNew.putpixel((18, 16), colorsDict["pvOrange"])
        imNew.putpixel((19, 16), colorsDict["pvYellow"])
        imNew.putpixel((20, 16), colorsDict["pvGreen"])
        imNew.putpixel((21, 16), colorsDict["pvBlue"])

        imNew.putpixel((12, 17), colorsDict["pvGreen"])
        imNew.putpixel((13, 17), colorsDict["pvYellow"])
        imNew.putpixel((14, 17), colorsDict["pvOrange"])
        imNew.putpixel((15, 17), colorsDict["pvRed"])
        imNew.putpixel((17, 17), colorsDict["pvRed"])
        imNew.putpixel((18, 17), colorsDict["pvOrange"])
        imNew.putpixel((19, 17), colorsDict["pvYellow"])
        imNew.putpixel((20, 17), colorsDict["pvGreen"])

    elif decodedType == "Happy":
        imNew.putpixel((12, 15), colorsDict["black"])
        imNew.putpixel((13, 15), colorsDict[typePrimaryColor])
        imNew.putpixel((18, 15), colorsDict[typeLightColor])
        imNew.putpixel((19, 15), colorsDict["black"])

        imNew.putpixel((11, 16), colorsDict["black"])
        imNew.putpixel((12, 16), colorsDict[typePrimaryColor])
        imNew.putpixel((13, 16), colorsDict["black"])
        imNew.putpixel((18, 16), colorsDict["black"])
        imNew.putpixel((19, 16), colorsDict[typePrimaryColor])
        imNew.putpixel((20, 16), colorsDict["black"])

        imNew.putpixel((11, 17), colorsDict[typePrimaryColor])
        imNew.putpixel((12, 17), colorsDict[typePrimaryColor])
        imNew.putpixel((13, 17), colorsDict[typePrimaryColor])
        imNew.putpixel((18, 17), colorsDict[typePrimaryColor])
        imNew.putpixel((19, 17), colorsDict[typePrimaryColor])
        imNew.putpixel((20, 17), colorsDict[typePrimaryColor])
        if type == "w":
            imNew.putpixel((13, 15), colorsDict["blobYellow"])
            imNew.putpixel((12, 16), colorsDict["blobYellow"])
            imNew.putpixel((11, 17), colorsDict["blobYellow"])
            imNew.putpixel((12, 17), colorsDict["blobYellow"])
            imNew.putpixel((13, 17), colorsDict["blobYellow"])
            imNew.putpixel((20, 17), colorsDict["blobBlueLight"])

    elif decodedType == "BigShades":
        imNew.putpixel((12, 14), colorsDict["black"])
        imNew.putpixel((13, 14), colorsDict["black"])
        imNew.putpixel((14, 14), colorsDict["black"])
        imNew.putpixel((15, 14), colorsDict["black"])
        imNew.putpixel((16, 14), colorsDict["black"])
        imNew.putpixel((17, 14), colorsDict["black"])
        imNew.putpixel((18, 14), colorsDict["black"])
        imNew.putpixel((19, 14), colorsDict["black"])
        imNew.putpixel((20, 14), colorsDict["black"])

        imNew.putpixel((11, 15), colorsDict["black"])
        imNew.putpixel((12, 15), colorsDict["bigShades1"])
        imNew.putpixel((13, 15), colorsDict["bigShades1"])
        imNew.putpixel((14, 15), colorsDict["bigShades1"])
        imNew.putpixel((17, 15), colorsDict["bigShades1"])
        imNew.putpixel((18, 15), colorsDict["bigShades1"])
        imNew.putpixel((19, 15), colorsDict["bigShades1"])

        imNew.putpixel((10, 16), colorsDict["black"])
        imNew.putpixel((12, 16), colorsDict["bigShades2"])
        imNew.putpixel((13, 16), colorsDict["bigShades2"])
        imNew.putpixel((14, 16), colorsDict["bigShades2"])
        imNew.putpixel((17, 16), colorsDict["bigShades2"])
        imNew.putpixel((18, 16), colorsDict["bigShades2"])
        imNew.putpixel((19, 16), colorsDict["bigShades2"])

        imNew.putpixel((12, 17), colorsDict["bigShades3"])
        imNew.putpixel((13, 17), colorsDict["bigShades3"])
        imNew.putpixel((14, 17), colorsDict["bigShades3"])
        imNew.putpixel((17, 17), colorsDict["bigShades3"])
        imNew.putpixel((18, 17), colorsDict["bigShades3"])
        imNew.putpixel((19, 17), colorsDict["bigShades3"])
    elif decodedType == "Wink":
        imNew.putpixel((12, 15), colorsDict[typePrimaryColor])
        imNew.putpixel((13, 15), colorsDict[typePrimaryColor])
        imNew.putpixel((12, 17), colorsDict[typePrimaryColor])
        imNew.putpixel((13, 17), colorsDict[typePrimaryColor])
        imNew.putpixel((12, 16), colorsDict["black"])
        imNew.putpixel((13, 16), colorsDict["black"])
        if type == "w":
            imNew.putpixel((12, 15), colorsDict["typeDevil"])
            imNew.putpixel((13, 15), colorsDict["typeDevil"])
            imNew.putpixel((12, 17), colorsDict["typeDevil"])
            imNew.putpixel((13, 17), colorsDict["blobYellow"])

    elif decodedType == "Laughing":
        imNew.putpixel((9, 11), colorsDict["black"])
        imNew.putpixel((14, 11), colorsDict["black"])

        imNew.putpixel((8, 12), colorsDict[typePrimaryColor])
        imNew.putpixel((9, 12), colorsDict[typePrimaryColor])
        imNew.putpixel((10, 12), colorsDict["black"])
        imNew.putpixel((13, 12), colorsDict["black"])
        imNew.putpixel((14, 12), colorsDict[typePrimaryColor])
        imNew.putpixel((15, 12), colorsDict[typePrimaryColor])

        imNew.putpixel((9, 13), colorsDict["black"])
        imNew.putpixel((14, 13), colorsDict["black"])

        imNew.putpixel((8, 13), colorsDict[typePrimaryColor])
        imNew.putpixel((15, 13), colorsDict[typePrimaryColor])
    elif decodedType == "HippieGlasses":

        imNew.putpixel((12, 15), colorsDict["hippieGlassesOutline"])
        imNew.putpixel((13, 15), colorsDict["hippieGlassesOutline"])
        imNew.putpixel((18, 15), colorsDict["hippieGlassesOutline"])
        imNew.putpixel((19, 15), colorsDict["hippieGlassesOutline"])

        imNew.putpixel((10, 16), colorsDict["hippieGlassesOutline"])
        imNew.putpixel((11, 16), colorsDict["hippieGlassesOutline"])
        imNew.putpixel((12, 16), colorsDict["hippieGlasses"])
        imNew.putpixel((13, 16), colorsDict["hippieGlasses"])
        imNew.putpixel((14, 16), colorsDict["hippieGlassesOutline"])
        imNew.putpixel((15, 16), colorsDict["hippieGlassesOutline"])
        imNew.putpixel((16, 16), colorsDict["hippieGlassesOutline"])
        imNew.putpixel((17, 16), colorsDict["hippieGlassesOutline"])
        imNew.putpixel((18, 16), colorsDict["hippieGlasses"])
        imNew.putpixel((19, 16), colorsDict["hippieGlasses"])
        imNew.putpixel((20, 16), colorsDict["hippieGlassesOutline"])
        imNew.putpixel((21, 16), colorsDict["hippieGlassesOutline"])

        imNew.putpixel((9, 17), colorsDict["hippieGlassesOutline"])
        imNew.putpixel((11, 17), colorsDict["hippieGlassesOutline"])
        imNew.putpixel((12, 17), colorsDict["hippieGlasses"])
        imNew.putpixel((13, 17), colorsDict["hippieGlasses"])
        imNew.putpixel((14, 17), colorsDict["hippieGlassesOutline"])
        imNew.putpixel((17, 17), colorsDict["hippieGlassesOutline"])
        imNew.putpixel((18, 17), colorsDict["hippieGlasses"])
        imNew.putpixel((19, 17), colorsDict["hippieGlasses"])
        imNew.putpixel((20, 17), colorsDict["hippieGlassesOutline"])

        imNew.putpixel((12, 18), colorsDict["hippieGlassesOutline"])
        imNew.putpixel((13, 18), colorsDict["hippieGlassesOutline"])
        imNew.putpixel((18, 18), colorsDict["hippieGlassesOutline"])
        imNew.putpixel((19, 18), colorsDict["hippieGlassesOutline"])
    elif decodedType == "MagicGlasses":

        imNew.putpixel((12, 15), colorsDict["matrixGlasses"])
        imNew.putpixel((13, 15), colorsDict["matrixGlassesShine"])
        imNew.putpixel((14, 15), colorsDict["matrixGlasses"])
        imNew.putpixel((17, 15), colorsDict["matrixGlasses"])
        imNew.putpixel((18, 15), colorsDict["matrixGlassesShine"])
        imNew.putpixel((19, 15), colorsDict["matrixGlasses"])

        imNew.putpixel((12, 16), colorsDict["matrixGlassesShine"])
        imNew.putpixel((13, 16), colorsDict["matrixGlasses"])
        imNew.putpixel((14, 16), colorsDict["matrixGlasses"])
        imNew.putpixel((15, 16), colorsDict["black"])
        imNew.putpixel((16, 16), colorsDict["black"])
        imNew.putpixel((17, 16), colorsDict["matrixGlassesShine"])
        imNew.putpixel((18, 16), colorsDict["matrixGlasses"])
        imNew.putpixel((19, 16), colorsDict["matrixGlasses"])

        imNew.putpixel((12, 17), colorsDict["matrixGlasses"])
        imNew.putpixel((13, 17), colorsDict["matrixGlasses"])
        imNew.putpixel((14, 17), colorsDict["matrixGlasses"])
        imNew.putpixel((17, 17), colorsDict["matrixGlasses"])
        imNew.putpixel((18, 17), colorsDict["matrixGlasses"])
        imNew.putpixel((19, 17), colorsDict["matrixGlasses"])
    elif decodedType == "DiamondVipers":

        imNew.putpixel((12, 14), colorsDict["black"])
        imNew.putpixel((13, 14), colorsDict["black"])
        imNew.putpixel((14, 14), colorsDict["black"])
        imNew.putpixel((15, 14), colorsDict["black"])
        imNew.putpixel((16, 14), colorsDict["black"])
        imNew.putpixel((17, 14), colorsDict["black"])
        imNew.putpixel((18, 14), colorsDict["black"])
        imNew.putpixel((19, 14), colorsDict["black"])
        imNew.putpixel((20, 14), colorsDict["black"])
        imNew.putpixel((21, 14), colorsDict["black"])

        imNew.putpixel((11, 15), colorsDict["black"])
        imNew.putpixel((12, 15), colorsDict["diamondVipers5"])
        imNew.putpixel((13, 15), colorsDict["diamondVipers4"])
        imNew.putpixel((14, 15), colorsDict["diamondVipers3"])
        imNew.putpixel((15, 15), colorsDict["diamondVipers2"])
        imNew.putpixel((16, 15), colorsDict["diamondVipers1"])
        imNew.putpixel((17, 15), colorsDict["diamondVipers2"])
        imNew.putpixel((18, 15), colorsDict["diamondVipers3"])
        imNew.putpixel((19, 15), colorsDict["diamondVipers4"])
        imNew.putpixel((20, 15), colorsDict["diamondVipers5"])
        imNew.putpixel((21, 15), colorsDict["diamondVipers6"])

        imNew.putpixel((9, 16), colorsDict["black"])
        imNew.putpixel((10, 16), colorsDict["black"])
        imNew.putpixel((11, 16), colorsDict["diamondVipers6"])
        imNew.putpixel((12, 16), colorsDict["diamondVipers5"])
        imNew.putpixel((13, 16), colorsDict["diamondVipers4"])
        imNew.putpixel((14, 16), colorsDict["diamondVipers3"])
        imNew.putpixel((15, 16), colorsDict["diamondVipers2"])
        imNew.putpixel((16, 16), colorsDict["diamondVipers1"])
        imNew.putpixel((17, 16), colorsDict["diamondVipers2"])
        imNew.putpixel((18, 16), colorsDict["diamondVipers3"])
        imNew.putpixel((19, 16), colorsDict["diamondVipers4"])
        imNew.putpixel((20, 16), colorsDict["diamondVipers5"])
        imNew.putpixel((21, 16), colorsDict["diamondVipers6"])

        imNew.putpixel((12, 17), colorsDict["diamondVipers5"])
        imNew.putpixel((13, 17), colorsDict["diamondVipers4"])
        imNew.putpixel((14, 17), colorsDict["diamondVipers3"])
        imNew.putpixel((15, 17), colorsDict["diamondVipers2"])
        imNew.putpixel((17, 17), colorsDict["diamondVipers2"])
        imNew.putpixel((18, 17), colorsDict["diamondVipers3"])
        imNew.putpixel((19, 17), colorsDict["diamondVipers4"])
        imNew.putpixel((20, 17), colorsDict["diamondVipers5"])
    elif decodedType == "AptosShades":

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

        imNew.putpixel((7, 11), colorsDict["black"])
        imNew.putpixel((8, 11), colorsDict["neo5"])
        imNew.putpixel((9, 11), colorsDict["neo4"])
        imNew.putpixel((10, 11), colorsDict["neo3"])
        imNew.putpixel((11, 11), colorsDict["neo2"])
        imNew.putpixel((12, 11), colorsDict["neo1"])
        imNew.putpixel((13, 11), colorsDict["neo2"])
        imNew.putpixel((14, 11), colorsDict["neo3"])
        imNew.putpixel((15, 11), colorsDict["neo4"])
        imNew.putpixel((16, 11), colorsDict["neo5"])
        imNew.putpixel((17, 11), colorsDict["neo6"])

        imNew.putpixel((5, 12), colorsDict["black"])
        imNew.putpixel((6, 12), colorsDict["black"])
        imNew.putpixel((7, 12), colorsDict["neo6"])
        imNew.putpixel((8, 12), colorsDict["neo5"])
        imNew.putpixel((9, 12), colorsDict["neo4"])
        imNew.putpixel((10, 12), colorsDict["neo3"])
        imNew.putpixel((11, 12), colorsDict["neo2"])
        imNew.putpixel((12, 12), colorsDict["neo1"])
        imNew.putpixel((13, 12), colorsDict["neo2"])
        imNew.putpixel((14, 12), colorsDict["neo3"])
        imNew.putpixel((15, 12), colorsDict["neo4"])
        imNew.putpixel((16, 12), colorsDict["neo5"])
        imNew.putpixel((17, 12), colorsDict["neo6"])

        imNew.putpixel((8, 13), colorsDict["neo5"])
        imNew.putpixel((9, 13), colorsDict["neo4"])
        imNew.putpixel((10, 13), colorsDict["neo3"])
        imNew.putpixel((11, 13), colorsDict["neo2"])
        imNew.putpixel((13, 13), colorsDict["neo2"])
        imNew.putpixel((14, 13), colorsDict["neo3"])
        imNew.putpixel((15, 13), colorsDict["neo4"])
        imNew.putpixel((16, 13), colorsDict["neo5"])
    elif decodedType == "GoldenVipers":

        imNew.putpixel((12, 14), colorsDict["black"])
        imNew.putpixel((13, 14), colorsDict["black"])
        imNew.putpixel((14, 14), colorsDict["black"])
        imNew.putpixel((15, 14), colorsDict["black"])
        imNew.putpixel((16, 14), colorsDict["black"])
        imNew.putpixel((17, 14), colorsDict["black"])
        imNew.putpixel((18, 14), colorsDict["black"])
        imNew.putpixel((19, 14), colorsDict["black"])
        imNew.putpixel((20, 14), colorsDict["black"])
        imNew.putpixel((21, 14), colorsDict["black"])

        imNew.putpixel((11, 15), colorsDict["black"])
        imNew.putpixel((12, 15), colorsDict["goldenVipers2"])
        imNew.putpixel((13, 15), colorsDict["goldenVipers3"])
        imNew.putpixel((14, 15), colorsDict["goldenVipers4"])
        imNew.putpixel((15, 15), colorsDict["goldenVipers5"])
        imNew.putpixel((16, 15), colorsDict["goldenVipers6"])
        imNew.putpixel((17, 15), colorsDict["goldenVipers5"])
        imNew.putpixel((18, 15), colorsDict["goldenVipers4"])
        imNew.putpixel((19, 15), colorsDict["goldenVipers3"])
        imNew.putpixel((20, 15), colorsDict["goldenVipers2"])
        imNew.putpixel((21, 15), colorsDict["goldenVipers1"])

        imNew.putpixel((9, 16), colorsDict["black"])
        imNew.putpixel((10, 16), colorsDict["black"])
        imNew.putpixel((11, 16), colorsDict["goldenVipers1"])
        imNew.putpixel((12, 16), colorsDict["goldenVipers2"])
        imNew.putpixel((13, 16), colorsDict["goldenVipers3"])
        imNew.putpixel((14, 16), colorsDict["goldenVipers4"])
        imNew.putpixel((15, 16), colorsDict["goldenVipers5"])
        imNew.putpixel((16, 16), colorsDict["goldenVipers6"])
        imNew.putpixel((17, 16), colorsDict["goldenVipers5"])
        imNew.putpixel((18, 16), colorsDict["goldenVipers4"])
        imNew.putpixel((19, 16), colorsDict["goldenVipers3"])
        imNew.putpixel((20, 16), colorsDict["goldenVipers2"])
        imNew.putpixel((21, 16), colorsDict["goldenVipers1"])

        imNew.putpixel((12, 17), colorsDict["goldenVipers2"])
        imNew.putpixel((13, 17), colorsDict["goldenVipers3"])
        imNew.putpixel((14, 17), colorsDict["goldenVipers4"])
        imNew.putpixel((15, 17), colorsDict["goldenVipers5"])
        imNew.putpixel((17, 17), colorsDict["goldenVipers5"])
        imNew.putpixel((18, 17), colorsDict["goldenVipers4"])
        imNew.putpixel((19, 17), colorsDict["goldenVipers3"])
        imNew.putpixel((20, 17), colorsDict["goldenVipers2"])

    elif decodedType == "SolanaShades":

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

        imNew.putpixel((7, 11), colorsDict["black"])
        imNew.putpixel((8, 11), colorsDict["solanaShades5"])
        imNew.putpixel((9, 11), colorsDict["solanaShades4"])
        imNew.putpixel((10, 11), colorsDict["solanaShades3"])
        imNew.putpixel((11, 11), colorsDict["solanaShades2"])
        imNew.putpixel((12, 11), colorsDict["solanaShades1"])
        imNew.putpixel((13, 11), colorsDict["solanaShades2"])
        imNew.putpixel((14, 11), colorsDict["solanaShades3"])
        imNew.putpixel((15, 11), colorsDict["solanaShades4"])
        imNew.putpixel((16, 11), colorsDict["solanaShades5"])
        imNew.putpixel((17, 11), colorsDict["solanaShades6"])

        imNew.putpixel((5, 12), colorsDict["black"])
        imNew.putpixel((6, 12), colorsDict["black"])
        imNew.putpixel((7, 12), colorsDict["solanaShades6"])
        imNew.putpixel((8, 12), colorsDict["solanaShades5"])
        imNew.putpixel((9, 12), colorsDict["solanaShades4"])
        imNew.putpixel((10, 12), colorsDict["solanaShades3"])
        imNew.putpixel((11, 12), colorsDict["solanaShades2"])
        imNew.putpixel((12, 12), colorsDict["solanaShades1"])
        imNew.putpixel((13, 12), colorsDict["solanaShades2"])
        imNew.putpixel((14, 12), colorsDict["solanaShades3"])
        imNew.putpixel((15, 12), colorsDict["solanaShades4"])
        imNew.putpixel((16, 12), colorsDict["solanaShades5"])
        imNew.putpixel((17, 12), colorsDict["solanaShades6"])

        imNew.putpixel((8, 13), colorsDict["solanaShades5"])
        imNew.putpixel((9, 13), colorsDict["solanaShades4"])
        imNew.putpixel((10, 13), colorsDict["solanaShades3"])
        imNew.putpixel((11, 13), colorsDict["solanaShades2"])
        imNew.putpixel((13, 13), colorsDict["solanaShades2"])
        imNew.putpixel((14, 13), colorsDict["solanaShades3"])
        imNew.putpixel((15, 13), colorsDict["solanaShades4"])
        imNew.putpixel((16, 13), colorsDict["solanaShades5"])

    elif decodedType == "LaserEyes":
        imNew.putpixel((12, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((13, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((14, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((15, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((16, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((17, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((18, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((19, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((20, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((21, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((22, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((23, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((24, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((25, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((26, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((27, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((28, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((29, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((30, 15), colorsDict["laserEyesOuter"])
        imNew.putpixel((31, 15), colorsDict["laserEyesOuter"])

        imNew.putpixel((11, 16), colorsDict["laserEyesOuter"])
        imNew.putpixel((12, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((13, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((14, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((15, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((16, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((17, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((18, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((19, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((20, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((21, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((22, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((23, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((24, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((25, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((26, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((27, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((28, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((29, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((30, 16), colorsDict["laserEyesInner"])
        imNew.putpixel((31, 16), colorsDict["laserEyesInner"])

        imNew.putpixel((12, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((13, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((14, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((15, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((16, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((17, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((18, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((19, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((20, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((21, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((22, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((23, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((24, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((25, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((26, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((27, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((28, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((29, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((30, 17), colorsDict["laserEyesOuter"])
        imNew.putpixel((31, 17), colorsDict["laserEyesOuter"])
    elif decodedType == "Solaneyes":
        imNew.putpixel((8, 12), colorsDict["solaneyesLeft"])
        imNew.putpixel((14, 12), colorsDict["solaneyesRight"])
    elif decodedType == "Monocle":
        imNew.putpixel((8, 11), colorsDict["monocleOutline"])
        imNew.putpixel((9, 11), colorsDict["monocleOutline"])

        imNew.putpixel((7, 12), colorsDict["monocleOutline"])
        imNew.putpixel((8, 12), colorsDict["monocle"])
        imNew.putpixel((9, 12), colorsDict["monocle"])
        imNew.putpixel((10, 12), colorsDict["monocleOutline"])

        imNew.putpixel((7, 13), colorsDict["monocleOutline"])
        imNew.putpixel((8, 13), colorsDict["monocle"])
        imNew.putpixel((9, 13), colorsDict["monocle"])
        imNew.putpixel((10, 13), colorsDict["monocleOutline"])

        imNew.putpixel((6, 14), colorsDict["monocleOutline"])
        imNew.putpixel((8, 14), colorsDict["monocleOutline"])
        imNew.putpixel((9, 14), colorsDict["monocleOutline"])

        imNew.putpixel((6, 15), colorsDict["monocleOutline"])

        imNew.putpixel((6, 16), colorsDict["monocleOutline"])

        imNew.putpixel((5, 17), colorsDict["monocleOutline"])

        imNew.putpixel((5, 18), colorsDict["monocleOutline"])

        imNew.putpixel((4, 19), colorsDict["monocleOutline"])
        imNew.putpixel((4, 20), colorsDict["monocleOutline"])
        imNew.putpixel((4, 21), colorsDict["monocleOutline"])
    elif decodedType == "Vice Shades":

        imNew.putpixel((5, 10), colorsDict["black"])
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

        imNew.putpixel((7, 11), colorsDict["black"])
        imNew.putpixel((8, 11), colorsDict["viceBrown"])
        imNew.putpixel((9, 11), colorsDict["viceBrown"])
        imNew.putpixel((10, 11), colorsDict["viceBrown"])
        imNew.putpixel((11, 11), colorsDict["viceBrown"])
        imNew.putpixel((12, 11), colorsDict["black"])
        imNew.putpixel((13, 11), colorsDict["viceBrown"])
        imNew.putpixel((14, 11), colorsDict["viceBrown"])
        imNew.putpixel((15, 11), colorsDict["viceBrown"])
        imNew.putpixel((16, 11), colorsDict["viceBrown"])
        imNew.putpixel((17, 11), colorsDict["black"])

        imNew.putpixel((7, 12), colorsDict["black"])
        imNew.putpixel((8, 12), colorsDict["viceBrownLight"])
        imNew.putpixel((9, 12), colorsDict["viceBrownLight"])
        imNew.putpixel((10, 12), colorsDict["viceBrownLight"])
        imNew.putpixel((11, 12), colorsDict["black"])
        imNew.putpixel((13, 12), colorsDict["black"])
        imNew.putpixel((14, 12), colorsDict["viceBrownLight"])
        imNew.putpixel((15, 12), colorsDict["viceBrownLight"])
        imNew.putpixel((16, 12), colorsDict["viceBrownLight"])
        imNew.putpixel((17, 12), colorsDict["black"])

        imNew.putpixel((7, 13), colorsDict["black"])
        imNew.putpixel((8, 13), colorsDict["black"])
        imNew.putpixel((9, 13), colorsDict["black"])
        imNew.putpixel((10, 13), colorsDict["black"])
        imNew.putpixel((14, 13), colorsDict["black"])
        imNew.putpixel((15, 13), colorsDict["black"])
        imNew.putpixel((16, 13), colorsDict["black"])
        imNew.putpixel((17, 13), colorsDict["black"])

    elif decodedType == "NavyThugLyfe":

        imNew.putpixel((8, 14), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((9, 14), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((10, 14), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((11, 14), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((12, 14), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((13, 14), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((14, 14), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((15, 14), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((16, 14), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((17, 14), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((18, 14), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((19, 14), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((20, 14), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((21, 14), colorsDict["navyThugLyfeOutline"])

        imNew.putpixel((10, 15), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((11, 15), colorsDict["navyThugLyfe"])
        imNew.putpixel((12, 15), colorsDict["navyThugLyfe"])
        imNew.putpixel((13, 15), colorsDict["navyThugLyfe"])
        imNew.putpixel((14, 15), colorsDict["white"])
        imNew.putpixel((15, 15), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((16, 15), colorsDict["navyThugLyfe"])
        imNew.putpixel((17, 15), colorsDict["navyThugLyfe"])
        imNew.putpixel((18, 15), colorsDict["navyThugLyfe"])
        imNew.putpixel((19, 15), colorsDict["navyThugLyfe"])
        imNew.putpixel((20, 15), colorsDict["white"])
        imNew.putpixel((21, 15), colorsDict["navyThugLyfeOutline"])

        imNew.putpixel((11, 16), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((12, 16), colorsDict["navyThugLyfe"])
        imNew.putpixel((13, 16), colorsDict["white"])
        imNew.putpixel((14, 16), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((16, 16), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((17, 16), colorsDict["navyThugLyfe"])
        imNew.putpixel((18, 16), colorsDict["navyThugLyfe"])
        imNew.putpixel((19, 16), colorsDict["white"])
        imNew.putpixel((20, 16), colorsDict["navyThugLyfeOutline"])

        imNew.putpixel((12, 17), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((13, 17), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((17, 17), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((18, 17), colorsDict["navyThugLyfeOutline"])
        imNew.putpixel((19, 17), colorsDict["navyThugLyfeOutline"])
    elif decodedType == "3dGlasses":

        imNew.putpixel((11, 14), colorsDict["white"])
        imNew.putpixel((12, 14), colorsDict["white"])
        imNew.putpixel((13, 14), colorsDict["white"])
        imNew.putpixel((14, 14), colorsDict["white"])
        imNew.putpixel((15, 14), colorsDict["white"])
        imNew.putpixel((16, 14), colorsDict["white"])
        imNew.putpixel((17, 14), colorsDict["white"])
        imNew.putpixel((18, 14), colorsDict["white"])
        imNew.putpixel((19, 14), colorsDict["white"])
        imNew.putpixel((20, 14), colorsDict["white"])
        imNew.putpixel((21, 14), colorsDict["white"])

        imNew.putpixel((10, 15), colorsDict["white"])
        imNew.putpixel((11, 15), colorsDict["white"])
        imNew.putpixel((12, 15), colorsDict["3dRed"])
        imNew.putpixel((13, 15), colorsDict["3dRedShade"])
        imNew.putpixel((14, 15), colorsDict["3dRed"])
        imNew.putpixel((15, 15), colorsDict["white"])
        imNew.putpixel((17, 15), colorsDict["white"])
        imNew.putpixel((18, 15), colorsDict["3dBlue"])
        imNew.putpixel((19, 15), colorsDict["3dBlueShade"])
        imNew.putpixel((20, 15), colorsDict["3dBlue"])
        imNew.putpixel((21, 15), colorsDict["white"])

        imNew.putpixel((9, 16), colorsDict["white"])
        imNew.putpixel((11, 16), colorsDict["white"])
        imNew.putpixel((12, 16), colorsDict["3dRed"])
        imNew.putpixel((13, 16), colorsDict["3dRed"])
        imNew.putpixel((14, 16), colorsDict["3dRedShade"])
        imNew.putpixel((15, 16), colorsDict["white"])
        imNew.putpixel((17, 16), colorsDict["white"])
        imNew.putpixel((18, 16), colorsDict["3dBlue"])
        imNew.putpixel((19, 16), colorsDict["3dBlue"])
        imNew.putpixel((20, 16), colorsDict["3dBlueShade"])
        imNew.putpixel((21, 16), colorsDict["white"])

        imNew.putpixel((12, 17), colorsDict["white"])
        imNew.putpixel((13, 17), colorsDict["white"])
        imNew.putpixel((14, 17), colorsDict["white"])
        imNew.putpixel((18, 17), colorsDict["white"])
        imNew.putpixel((19, 17), colorsDict["white"])
        imNew.putpixel((20, 17), colorsDict["white"])
    elif decodedType == "ThugLyfe":

        imNew.putpixel((8, 14), colorsDict["black"])
        imNew.putpixel((9, 14), colorsDict["black"])
        imNew.putpixel((10, 14), colorsDict["black"])
        imNew.putpixel((11, 14), colorsDict["black"])
        imNew.putpixel((12, 14), colorsDict["black"])
        imNew.putpixel((13, 14), colorsDict["black"])
        imNew.putpixel((14, 14), colorsDict["black"])
        imNew.putpixel((15, 14), colorsDict["black"])
        imNew.putpixel((16, 14), colorsDict["black"])
        imNew.putpixel((17, 14), colorsDict["black"])
        imNew.putpixel((18, 14), colorsDict["black"])
        imNew.putpixel((19, 14), colorsDict["black"])
        imNew.putpixel((20, 14), colorsDict["black"])
        imNew.putpixel((21, 14), colorsDict["black"])

        imNew.putpixel((10, 15), colorsDict["black"])
        imNew.putpixel((11, 15), colorsDict["black"])
        imNew.putpixel((12, 15), colorsDict["black"])
        imNew.putpixel((13, 15), colorsDict["black"])
        imNew.putpixel((14, 15), colorsDict["white"])
        imNew.putpixel((15, 15), colorsDict["black"])
        imNew.putpixel((16, 15), colorsDict["black"])
        imNew.putpixel((17, 15), colorsDict["black"])
        imNew.putpixel((18, 15), colorsDict["black"])
        imNew.putpixel((19, 15), colorsDict["black"])
        imNew.putpixel((20, 15), colorsDict["white"])
        imNew.putpixel((21, 15), colorsDict["black"])

        imNew.putpixel((11, 16), colorsDict["black"])
        imNew.putpixel((12, 16), colorsDict["black"])
        imNew.putpixel((13, 16), colorsDict["white"])
        imNew.putpixel((14, 16), colorsDict["black"])
        imNew.putpixel((16, 16), colorsDict["black"])
        imNew.putpixel((17, 16), colorsDict["black"])
        imNew.putpixel((18, 16), colorsDict["black"])
        imNew.putpixel((19, 16), colorsDict["white"])
        imNew.putpixel((20, 16), colorsDict["black"])

        imNew.putpixel((12, 17), colorsDict["black"])
        imNew.putpixel((13, 17), colorsDict["black"])
        imNew.putpixel((17, 17), colorsDict["black"])
        imNew.putpixel((18, 17), colorsDict["black"])
        imNew.putpixel((19, 17), colorsDict["black"])

    elif decodedType == "Tear":
        imNew.putpixel((12, 18), colorsDict["tears"])
        # imNew.putpixel((9, 14), colorsDict["tears"])
        # imNew.putpixel((14, 14), colorsDict["tears"])
        # imNew.putpixel((15, 14), colorsDict["tears"])

        # imNew.putpixel((8, 15), colorsDict["tears"])
        # imNew.putpixel((15, 15), colorsDict["tears"])

        # imNew.putpixel((8, 17), colorsDict["tears"])
    elif decodedType == "ClassyGlasses":

        imNew.putpixel((11, 14), colorsDict["monocleOutline"])
        imNew.putpixel((12, 14), colorsDict["monocleOutline"])
        imNew.putpixel((13, 14), colorsDict["monocleOutline"])
        imNew.putpixel((14, 14), colorsDict["monocleOutline"])
        imNew.putpixel((15, 14), colorsDict["monocleOutline"])
        imNew.putpixel((16, 14), colorsDict["monocleOutline"])
        imNew.putpixel((17, 14), colorsDict["monocleOutline"])
        imNew.putpixel((18, 14), colorsDict["monocleOutline"])
        imNew.putpixel((19, 14), colorsDict["monocleOutline"])
        imNew.putpixel((20, 14), colorsDict["monocleOutline"])

        imNew.putpixel((10, 15), colorsDict["monocleOutline"])
        imNew.putpixel((11, 15), colorsDict["glasses"])
        imNew.putpixel((12, 15), colorsDict["glassesLight"])
        imNew.putpixel((13, 15), colorsDict["glasses"])
        imNew.putpixel((14, 15), colorsDict["glasses"])
        imNew.putpixel((17, 15), colorsDict["glasses"])
        imNew.putpixel((18, 15), colorsDict["glassesLight"])
        imNew.putpixel((19, 15), colorsDict["glasses"])
        imNew.putpixel((20, 15), colorsDict["glasses"])

        imNew.putpixel((11, 16), colorsDict["glassesLight"])
        imNew.putpixel((12, 16), colorsDict["glasses"])
        imNew.putpixel((13, 16), colorsDict["glasses"])
        imNew.putpixel((14, 16), colorsDict["glasses"])
        imNew.putpixel((17, 16), colorsDict["glassesLight"])
        imNew.putpixel((18, 16), colorsDict["glasses"])
        imNew.putpixel((19, 16), colorsDict["glasses"])
        imNew.putpixel((20, 16), colorsDict["glasses"])

        imNew.putpixel((11, 17), colorsDict["glasses"])
        imNew.putpixel((12, 17), colorsDict["glasses"])
        imNew.putpixel((13, 17), colorsDict["glasses"])
        imNew.putpixel((14, 17), colorsDict["glasses"])
        imNew.putpixel((17, 17), colorsDict["glasses"])
        imNew.putpixel((18, 17), colorsDict["glasses"])
        imNew.putpixel((19, 17), colorsDict["glasses"])
        imNew.putpixel((20, 17), colorsDict["glasses"])


    elif decodedType == "AngryEyebrows":

        imNew.putpixel((13, 13), colorsDict["black"])
        imNew.putpixel((18, 13), colorsDict["black"])

        imNew.putpixel((14, 14), colorsDict["black"])
        imNew.putpixel((17, 14), colorsDict["black"])

    elif decodedType == "HeartEyes":

        imNew.putpixel((12, 14), colorsDict["heartEyesRed"])
        imNew.putpixel((14, 14), colorsDict["heartEyesRed"])
        imNew.putpixel((17, 14), colorsDict["heartEyesRed"])
        imNew.putpixel((19, 14), colorsDict["heartEyesRed"])

        imNew.putpixel((11, 15), colorsDict["heartEyesRed"])
        imNew.putpixel((12, 15), colorsDict["white"])
        imNew.putpixel((13, 15), colorsDict["heartEyesRed"])
        imNew.putpixel((14, 15), colorsDict["heartEyesRed"])
        imNew.putpixel((15, 15), colorsDict["heartEyesRed"])
        imNew.putpixel((16, 15), colorsDict["heartEyesRed"])
        imNew.putpixel((17, 15), colorsDict["white"])
        imNew.putpixel((18, 15), colorsDict["heartEyesRed"])
        imNew.putpixel((19, 15), colorsDict["heartEyesRed"])
        imNew.putpixel((20, 15), colorsDict["heartEyesRed"])

        imNew.putpixel((11, 16), colorsDict["heartEyesRed"])
        imNew.putpixel((12, 16), colorsDict["heartEyesRed"])
        imNew.putpixel((13, 16), colorsDict["heartEyesRed"])
        imNew.putpixel((14, 16), colorsDict["heartEyesRed"])
        imNew.putpixel((15, 16), colorsDict["heartEyesRedShade"])
        imNew.putpixel((16, 16), colorsDict["heartEyesRed"])
        imNew.putpixel((17, 16), colorsDict["heartEyesRed"])
        imNew.putpixel((18, 16), colorsDict["heartEyesRed"])
        imNew.putpixel((19, 16), colorsDict["heartEyesRed"])
        imNew.putpixel((20, 16), colorsDict["heartEyesRedShade"])

        imNew.putpixel((12, 17), colorsDict["heartEyesRed"])
        imNew.putpixel((13, 17), colorsDict["heartEyesRed"])
        imNew.putpixel((14, 17), colorsDict["heartEyesRedShade"])
        imNew.putpixel((17, 17), colorsDict["heartEyesRed"])
        imNew.putpixel((18, 17), colorsDict["heartEyesRed"])
        imNew.putpixel((19, 17), colorsDict["heartEyesRedShade"])

        imNew.putpixel((13, 18), colorsDict["heartEyesRedShade"])
        imNew.putpixel((18, 18), colorsDict["heartEyesRedShade"])

    elif decodedType == "Cyclops":

        imNew.putpixel((6, 10), colorsDict["black"])
        imNew.putpixel((8, 10), colorsDict["black"])
        imNew.putpixel((9, 10), colorsDict["black"])
        imNew.putpixel((10, 10), colorsDict["black"])
        imNew.putpixel((11, 10), colorsDict["black"])
        imNew.putpixel((12, 10), colorsDict["black"])
        imNew.putpixel((13, 10), colorsDict["black"])
        imNew.putpixel((14, 10), colorsDict["black"])
        imNew.putpixel((15, 10), colorsDict["black"])

        imNew.putpixel((5, 11), colorsDict["black"])
        imNew.putpixel((6, 11), colorsDict["cyclopsYellowShade"])
        imNew.putpixel((7, 11), colorsDict["black"])
        imNew.putpixel((8, 11), colorsDict["cyclopsYellowShade"])
        imNew.putpixel((9, 11), colorsDict["cyclopsYellow"])
        imNew.putpixel((10, 11), colorsDict["cyclopsYellow"])
        imNew.putpixel((11, 11), colorsDict["cyclopsYellow"])
        imNew.putpixel((12, 11), colorsDict["cyclopsYellow"])
        imNew.putpixel((13, 11), colorsDict["cyclopsYellow"])
        imNew.putpixel((14, 11), colorsDict["cyclopsYellow"])
        imNew.putpixel((15, 11), colorsDict["cyclopsYellow"])
        imNew.putpixel((16, 11), colorsDict["black"])

        imNew.putpixel((4, 12), colorsDict["black"])
        imNew.putpixel((5, 12), colorsDict["cyclopsYellowShade"])
        imNew.putpixel((6, 12), colorsDict["cyclopsYellow"])
        imNew.putpixel((7, 12), colorsDict["cyclopsYellow"])
        imNew.putpixel((8, 12), colorsDict["cyclopsRed"])
        imNew.putpixel((9, 12), colorsDict["cyclopsRed"])
        imNew.putpixel((10, 12), colorsDict["cyclopsRed"])
        imNew.putpixel((11, 12), colorsDict["cyclopsRed"])
        imNew.putpixel((12, 12), colorsDict["cyclopsRed"])
        imNew.putpixel((13, 12), colorsDict["cyclopsRed"])
        imNew.putpixel((14, 12), colorsDict["cyclopsRed"])
        imNew.putpixel((15, 12), colorsDict["cyclopsRed"])
        imNew.putpixel((16, 12), colorsDict["cyclopsYellowShade"])
        imNew.putpixel((17, 12), colorsDict["black"])

        imNew.putpixel((5, 13), colorsDict["black"])
        imNew.putpixel((6, 13), colorsDict["cyclopsYellow"])
        imNew.putpixel((7, 13), colorsDict["black"])
        imNew.putpixel((8, 13), colorsDict["cyclopsYellow"])
        imNew.putpixel((9, 13), colorsDict["cyclopsYellow"])
        imNew.putpixel((10, 13), colorsDict["cyclopsYellow"])
        imNew.putpixel((11, 13), colorsDict["cyclopsYellow"])
        imNew.putpixel((12, 13), colorsDict["cyclopsYellow"])
        imNew.putpixel((13, 13), colorsDict["cyclopsYellow"])
        imNew.putpixel((14, 13), colorsDict["cyclopsYellow"])
        imNew.putpixel((15, 13), colorsDict["cyclopsYellowShade"])
        imNew.putpixel((16, 13), colorsDict["black"])

        imNew.putpixel((6, 14), colorsDict["black"])
        imNew.putpixel((8, 14), colorsDict["black"])
        imNew.putpixel((9, 14), colorsDict["black"])
        imNew.putpixel((10, 14), colorsDict["black"])
        imNew.putpixel((11, 14), colorsDict["black"])
        imNew.putpixel((12, 14), colorsDict["black"])
        imNew.putpixel((13, 14), colorsDict["black"])
        imNew.putpixel((14, 14), colorsDict["black"])
        imNew.putpixel((15, 14), colorsDict["black"])

    elif decodedType == "GoogleyEyes":

        imNew.putpixel((8, 10), colorsDict["black"])
        imNew.putpixel((9, 10), colorsDict["black"])
        imNew.putpixel((14, 10), colorsDict["black"])
        imNew.putpixel((15, 10), colorsDict["black"])

        imNew.putpixel((7, 11), colorsDict["black"])
        imNew.putpixel((8, 11), colorsDict["black"])
        imNew.putpixel((9, 11), colorsDict["white"])
        imNew.putpixel((10, 11), colorsDict["black"])
        imNew.putpixel((13, 11), colorsDict["black"])
        imNew.putpixel((14, 11), colorsDict["white"])
        imNew.putpixel((15, 11), colorsDict["white"])
        imNew.putpixel((16, 11), colorsDict["black"])

        imNew.putpixel((7, 12), colorsDict["black"])
        imNew.putpixel((8, 12), colorsDict["white"])
        imNew.putpixel((9, 12), colorsDict["white"])
        imNew.putpixel((10, 12), colorsDict["black"])
        imNew.putpixel((13, 12), colorsDict["black"])
        imNew.putpixel((14, 12), colorsDict["white"])
        imNew.putpixel((15, 12), colorsDict["black"])
        imNew.putpixel((16, 12), colorsDict["black"])

        imNew.putpixel((8, 13), colorsDict["black"])
        imNew.putpixel((9, 13), colorsDict["black"])
        imNew.putpixel((14, 13), colorsDict["black"])
        imNew.putpixel((15, 13), colorsDict["black"])

    im.paste(imNew, (0,0), mask=imNew)
