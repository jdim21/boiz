from PIL import Image
from colors import colorsDict, backgroundLookup
from traitEncodings import TRAIT_ENCODINGS
from draw.drawShirt import drawShirt
from draw.drawCollaredShirt import drawCollaredShirt
from draw.drawSuit import drawSuit
from draw.drawHoodie import drawHoodie
from draw.drawScarf import drawScarf
from draw.drawBowtie import drawBowtie
from draw.drawNecklace import drawNecklace

def drawBody(im, trait, typeEncoding, backgroundColor):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    decodedType = TRAIT_ENCODINGS["type"][typeEncoding]
    colorBlack = (0, 0, 0)
    if decodedType == "Normal":
        primaryColor = "typeNormal"
        colorShade = "typeNormalShade"
    elif decodedType == "Snowy":
        primaryColor = "typeSnowy"
        colorShade = "typeSnowyShade"
    elif decodedType == "Light":
        primaryColor = "typeLight"
        colorShade = "typeLightShade"
    elif decodedType == "Dark":
        primaryColor = "typeDark"
        colorShade = "typeDarkShade"
    elif decodedType == "Brown":
        primaryColor = "typeBrown"
        colorShade = "typeBrownShade"
    elif decodedType == "DarkBrown":
        primaryColor = "typeDarkBrown"
        colorShade = "typeDarkBrownShade"
    elif decodedType == "Black":
        primaryColor = "typeBlack"
        colorShade = "typeBlackShade"
    elif decodedType == "Skeleton":
        primaryColor = "typeSkeleton"
        colorShade = "typeSkeletonShade"
    elif decodedType == "Alien":
        primaryColor = "typeAlien"
        colorShade = "typeAlienShade"
    elif decodedType == "Zombie":
        primaryColor = "typeZombie"
        colorShade = "typeZombieShade"
    elif decodedType == "Devil":
        primaryColor = "typeDevil"
        colorShade = "typeDevilShade"
    elif decodedType == "Ghost":
        primaryColor = "typeGhost"
        colorShade = "typeGhostShade"
        colorBlack = (0, 0, 0, 128)

    decodedBody = TRAIT_ENCODINGS["body"][trait]
    if decodedBody == "SolanaHoodie":
        drawHoodie(im, "dark")
        imNew.putpixel((7, 21), backgroundLookup[backgroundColor])
        imNew.putpixel((8, 21), backgroundLookup[backgroundColor])
        #imNew.putpixel((7, 22), colorsDict["backgroundGreennt(len(colorsDict["solanaBand"])/2)])
        #imNew.putpixel((8, 22), colorsDict["backgroundGreennt(len(colorsDict["solanaBand"])/2)])
        imNew.putpixel((7, 22), backgroundLookup[backgroundColor])
        imNew.putpixel((8, 22), backgroundLookup[backgroundColor])
        imNew.putpixel((7, 23), backgroundLookup[backgroundColor])
        imNew.putpixel((8, 23), backgroundLookup[backgroundColor])
    elif decodedBody == "BlueHoodie":
        drawHoodie(im, "blueHoodie")
    elif decodedBody == "YellowHoodie":
        drawHoodie(im, "yellowHoodie")
    elif decodedBody == "OrangeHoodie":
        drawHoodie(im, "orangeHoodie")
    elif decodedBody == "PurpleHoodie":
        drawHoodie(im, "purpleHoodie")
    elif decodedBody == "BlackHoodie":
        drawHoodie(im, "dark")
    elif decodedBody == "GrayHoodie":
        drawHoodie(im, "grayHoodie")
    elif decodedBody == "RedCollared":
        drawCollaredShirt(im, "red")
    elif decodedBody == "LightBlueCollared":
        drawCollaredShirt(im, "skyBlue")
    elif decodedBody == "BlueCollared":
        drawCollaredShirt(im, "blue")
    elif decodedBody == "PinkCollared":
        drawCollaredShirt(im, "pink")
    elif decodedBody == "YellowCollared":
        drawCollaredShirt(im, "yellow")
    elif decodedBody == "GreenCollared":
        drawCollaredShirt(im, "green")
    elif decodedBody == "Fat":
        imNew.putpixel((0, 17), backgroundLookup[backgroundColor])
        imNew.putpixel((1, 17), backgroundLookup[backgroundColor])
        imNew.putpixel((2, 17), backgroundLookup[backgroundColor])
        imNew.putpixel((3, 17), backgroundLookup[backgroundColor])
        imNew.putpixel((4, 17), colorBlack)
        imNew.putpixel((5, 17), colorBlack)

        imNew.putpixel((0, 18), backgroundLookup[backgroundColor])
        imNew.putpixel((1, 18), backgroundLookup[backgroundColor])
        imNew.putpixel((2, 18), colorBlack)
        imNew.putpixel((3, 18), colorBlack)
        imNew.putpixel((4, 18), colorsDict[colorShade])
        imNew.putpixel((5, 18), colorsDict[colorShade])
        imNew.putpixel((6, 18), colorsDict[colorShade])

        imNew.putpixel((0, 19), backgroundLookup[backgroundColor])
        imNew.putpixel((1, 19), backgroundLookup[backgroundColor])
        imNew.putpixel((1, 19), colorBlack)
        imNew.putpixel((2, 19), colorsDict[colorShade])
        imNew.putpixel((3, 19), colorsDict[colorShade])
        imNew.putpixel((4, 19), colorsDict[primaryColor])
        imNew.putpixel((5, 19), colorsDict[primaryColor])
        imNew.putpixel((6, 19), colorsDict[primaryColor])
        imNew.putpixel((7, 19), colorsDict[primaryColor])

        imNew.putpixel((0, 20), colorBlack)
        imNew.putpixel((1, 20), colorsDict[colorShade])
        imNew.putpixel((2, 20), colorsDict[primaryColor])
        imNew.putpixel((3, 20), colorsDict[primaryColor])
        imNew.putpixel((4, 20), colorsDict[primaryColor])
        imNew.putpixel((5, 20), colorsDict[primaryColor])
        imNew.putpixel((6, 20), colorsDict[primaryColor])
        imNew.putpixel((7, 20), colorsDict[primaryColor])

        imNew.putpixel((0, 21), colorsDict[colorShade])
        imNew.putpixel((1, 21), colorsDict[primaryColor])
        imNew.putpixel((2, 21), colorsDict[primaryColor])
        imNew.putpixel((3, 21), colorsDict[primaryColor])
        imNew.putpixel((4, 21), colorsDict[primaryColor])
        imNew.putpixel((5, 21), colorsDict[primaryColor])
        imNew.putpixel((6, 21), colorsDict[primaryColor])
        imNew.putpixel((7, 21), colorsDict[primaryColor])

        imNew.putpixel((0, 22), colorsDict[primaryColor])
        imNew.putpixel((1, 22), colorsDict[primaryColor])
        imNew.putpixel((2, 22), colorsDict[primaryColor])
        imNew.putpixel((3, 22), colorsDict[primaryColor])
        imNew.putpixel((4, 22), colorsDict[primaryColor])
        imNew.putpixel((5, 22), colorsDict[primaryColor])
        imNew.putpixel((6, 22), colorsDict[primaryColor])
        imNew.putpixel((7, 22), colorsDict[primaryColor])

        imNew.putpixel((0, 23), colorsDict[primaryColor])
        imNew.putpixel((1, 23), colorsDict[primaryColor])
        imNew.putpixel((2, 23), colorsDict[primaryColor])
        imNew.putpixel((3, 23), colorsDict[primaryColor])
        imNew.putpixel((4, 23), colorsDict[primaryColor])
        imNew.putpixel((5, 23), colorsDict[primaryColor])
        imNew.putpixel((6, 23), colorsDict[primaryColor])
        imNew.putpixel((7, 23), colorsDict[primaryColor])

    elif decodedBody == "MuddyPaws":
        imNew.putpixel((10, 23), colorsDict["muddyPaws"])
        imNew.putpixel((11, 23), colorsDict["muddyPaws"])
        imNew.putpixel((13, 23), colorsDict["muddyPaws"])
        imNew.putpixel((14, 23), colorsDict["muddyPaws"])
    elif decodedBody == "CheckeredShirt":
        imNew.putpixel((7, 19), colorsDict["plaidRedShade"])
        imNew.putpixel((8, 19), colorsDict["plaidBlack"])

        imNew.putpixel((6, 20), colorsDict["plaidRedShade"])
        imNew.putpixel((7, 20), colorsDict["plaidBlack"])
        imNew.putpixel((8, 20), colorsDict["plaidRed"])
        imNew.putpixel((9, 20), colorsDict["black"])
        imNew.putpixel((13, 20), colorsDict["black"])
        imNew.putpixel((14, 20), colorsDict["plaidRed"])

        imNew.putpixel((5, 21), colorsDict["plaidRedShade"])
        imNew.putpixel((6, 21), colorsDict["plaidBlack"])
        imNew.putpixel((7, 21), colorsDict["plaidRed"])
        imNew.putpixel((8, 21), colorsDict["plaidBlack"])
        imNew.putpixel((9, 21), colorsDict["plaidRed"])
        imNew.putpixel((10, 21), colorsDict["black"])
        imNew.putpixel((12, 21), colorsDict["black"])
        imNew.putpixel((13, 21), colorsDict["plaidRed"])
        imNew.putpixel((14, 21), colorsDict["plaidBlack"])

        imNew.putpixel((4, 22), colorsDict["plaidRedShade"])
        imNew.putpixel((5, 22), colorsDict["plaidBlack"])
        imNew.putpixel((6, 22), colorsDict["plaidRed"])
        imNew.putpixel((7, 22), colorsDict["plaidBlack"])
        imNew.putpixel((8, 22), colorsDict["plaidRed"])
        imNew.putpixel((9, 22), colorsDict["plaidBlack"])
        imNew.putpixel((10, 22), colorsDict["plaidRed"])
        imNew.putpixel((11, 22), colorsDict["black"])
        imNew.putpixel((12, 22), colorsDict["plaidRed"])
        imNew.putpixel((13, 22), colorsDict["plaidBlack"])
        imNew.putpixel((14, 22), colorsDict["plaidRed"])

        imNew.putpixel((3, 23), colorsDict["plaidRedShade"])
        imNew.putpixel((4, 23), colorsDict["plaidBlack"])
        imNew.putpixel((5, 23), colorsDict["plaidRed"])
        imNew.putpixel((6, 23), colorsDict["plaidBlack"])
        imNew.putpixel((7, 23), colorsDict["plaidRed"])
        imNew.putpixel((8, 23), colorsDict["plaidBlack"])
        imNew.putpixel((9, 23), colorsDict["black"])
        imNew.putpixel((10, 23), colorsDict["plaidBlackShade"])
        imNew.putpixel((11, 23), colorsDict["plaidRedShade"])
        imNew.putpixel((12, 23), colorsDict["black"])
        imNew.putpixel((13, 23), colorsDict["plaidRedShade"])
        imNew.putpixel((14, 23), colorsDict["plaidBlackShade"])
    elif decodedBody == "BitcoinShirt":
        drawShirt(im, "bitcoin")
        imNew.putpixel((7, 19), colorsDict["bitcoinLabelShade"])
        imNew.putpixel((8, 19), colorsDict["bitcoinLabel"])

        imNew.putpixel((7, 20), colorsDict["bitcoinLabel"])
        imNew.putpixel((9, 20), colorsDict["bitcoinLabelShade"])

        imNew.putpixel((7, 21), colorsDict["bitcoinLabel"])
        imNew.putpixel((8, 21), colorsDict["bitcoinLabel"])
        imNew.putpixel((14, 21), colorsDict["bitcoinShirtShade"])

        imNew.putpixel((6, 22), colorsDict["bitcoinShirtShade"])
        imNew.putpixel((7, 22), colorsDict["bitcoinLabel"])
        imNew.putpixel((9, 22), colorsDict["bitcoinLabel"])
        imNew.putpixel((12, 22), colorsDict["bitcoinShirtShade"])

        imNew.putpixel((5, 23), colorsDict["bitcoinShirtShade"])
        imNew.putpixel((7, 23), colorsDict["bitcoinLabel"])
        imNew.putpixel((8, 23), colorsDict["bitcoinLabel"])

    elif decodedBody == "PinkShirt":
        drawShirt(im, "pink")
    elif decodedBody == "RainbowShirt":
        imNew.putpixel((7, 19), colorsDict["rainbowBlueShade"])
        imNew.putpixel((8, 19), colorsDict["rainbowBlue"])

        imNew.putpixel((1, 20), colorsDict["rainbowPurple"])
        imNew.putpixel((6, 20), colorsDict["rainbowGreenShade"])
        imNew.putpixel((7, 20), colorsDict["rainbowGreen"])
        imNew.putpixel((8, 20), colorsDict["rainbowGreen"])
        imNew.putpixel((9, 20), colorsDict["black"])
        imNew.putpixel((13, 20), colorsDict["black"])
        imNew.putpixel((14, 20), colorsDict["rainbowGreen"])

        imNew.putpixel((0, 21), colorsDict["rainbowYellow"])
        imNew.putpixel((5, 21), colorsDict["rainbowYellowShade"])
        imNew.putpixel((6, 21), colorsDict["rainbowYellow"])
        imNew.putpixel((7, 21), colorsDict["rainbowYellow"])
        imNew.putpixel((8, 21), colorsDict["rainbowYellow"])
        imNew.putpixel((9, 21), colorsDict["rainbowYellow"])
        imNew.putpixel((10, 21), colorsDict["black"])
        imNew.putpixel((11, 21), colorsDict["black"])
        imNew.putpixel((12, 21), colorsDict["black"])
        imNew.putpixel((13, 21), colorsDict["rainbowYellow"])
        imNew.putpixel((14, 21), colorsDict["rainbowYellow"])

        imNew.putpixel((0, 22), colorsDict["rainbowOrange"])
        imNew.putpixel((4, 22), colorsDict["rainbowOrangeShade"])
        imNew.putpixel((5, 22), colorsDict["rainbowOrange"])
        imNew.putpixel((6, 22), colorsDict["rainbowOrange"])
        imNew.putpixel((7, 22), colorsDict["rainbowOrange"])
        imNew.putpixel((8, 22), colorsDict["rainbowOrange"])
        imNew.putpixel((9, 22), colorsDict["rainbowOrange"])
        imNew.putpixel((10, 22), colorsDict["rainbowOrange"])
        imNew.putpixel((11, 22), colorsDict["rainbowOrange"])
        imNew.putpixel((12, 22), colorsDict["rainbowOrange"])
        imNew.putpixel((13, 22), colorsDict["rainbowOrange"])
        imNew.putpixel((14, 22), colorsDict["rainbowOrange"])

        imNew.putpixel((0, 23), colorsDict["rainbowRed"])
        imNew.putpixel((3, 23), colorsDict["rainbowRedShade"])
        imNew.putpixel((4, 23), colorsDict["rainbowRed"])
        imNew.putpixel((5, 23), colorsDict["rainbowRed"])
        imNew.putpixel((6, 23), colorsDict["rainbowRed"])
        imNew.putpixel((7, 23), colorsDict["rainbowRed"])
        imNew.putpixel((8, 23), colorsDict["rainbowRed"])
        imNew.putpixel((9, 23), colorsDict["black"])
        imNew.putpixel((10, 23), colorsDict["rainbowRedShade"])
        imNew.putpixel((11, 23), colorsDict["rainbowRedShade"])
        imNew.putpixel((12, 23), colorsDict["black"])
        imNew.putpixel((13, 23), colorsDict["rainbowRedShade"])
        imNew.putpixel((14, 23), colorsDict["rainbowRedShade"])

        if typeEncoding == "v":
            imNew.putpixel((0, 18), colorsDict["rainbowPurple"])
            imNew.putpixel((1, 18), colorsDict["rainbowPurple"])
            imNew.putpixel((2, 19), colorsDict["rainbowPurple"])
            imNew.putpixel((1, 20), colorsDict["black"])
            imNew.putpixel((2, 20), colorsDict["rainbowPurple"])

    elif decodedBody == "Referee":
        drawShirt(im, "white")
        imNew.putpixel((7, 19), colorsDict["refereeStripeShade"])

        imNew.putpixel((7, 20), colorsDict["refereeStripe"])

        imNew.putpixel((5, 21), colorsDict["refereeStripeShade"])
        imNew.putpixel((7, 21), colorsDict["refereeStripe"])
        imNew.putpixel((9, 21), colorsDict["refereeStripe"])
        imNew.putpixel((13, 21), colorsDict["refereeStripe"])

        imNew.putpixel((5, 22), colorsDict["refereeStripe"])
        imNew.putpixel((7, 22), colorsDict["refereeStripe"])
        imNew.putpixel((9, 22), colorsDict["refereeStripe"])
        imNew.putpixel((11, 22), colorsDict["refereeStripe"])
        imNew.putpixel((13, 22), colorsDict["refereeStripe"])

        imNew.putpixel((3, 23), colorsDict["refereeStripeShade"])
        imNew.putpixel((5, 23), colorsDict["refereeStripe"])
        imNew.putpixel((7, 23), colorsDict["refereeStripe"])
        imNew.putpixel((11, 23), colorsDict["refereeStripeShade"])
        imNew.putpixel((13, 23), colorsDict["refereeStripeShade"])
    elif decodedBody == "ConeOfShame":
        imNew.putpixel((2, 16), colorsDict["coneOfShameOutline"])
        imNew.putpixel((3, 16), colorsDict["coneOfShameOutline"])
        imNew.putpixel((4, 16), colorsDict["coneOfShameOutline"])
        imNew.putpixel((5, 16), colorsDict["coneOfShameOutline"])
        imNew.putpixel((18, 16), colorsDict["coneOfShameOutline"])
        imNew.putpixel((19, 16), colorsDict["coneOfShameOutline"])
        imNew.putpixel((20, 16), colorsDict["coneOfShameOutline"])
        imNew.putpixel((21, 16), colorsDict["coneOfShameOutline"])

        imNew.putpixel((3, 17), colorsDict["coneOfShameOutline"])
        imNew.putpixel((4, 17), colorsDict["coneOfShame"])
        imNew.putpixel((5, 17), colorsDict["coneOfShame"])
        imNew.putpixel((6, 17), colorsDict["coneOfShameOutline"])
        imNew.putpixel((7, 17), colorsDict["coneOfShameOutline"])
        imNew.putpixel((8, 17), colorsDict["coneOfShameOutline"])
        imNew.putpixel((15, 17), colorsDict["coneOfShameOutline"])
        imNew.putpixel((16, 17), colorsDict["coneOfShameOutline"])
        imNew.putpixel((17, 17), colorsDict["coneOfShameOutline"])
        imNew.putpixel((18, 17), colorsDict["coneOfShame"])
        imNew.putpixel((19, 17), colorsDict["coneOfShame"])
        imNew.putpixel((20, 17), colorsDict["coneOfShameOutline"])

        imNew.putpixel((4, 18), colorsDict["coneOfShameOutline"])
        imNew.putpixel((5, 18), colorsDict["coneOfShame"])
        imNew.putpixel((6, 18), colorsDict["coneOfShame"])
        imNew.putpixel((7, 18), colorsDict["coneOfShame"])
        imNew.putpixel((8, 18), colorsDict["coneOfShame"])
        imNew.putpixel((9, 18), colorsDict["coneOfShameOutline"])
        imNew.putpixel((10, 18), colorsDict["coneOfShameOutline"])
        imNew.putpixel((11, 18), colorsDict["coneOfShameOutline"])
        imNew.putpixel((12, 18), colorsDict["coneOfShameOutline"])
        imNew.putpixel((13, 18), colorsDict["coneOfShameOutline"])
        imNew.putpixel((14, 18), colorsDict["coneOfShameOutline"])
        imNew.putpixel((15, 18), colorsDict["coneOfShame"])
        imNew.putpixel((16, 18), colorsDict["coneOfShame"])
        imNew.putpixel((17, 18), colorsDict["coneOfShame"])
        imNew.putpixel((18, 18), colorsDict["coneOfShame"])
        imNew.putpixel((19, 18), colorsDict["coneOfShameOutline"])

        imNew.putpixel((5, 19), colorsDict["coneOfShameOutline"])
        imNew.putpixel((6, 19), colorsDict["coneOfShame"])
        imNew.putpixel((7, 19), colorsDict["coneOfShame"])
        imNew.putpixel((8, 19), colorsDict["coneOfShame"])
        imNew.putpixel((9, 19), colorsDict["coneOfShame"])
        imNew.putpixel((10, 19), colorsDict["coneOfShame"])
        imNew.putpixel((11, 19), colorsDict["coneOfShame"])
        imNew.putpixel((12, 19), colorsDict["coneOfShame"])
        imNew.putpixel((13, 19), colorsDict["coneOfShame"])
        imNew.putpixel((14, 19), colorsDict["coneOfShame"])
        imNew.putpixel((15, 19), colorsDict["coneOfShame"])
        imNew.putpixel((16, 19), colorsDict["coneOfShame"])
        imNew.putpixel((17, 19), colorsDict["coneOfShame"])
        imNew.putpixel((18, 19), colorsDict["coneOfShameOutline"])

        imNew.putpixel((6, 20), colorsDict["coneOfShameOutline"])
        imNew.putpixel((7, 20), colorsDict["coneOfShame"])
        imNew.putpixel((8, 20), colorsDict["coneOfShame"])
        imNew.putpixel((9, 20), colorsDict["coneOfShame"])
        imNew.putpixel((10, 20), colorsDict["coneOfShame"])
        imNew.putpixel((11, 20), colorsDict["coneOfShame"])
        imNew.putpixel((12, 20), colorsDict["coneOfShame"])
        imNew.putpixel((13, 20), colorsDict["coneOfShame"])
        imNew.putpixel((14, 20), colorsDict["coneOfShame"])
        imNew.putpixel((15, 20), colorsDict["coneOfShame"])
        imNew.putpixel((16, 20), colorsDict["coneOfShame"])
        imNew.putpixel((17, 20), colorsDict["coneOfShameOutline"])

        imNew.putpixel((7, 21), colorsDict["coneOfShameOutline"])
        imNew.putpixel((8, 21), colorsDict["coneOfShameOutline"])
        imNew.putpixel((9, 21), colorsDict["coneOfShameOutline"])
        imNew.putpixel((10, 21), colorsDict["coneOfShameOutline"])
        imNew.putpixel((11, 21), colorsDict["coneOfShameOutline"])
        imNew.putpixel((12, 21), colorsDict["coneOfShameOutline"])
        imNew.putpixel((13, 21), colorsDict["coneOfShameOutline"])
        imNew.putpixel((14, 21), colorsDict["coneOfShameOutline"])
        imNew.putpixel((15, 21), colorsDict["coneOfShameOutline"])
        imNew.putpixel((16, 21), colorsDict["coneOfShameOutline"])
    elif decodedBody == "PikaTail":
        imNew.putpixel((2, 15), colorsDict["black"])

        imNew.putpixel((1, 16), colorsDict["black"])
        imNew.putpixel((2, 16), colorsDict["pikaTailShade"])
        imNew.putpixel((3, 16), colorsDict["black"])

        imNew.putpixel((0, 17), colorsDict["black"])
        imNew.putpixel((1, 17), colorsDict["pikaTailShade"])
        imNew.putpixel((2, 17), colorsDict["pikaTail"])
        imNew.putpixel((3, 17), colorsDict["pikaTail"])
        imNew.putpixel((4, 17), colorsDict["black"])

        imNew.putpixel((0, 18), colorsDict["pikaTailShade"])
        imNew.putpixel((1, 18), colorsDict["pikaTail"])
        imNew.putpixel((2, 18), colorsDict["pikaTail"])
        imNew.putpixel((3, 18), colorsDict["black"])

        imNew.putpixel((0, 19), colorsDict["pikaTail"])
        imNew.putpixel((1, 19), colorsDict["black"])
        imNew.putpixel((2, 19), colorsDict["black"])
        imNew.putpixel((3, 19), backgroundLookup[backgroundColor])

        imNew.putpixel((0, 20), colorsDict["black"])
        imNew.putpixel((1, 20), colorsDict["pikaTail"])
        imNew.putpixel((2, 20), colorsDict["black"])
        imNew.putpixel((3, 20), backgroundLookup[backgroundColor])

        imNew.putpixel((0, 21), backgroundLookup[backgroundColor])
        imNew.putpixel((1, 21), colorsDict["black"])
        imNew.putpixel((2, 21), colorsDict["pikaTail"])
        imNew.putpixel((3, 21), colorsDict["black"])

        imNew.putpixel((0, 22), colorsDict["black"])
        imNew.putpixel((1, 22), colorsDict["pikaTail"])
        imNew.putpixel((2, 22), colorsDict["black"])

        imNew.putpixel((0, 23), colorsDict["pikaTail"])
        imNew.putpixel((1, 23), colorsDict["black"])
    elif decodedBody == "Tutu":
        drawShirt(im, "tutu")
        imNew.putpixel((4, 20), colorsDict["tutuOutline"])

        imNew.putpixel((2, 21), colorsDict["tutuOutline"])
        imNew.putpixel((3, 21), colorsDict["tutuOutline"])
        imNew.putpixel((4, 21), colorsDict["tutuShade"])
        imNew.putpixel((5, 21), colorsDict["tutuOutline"])

        imNew.putpixel((1, 22), colorsDict["tutuOutline"])
        imNew.putpixel((2, 22), colorsDict["tutuShade"])
        imNew.putpixel((3, 22), colorsDict["tutu"])
        imNew.putpixel((4, 22), colorsDict["tutuOutline"])
        imNew.putpixel((5, 22), colorsDict["tutuShade"])
        imNew.putpixel((6, 22), colorsDict["tutuOutline"])
        imNew.putpixel((7, 22), colorsDict["tutuOutline"])

        imNew.putpixel((0, 23), colorsDict["tutuOutline"])
        imNew.putpixel((1, 23), colorsDict["tutuShade"])
        imNew.putpixel((2, 23), colorsDict["tutu"])
        imNew.putpixel((3, 23), colorsDict["tutuOutline"])
        imNew.putpixel((4, 23), colorsDict["tutuShade"])
        imNew.putpixel((5, 23), colorsDict["tutu"])
        imNew.putpixel((6, 23), colorsDict["tutuOutline"])
        imNew.putpixel((7, 23), colorsDict["tutuShade"])
        imNew.putpixel((8, 23), colorsDict["tutuOutline"])
    elif decodedBody == "LimeShirt":
        drawShirt(im, "lime")
    elif decodedBody == "WhiteShirt":
        drawShirt(im, "white")
    elif decodedBody == "DarkShirt":
        drawShirt(im, "dark")
    elif decodedBody == "PurpleShirt":
        drawShirt(im, "purple")
    elif decodedBody == "RedAndBlue":
        drawShirt(im, "stripes2")
        imNew.putpixel((6, 20), colorsDict["stripes22Shade"])
        imNew.putpixel((7, 20), colorsDict["stripes22"])
        imNew.putpixel((8, 20), colorsDict["stripes22"])
        imNew.putpixel((14, 20), colorsDict["stripes22"])

        imNew.putpixel((4, 22), colorsDict["stripes22Shade"])
        imNew.putpixel((5, 22), colorsDict["stripes22"])
        imNew.putpixel((6, 22), colorsDict["stripes22"])
        imNew.putpixel((7, 22), colorsDict["stripes22"])
        imNew.putpixel((8, 22), colorsDict["stripes22"])
        imNew.putpixel((9, 22), colorsDict["stripes22"])
        imNew.putpixel((10, 22), colorsDict["stripes22"])
        imNew.putpixel((11, 22), colorsDict["stripes22"])
        imNew.putpixel((12, 22), colorsDict["stripes22"])
        imNew.putpixel((13, 22), colorsDict["stripes22"])
        imNew.putpixel((14, 22), colorsDict["stripes22"])
    elif decodedBody == "Hawaiian":
        imNew.putpixel((7, 19), colorsDict["hawaiianShirtPurpleShade"])
        imNew.putpixel((8, 19), colorsDict["hawaiianShirtGreen"])

        imNew.putpixel((6, 20), colorsDict["hawaiianShirtShade"])
        imNew.putpixel((7, 20), colorsDict["hawaiianShirt"])
        imNew.putpixel((8, 20), colorsDict["hawaiianShirtPurple"])
        imNew.putpixel((9, 20), colorsDict["black"])
        imNew.putpixel((13, 20), colorsDict["black"])
        imNew.putpixel((14, 20), colorsDict["hawaiianShirt"])

        imNew.putpixel((5, 21), colorsDict["hawaiianShirtBlueShade"])
        imNew.putpixel((6, 21), colorsDict["hawaiianShirt"])
        imNew.putpixel((7, 21), colorsDict["hawaiianShirtBlue"])
        imNew.putpixel((8, 21), colorsDict["hawaiianShirt"])
        imNew.putpixel((9, 21), colorsDict["hawaiianShirt"])
        imNew.putpixel((10, 21), colorsDict["black"])
        imNew.putpixel((12, 21), colorsDict["black"])
        imNew.putpixel((13, 21), colorsDict["hawaiianShirtRed"])
        imNew.putpixel((14, 21), colorsDict["hawaiianShirt"])

        imNew.putpixel((4, 22), colorsDict["hawaiianShirtShade"])
        imNew.putpixel((5, 22), colorsDict["hawaiianShirt"])
        imNew.putpixel((6, 22), colorsDict["hawaiianShirtGreen"])
        imNew.putpixel((7, 22), colorsDict["hawaiianShirt"])
        imNew.putpixel((8, 22), colorsDict["hawaiianShirt"])
        imNew.putpixel((9, 22), colorsDict["hawaiianShirt"])
        imNew.putpixel((10, 22), colorsDict["hawaiianShirt"])
        imNew.putpixel((11, 22), colorsDict["black"])
        imNew.putpixel((12, 22), colorsDict["hawaiianShirtRed"])
        imNew.putpixel((13, 22), colorsDict["hawaiianShirtOrange"])
        imNew.putpixel((14, 22), colorsDict["hawaiianShirtRed"])

        imNew.putpixel((3, 23), colorsDict["hawaiianShirtShade"])
        imNew.putpixel((4, 23), colorsDict["hawaiianShirt"])
        imNew.putpixel((5, 23), colorsDict["hawaiianShirtBlue"])
        imNew.putpixel((6, 23), colorsDict["hawaiianShirt"])
        imNew.putpixel((7, 23), colorsDict["hawaiianShirtBlue"])
        imNew.putpixel((8, 23), colorsDict["hawaiianShirt"])
        imNew.putpixel((10, 23), colorsDict["hawaiianShirtShade"])
        imNew.putpixel((11, 23), colorsDict["hawaiianShirtShade"])
        imNew.putpixel((13, 23), colorsDict["hawaiianShirtRedShade"])
        imNew.putpixel((14, 23), colorsDict["hawaiianShirtShade"])
    elif decodedBody == "BathRobe":
        imNew.putpixel((7, 19), colorsDict["bathRobeShade"])
        imNew.putpixel((8, 19), colorsDict["bathRobeAccent"])

        imNew.putpixel((6, 20), colorsDict["bathRobeShade"])
        imNew.putpixel((7, 20), colorsDict["white"])
        imNew.putpixel((8, 20), colorsDict["white"])
        imNew.putpixel((9, 20), colorsDict["bathRobeAccent"])
        imNew.putpixel((13, 20), colorsDict["bathRobeAccent"])
        imNew.putpixel((14, 20), colorsDict["bathRobeAccent"])

        imNew.putpixel((5, 21), colorsDict["bathRobeAccent"])
        imNew.putpixel((6, 21), colorsDict["white"])
        imNew.putpixel((7, 21), colorsDict["white"])
        imNew.putpixel((8, 21), colorsDict["white"])
        imNew.putpixel((9, 21), colorsDict["white"])
        imNew.putpixel((10, 21), colorsDict["bathRobeAccent"])
        imNew.putpixel((12, 21), colorsDict["bathRobeAccent"])
        imNew.putpixel((13, 21), colorsDict["white"])
        imNew.putpixel((14, 21), colorsDict["white"])

        imNew.putpixel((4, 22), colorsDict["bathRobeShade"])
        imNew.putpixel((5, 22), colorsDict["white"])
        imNew.putpixel((6, 22), colorsDict["bathRobeAccent"])
        imNew.putpixel((7, 22), colorsDict["white"])
        imNew.putpixel((8, 22), colorsDict["white"])
        imNew.putpixel((9, 22), colorsDict["white"])
        imNew.putpixel((10, 22), colorsDict["white"])
        imNew.putpixel((11, 22), colorsDict["bathRobeAccent"])
        imNew.putpixel((12, 22), colorsDict["white"])
        imNew.putpixel((13, 22), colorsDict["white"])
        imNew.putpixel((14, 22), colorsDict["white"])

        imNew.putpixel((3, 23), colorsDict["bathRobeShade"])
        imNew.putpixel((4, 23), colorsDict["white"])
        imNew.putpixel((5, 23), colorsDict["white"])
        imNew.putpixel((6, 23), colorsDict["white"])
        imNew.putpixel((7, 23), colorsDict["bathRobeAccent"])
        imNew.putpixel((8, 23), colorsDict["white"])
        imNew.putpixel((10, 23), colorsDict["bathRobeShade"])
        imNew.putpixel((11, 23), colorsDict["bathRobeShade"])
        imNew.putpixel((13, 23), colorsDict["bathRobeShade"])
        imNew.putpixel((14, 23), colorsDict["bathRobeShade"])
    elif decodedBody == "VelvetRobe":
        imNew.putpixel((6, 19), colorsDict["black"])
        imNew.putpixel((7, 19), colorsDict["velvetRobeShade"])
        imNew.putpixel((8, 19), colorsDict["velvetRobeAccent"])

        imNew.putpixel((5, 20), colorsDict["black"])
        imNew.putpixel((6, 20), colorsDict["velvetRobeShade"])
        imNew.putpixel((7, 20), colorsDict["velvetRobe"])
        imNew.putpixel((8, 20), colorsDict["velvetRobe"])
        imNew.putpixel((9, 20), colorsDict["velvetRobeAccent"])
        imNew.putpixel((13, 20), colorsDict["velvetRobeAccent"])
        imNew.putpixel((14, 20), colorsDict["velvetRobeAccent"])
        imNew.putpixel((15, 20), colorsDict["black"])

        imNew.putpixel((4, 21), colorsDict["black"])
        imNew.putpixel((5, 21), colorsDict["velvetRobeBeltShade"])
        imNew.putpixel((6, 21), colorsDict["velvetRobe"])
        imNew.putpixel((7, 21), colorsDict["velvetRobe"])
        imNew.putpixel((8, 21), colorsDict["velvetRobe"])
        imNew.putpixel((9, 21), colorsDict["velvetRobe"])
        imNew.putpixel((10, 21), colorsDict["velvetRobeAccent"])
        imNew.putpixel((12, 21), colorsDict["velvetRobeAccent"])
        imNew.putpixel((13, 21), colorsDict["velvetRobe"])
        imNew.putpixel((14, 21), colorsDict["velvetRobe"])
        imNew.putpixel((15, 21), colorsDict["black"])

        imNew.putpixel((3, 22), colorsDict["black"])
        imNew.putpixel((4, 22), colorsDict["velvetRobeShade"])
        imNew.putpixel((5, 22), colorsDict["velvetRobe"])
        imNew.putpixel((6, 22), colorsDict["velvetRobeBelt"])
        imNew.putpixel((7, 22), colorsDict["velvetRobe"])
        imNew.putpixel((8, 22), colorsDict["velvetRobe"])
        imNew.putpixel((9, 22), colorsDict["velvetRobe"])
        imNew.putpixel((10, 22), colorsDict["velvetRobe"])
        imNew.putpixel((11, 22), colorsDict["velvetRobeAccent"])
        imNew.putpixel((12, 22), colorsDict["velvetRobe"])
        imNew.putpixel((13, 22), colorsDict["velvetRobe"])
        imNew.putpixel((14, 22), colorsDict["velvetRobe"])
        imNew.putpixel((15, 22), colorsDict["black"])

        imNew.putpixel((2, 23), colorsDict["black"])
        imNew.putpixel((3, 23), colorsDict["velvetRobeShade"])
        imNew.putpixel((4, 23), colorsDict["velvetRobe"])
        imNew.putpixel((5, 23), colorsDict["velvetRobe"])
        imNew.putpixel((6, 23), colorsDict["velvetRobe"])
        imNew.putpixel((7, 23), colorsDict["velvetRobeBelt"])
        imNew.putpixel((8, 23), colorsDict["velvetRobe"])
        imNew.putpixel((9, 23), colorsDict["black"])
        imNew.putpixel((10, 23), colorsDict["velvetRobeShade"])
        imNew.putpixel((11, 23), colorsDict["velvetRobeShade"])
        imNew.putpixel((12, 23), colorsDict["black"])
        imNew.putpixel((13, 23), colorsDict["velvetRobeShade"])
        imNew.putpixel((14, 23), colorsDict["velvetRobeShade"])
        imNew.putpixel((15, 23), colorsDict["black"])
    elif decodedBody == "Cope":
        drawShirt(im, "dark")

        imNew.putpixel((9, 22), colorsDict["white"])
        imNew.putpixel((11, 22), colorsDict["white"])
        imNew.putpixel((13, 22), colorsDict["white"])
    elif decodedBody == "StripedShirt":
        drawShirt(im, "stripes")
        imNew.putpixel((6, 20), colorsDict["stripes2Shade"])
        imNew.putpixel((7, 20), colorsDict["stripes2"])
        imNew.putpixel((8, 20), colorsDict["stripes2"])
        imNew.putpixel((14, 20), colorsDict["stripes2"])

        imNew.putpixel((4, 22), colorsDict["stripes2Shade"])
        imNew.putpixel((5, 22), colorsDict["stripes2"])
        imNew.putpixel((6, 22), colorsDict["stripes2"])
        imNew.putpixel((7, 22), colorsDict["stripes2"])
        imNew.putpixel((8, 22), colorsDict["stripes2"])
        imNew.putpixel((9, 22), colorsDict["stripes2"])
        imNew.putpixel((10, 22), colorsDict["stripes2"])
        imNew.putpixel((11, 22), colorsDict["stripes2"])
        imNew.putpixel((12, 22), colorsDict["stripes2"])
        imNew.putpixel((13, 22), colorsDict["stripes2"])
        imNew.putpixel((14, 22), colorsDict["stripes2"])
    elif decodedBody == "PolkaDots":
        drawShirt(im, "yellow")
        imNew.putpixel((8, 20), colorsDict["polkaDotSpot"])

        imNew.putpixel((6, 21), colorsDict["polkaDotSpot"])
        imNew.putpixel((13, 21), colorsDict["polkaDotSpot"])

        imNew.putpixel((8, 22), colorsDict["polkaDotSpot"])
        imNew.putpixel((10, 22), colorsDict["polkaDotSpot"])

        imNew.putpixel((5, 23), colorsDict["polkaDotSpot"])
        imNew.putpixel((14, 23), colorsDict["polkaDotSpot"])
    elif decodedBody == "LuckyShirt":
        drawShirt(im, "white")
        imNew.putpixel((6, 20), colorsDict["clover"])
        imNew.putpixel((8, 20), colorsDict["clover"])

        imNew.putpixel((5, 21), colorsDict["clover"])
        imNew.putpixel((6, 21), colorsDict["clover"])
        imNew.putpixel((7, 21), colorsDict["cloverSecondary"])
        imNew.putpixel((8, 21), colorsDict["clover"])
        imNew.putpixel((9, 21), colorsDict["clover"])

        imNew.putpixel((6, 22), colorsDict["cloverSecondary"])
        imNew.putpixel((7, 22), colorsDict["clover"])
        imNew.putpixel((8, 22), colorsDict["cloverSecondary"])

        imNew.putpixel((5, 23), colorsDict["clover"])
        imNew.putpixel((6, 23), colorsDict["clover"])
        imNew.putpixel((7, 23), colorsDict["cloverSecondary"])
        imNew.putpixel((8, 23), colorsDict["clover"])
        imNew.putpixel((9, 23), colorsDict["clover"])
    elif decodedBody == "AnimeShirt":
        drawShirt(im, "goku")
        imNew.putpixel((9, 20), colorsDict["gokuBlue"])
        imNew.putpixel((13, 20), colorsDict["gokuBlue"])
        imNew.putpixel((14, 20), colorsDict["gokuBlue"])
        imNew.putpixel((15, 20), colorsDict["black"])

        imNew.putpixel((10, 21), colorsDict["gokuBlue"])
        imNew.putpixel((11, 21), colorsDict["gokuBlue"])
        imNew.putpixel((12, 21), colorsDict["gokuBlue"])
        imNew.putpixel((13, 21), colorsDict["white"])

        imNew.putpixel((10, 23), colorsDict["gokuBlue"])
        imNew.putpixel((11, 23), colorsDict["gokuBlue"])
        imNew.putpixel((13, 23), colorsDict["gokuBlue"])
        imNew.putpixel((14, 23), colorsDict["gokuBlue"])
    elif decodedBody == "ViceShirt":
        drawShirt(im, "vice")
        imNew.putpixel((6, 20), colorsDict["viceFlower"])
        imNew.putpixel((8, 20), colorsDict["viceFlower"])

        imNew.putpixel((7, 21), colorsDict["viceFlower"])
        imNew.putpixel((14, 21), colorsDict["viceFlower"])

        imNew.putpixel((6, 22), colorsDict["viceFlower"])
        imNew.putpixel((8, 22), colorsDict["viceFlower"])
        imNew.putpixel((13, 22), colorsDict["viceFlower"])

        imNew.putpixel((14, 23), colorsDict["viceFlower"])
    elif decodedBody == "Diaper":
        imNew.putpixel((5, 20), colorsDict["black"])
        
        imNew.putpixel((4, 21), colorsDict["black"])
        imNew.putpixel((5, 21), colorsDict["white"])
        imNew.putpixel((6, 21), colorsDict["black"])
        imNew.putpixel((7, 21), colorsDict["black"])
    
        imNew.putpixel((3, 22), colorsDict["black"])
        imNew.putpixel((4, 22), colorsDict["whiteShade"])
        imNew.putpixel((5, 22), colorsDict["white"])
        imNew.putpixel((6, 22), colorsDict["white"])
        imNew.putpixel((7, 22), colorsDict["diaperStrap"])
        imNew.putpixel((8, 22), colorsDict["black"])

        imNew.putpixel((2, 23), colorsDict["black"])
        imNew.putpixel((3, 23), colorsDict["whiteShade"])
        imNew.putpixel((4, 23), colorsDict["white"])
        imNew.putpixel((5, 23), colorsDict["white"])
        imNew.putpixel((6, 23), colorsDict["white"])
        imNew.putpixel((7, 23), colorsDict["white"])
        imNew.putpixel((8, 23), colorsDict["white"])
        imNew.putpixel((9, 23), colorsDict["black"])
    elif decodedBody == "BlackSuit":
        primaryColor = colorsDict["blackSuit"]
        primaryColorShade = colorsDict["blackSuitShade"]
        tieColor = colorsDict["blackSuitTie"]
        drawSuit(imNew, primaryColor, primaryColorShade, tieColor)
    elif decodedBody == "NavySuit":
        primaryColor = colorsDict["navySuit"]
        primaryColorShade = colorsDict["navySuitShade"]
        tieColor = colorsDict["navySuitTie"]
        drawSuit(imNew, primaryColor, primaryColorShade, tieColor)
    elif decodedBody == "PurpleSuit":
        primaryColor = colorsDict["purpleSuit"]
        primaryColorShade = colorsDict["purpleSuitShade"]
        tieColor = colorsDict["purpleSuitTie"]
        drawSuit(imNew, primaryColor, primaryColorShade, tieColor)
    elif decodedBody == "NyanDoge":
        imNew.putpixel((0, 18), colorsDict["nyanDogeRed"])
        imNew.putpixel((1, 18), colorsDict["nyanDogeRed"])
        imNew.putpixel((2, 18), colorsDict["nyanDogeRed"])
        imNew.putpixel((3, 18), colorsDict["black"])
        imNew.putpixel((4, 18), colorsDict["black"])
        imNew.putpixel((5, 18), colorsDict["black"])
        imNew.putpixel((6, 18), colorsDict["black"])
        imNew.putpixel((7, 18), colorsDict["black"])
        imNew.putpixel((8, 18), colorsDict["black"])
        imNew.putpixel((15, 18), colorsDict["black"])
        imNew.putpixel((16, 18), colorsDict["black"])

        imNew.putpixel((0, 19), colorsDict["nyanDogeOrange"])
        imNew.putpixel((1, 19), colorsDict["nyanDogeOrange"])
        imNew.putpixel((2, 19), colorsDict["black"])
        imNew.putpixel((3, 19), colorsDict["nyanDogeEdge"])
        imNew.putpixel((4, 19), colorsDict["nyanDogeEdge"])
        imNew.putpixel((5, 19), colorsDict["nyanDogeEdge"])
        imNew.putpixel((6, 19), colorsDict["nyanDogeEdge"])
        imNew.putpixel((7, 19), colorsDict["nyanDogeEdge"])
        imNew.putpixel((8, 19), colorsDict["nyanDogeEdge"])
        imNew.putpixel((9, 19), colorsDict["black"])
        imNew.putpixel((10, 19), colorsDict["black"])
        imNew.putpixel((11, 19), colorsDict["black"])
        imNew.putpixel((12, 19), colorsDict["black"])
        imNew.putpixel((13, 19), colorsDict["black"])
        imNew.putpixel((14, 19), colorsDict["black"])
        imNew.putpixel((15, 19), colorsDict["nyanDogeEdge"])
        imNew.putpixel((16, 19), colorsDict["nyanDogeEdge"])
        imNew.putpixel((17, 19), colorsDict["black"])

        imNew.putpixel((0, 20), colorsDict["nyanDogeYellow"])
        imNew.putpixel((1, 20), colorsDict["black"])
        imNew.putpixel((2, 20), colorsDict["nyanDogeEdge"])
        imNew.putpixel((3, 20), colorsDict["nyanDogeEdge"])
        imNew.putpixel((4, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((5, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((6, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((7, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((8, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((9, 20), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((10, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((11, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((12, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((13, 20), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((14, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((15, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((16, 20), colorsDict["nyanDogeEdge"])
        imNew.putpixel((17, 20), colorsDict["nyanDogeEdge"])
        imNew.putpixel((18, 20), colorsDict["black"])

        imNew.putpixel((0, 21), colorsDict["nyanDogeGreen"])
        imNew.putpixel((1, 21), colorsDict["black"])
        imNew.putpixel((2, 21), colorsDict["nyanDogeEdge"])
        imNew.putpixel((3, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((4, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((5, 21), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((6, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((7, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((8, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((9, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((10, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((11, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((12, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((13, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((14, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((15, 21), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((16, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((17, 21), colorsDict["nyanDogeEdge"])
        imNew.putpixel((18, 21), colorsDict["black"])

        imNew.putpixel((0, 22), colorsDict["nyanDogeBlue"])
        imNew.putpixel((1, 22), colorsDict["black"])
        imNew.putpixel((2, 22), colorsDict["nyanDogeEdge"])
        imNew.putpixel((3, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((4, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((5, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((6, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((7, 22), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((8, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((9, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((10, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((11, 22), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((12, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((13, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((14, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((15, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((16, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((17, 22), colorsDict["nyanDogeEdge"])
        imNew.putpixel((18, 22), colorsDict["black"])

        imNew.putpixel((0, 23), colorsDict["nyanDogePurple"])
        imNew.putpixel((1, 23), colorsDict["black"])
        imNew.putpixel((2, 23), colorsDict["nyanDogeEdge"])
        imNew.putpixel((3, 23), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((4, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((5, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((6, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((7, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((8, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((9, 23), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((10, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((11, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((12, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((13, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((14, 23), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((15, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((16, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((17, 23), colorsDict["nyanDogeEdge"])
        imNew.putpixel((18, 23), colorsDict["black"])
    elif decodedBody == "BlueCollar":
        imNew.putpixel((7, 19), colorsDict["blueShade"])
        imNew.putpixel((8, 19), colorsDict["blue"])

        imNew.putpixel((9, 20), colorsDict["blue"])
        imNew.putpixel((10, 20), colorsDict["blue"])
        imNew.putpixel((11, 20), colorsDict["buckleSilver"])
        imNew.putpixel((12, 20), colorsDict["blue"])
        imNew.putpixel((13, 20), colorsDict["blue"])
        imNew.putpixel((14, 20), colorsDict["blue"])
    elif decodedBody == "GoldenCollar":
        # imNew.putpixel((7, 19), colorsDict["goldDogtagsShade"])
        # imNew.putpixel((8, 19), colorsDict["goldDogtags"])

        # imNew.putpixel((9, 20), colorsDict["goldDogtags"])
        imNew.putpixel((10, 20), colorsDict["goldDogtagsShade"])
        imNew.putpixel((11, 20), colorsDict["goldDogtags"])
        imNew.putpixel((12, 20), colorsDict["goldDogtagsShade"])
        # imNew.putpixel((13, 20), colorsDict["goldDogtags"])
        # imNew.putpixel((14, 20), colorsDict["goldDogtags"])
    elif decodedBody == "RastaCollar":
        # imNew.putpixel((7, 19), colorsDict["bronzeDogtagsShade"])
        # imNew.putpixel((8, 19), colorsDict["bronzeDogtagsShade"])

        # imNew.putpixel((9, 20), colorsDict["bronzeDogtagsShade"])
        imNew.putpixel((10, 20), colorsDict["redDogtags"])
        imNew.putpixel((11, 20), colorsDict["yellowDogtags"])
        imNew.putpixel((12, 20), colorsDict["greenDogtags"])
        # imNew.putpixel((13, 20), colorsDict["bronzeDogtagsShade"])
        # imNew.putpixel((14, 20), colorsDict["bronzeDogtagsShade"])
    elif decodedBody == "FreedomCollar":
        imNew.putpixel((10, 20), colorsDict["redDogtags"])
        imNew.putpixel((11, 20), colorsDict["white"])
        imNew.putpixel((12, 20), colorsDict["blueDogtags"])
    elif decodedBody == "SilverCollar":
        imNew.putpixel((10, 20), colorsDict["silverDogtagsShade"])
        imNew.putpixel((11, 20), colorsDict["silverDogtags"])
        imNew.putpixel((12, 20), colorsDict["silverDogtagsShade"])
    elif decodedBody == "LeatherCollar":
        imNew.putpixel((10, 20), colorsDict["bronzeDogtags"])
        imNew.putpixel((11, 20), colorsDict["silverDogtagsShade"])
        imNew.putpixel((12, 20), colorsDict["bronzeDogtags"])

    elif decodedBody == "RedCollar":
        imNew.putpixel((7, 19), colorsDict["redCollarShade"])
        imNew.putpixel((8, 19), colorsDict["redCollar"])

        imNew.putpixel((9, 20), colorsDict["redCollar"])
        imNew.putpixel((10, 20), colorsDict["redCollar"])
        imNew.putpixel((11, 20), colorsDict["buckleSilver"])
        imNew.putpixel((12, 20), colorsDict["redCollar"])
        imNew.putpixel((13, 20), colorsDict["redCollar"])
        imNew.putpixel((14, 20), colorsDict["redCollar"])
    elif decodedBody == "PinkCollar":
        imNew.putpixel((7, 19), colorsDict["pinkCollarShade"])
        imNew.putpixel((8, 19), colorsDict["pinkCollar"])

        imNew.putpixel((9, 20), colorsDict["pinkCollar"])
        imNew.putpixel((10, 20), colorsDict["pinkCollar"])
        imNew.putpixel((11, 20), colorsDict["buckleSilver"])
        imNew.putpixel((12, 20), colorsDict["pinkCollar"])
        imNew.putpixel((13, 20), colorsDict["pinkCollar"])
        imNew.putpixel((14, 20), colorsDict["pinkCollar"])
    elif decodedBody == "GreenCollar":
        imNew.putpixel((7, 19), colorsDict["greenCollarShade"])
        imNew.putpixel((8, 19), colorsDict["greenCollar"])

        imNew.putpixel((9, 20), colorsDict["greenCollar"])
        imNew.putpixel((10, 20), colorsDict["greenCollar"])
        imNew.putpixel((11, 20), colorsDict["buckleSilver"])
        imNew.putpixel((12, 20), colorsDict["greenCollar"])
        imNew.putpixel((13, 20), colorsDict["greenCollar"])
        imNew.putpixel((14, 20), colorsDict["greenCollar"])
    elif decodedBody == "PurpleCollar":
        imNew.putpixel((7, 19), colorsDict["purpleCollarShade"])
        imNew.putpixel((8, 19), colorsDict["purpleCollar"])

        imNew.putpixel((9, 20), colorsDict["purpleCollar"])
        imNew.putpixel((10, 20), colorsDict["purpleCollar"])
        imNew.putpixel((11, 20), colorsDict["buckleSilver"])
        imNew.putpixel((12, 20), colorsDict["purpleCollar"])
        imNew.putpixel((13, 20), colorsDict["purpleCollar"])
        imNew.putpixel((14, 20), colorsDict["purpleCollar"])

    elif decodedBody == "PurpleBowtie":
        drawBowtie(imNew, "purpleBowtie", "purpleBowtieBlue")
    elif decodedBody == "GreenBowtie":
        drawBowtie(imNew, "greenBowtie", "greenBowtieShade")
    elif decodedBody == "YellowBowtie":
        drawBowtie(imNew, "yellowBowtie", "yellowBowtieShade")
    elif decodedBody == "OrangeBowtie":
        drawBowtie(imNew, "orangeBowtie", "orangeBowtieShade")
    elif decodedBody == "EmeraldNecklace":
        imNew.putpixel((8, 19), colorsDict["newNecklaceShade"])

        imNew.putpixel((8, 20), colorsDict["newNecklace"])
        imNew.putpixel((9, 20), colorsDict["newNecklaceLight"])
        imNew.putpixel((11, 20), colorsDict["newEmeraldShade"])
        imNew.putpixel((13, 20), colorsDict["newNecklaceLight"])
        imNew.putpixel((14, 20), colorsDict["newNecklace"])

        imNew.putpixel((9, 21), colorsDict["newNecklace"])
        imNew.putpixel((10, 21), colorsDict["newEmeraldShade"])
        imNew.putpixel((11, 21), colorsDict["newEmeraldLight"])
        imNew.putpixel((12, 21), colorsDict["newEmerald"])
        imNew.putpixel((13, 21), colorsDict["newNecklace"])

        imNew.putpixel((11, 22), colorsDict["newEmerald"])
    elif decodedBody == "SapphireNecklace":
        imNew.putpixel((8, 19), colorsDict["newNecklaceShade"])

        imNew.putpixel((8, 20), colorsDict["newNecklace"])
        imNew.putpixel((9, 20), colorsDict["newNecklaceLight"])
        imNew.putpixel((11, 20), colorsDict["newSapphireShade"])
        imNew.putpixel((13, 20), colorsDict["newNecklaceLight"])
        imNew.putpixel((14, 20), colorsDict["newNecklace"])

        imNew.putpixel((9, 21), colorsDict["newNecklace"])
        imNew.putpixel((10, 21), colorsDict["newSapphireShade"])
        imNew.putpixel((11, 21), colorsDict["newSapphireLight"])
        imNew.putpixel((12, 21), colorsDict["newSapphire"])
        imNew.putpixel((13, 21), colorsDict["newNecklace"])

        imNew.putpixel((11, 22), colorsDict["newSapphire"])
    elif decodedBody == "RubyNecklace":
        imNew.putpixel((8, 19), colorsDict["newNecklaceShade"])

        imNew.putpixel((8, 20), colorsDict["newNecklace"])
        imNew.putpixel((9, 20), colorsDict["newNecklaceLight"])
        imNew.putpixel((11, 20), colorsDict["newRubyShade"])
        imNew.putpixel((13, 20), colorsDict["newNecklaceLight"])
        imNew.putpixel((14, 20), colorsDict["newNecklace"])

        imNew.putpixel((9, 21), colorsDict["newNecklace"])
        imNew.putpixel((10, 21), colorsDict["newRubyShade"])
        imNew.putpixel((11, 21), colorsDict["newRubyLight"])
        imNew.putpixel((12, 21), colorsDict["newRuby"])
        imNew.putpixel((13, 21), colorsDict["newNecklace"])

        imNew.putpixel((11, 22), colorsDict["newRuby"])
    elif decodedBody == "DiamondNecklace":
        imNew.putpixel((8, 19), colorsDict["newNecklaceShade"])

        imNew.putpixel((8, 20), colorsDict["newNecklace"])
        imNew.putpixel((9, 20), colorsDict["newNecklaceLight"])
        imNew.putpixel((11, 20), colorsDict["newDiamondShade"])
        imNew.putpixel((13, 20), colorsDict["newNecklaceLight"])
        imNew.putpixel((14, 20), colorsDict["newNecklace"])

        imNew.putpixel((9, 21), colorsDict["newNecklace"])
        imNew.putpixel((10, 21), colorsDict["newDiamondShade"])
        imNew.putpixel((11, 21), colorsDict["newDiamondLight"])
        imNew.putpixel((12, 21), colorsDict["newDiamond"])
        imNew.putpixel((13, 21), colorsDict["newNecklace"])

        imNew.putpixel((11, 22), colorsDict["newDiamond"])
    elif decodedBody == "RedScarf":
        primaryColor = "scarfRed"
        primaryColorShade = "scarfRedShade"
        drawScarf(imNew, primaryColor, primaryColorShade)
    elif decodedBody == "GreenScarf":
        primaryColor = "scarfGreen"
        primaryColorShade = "scarfGreenShade"
        drawScarf(imNew, primaryColor, primaryColorShade)
    elif decodedBody == "Cape":
        imNew.putpixel((0, 15), colorsDict["black"])
        imNew.putpixel((1, 15), colorsDict["black"])

        imNew.putpixel((0, 16), colorsDict["capeShade"])
        imNew.putpixel((1, 16), colorsDict["capeShade"])
        imNew.putpixel((2, 16), colorsDict["black"])
        imNew.putpixel((3, 16), colorsDict["black"])

        imNew.putpixel((0, 17), colorsDict["cape"])
        imNew.putpixel((1, 17), colorsDict["cape"])
        imNew.putpixel((2, 17), colorsDict["capeShade"])
        imNew.putpixel((3, 17), colorsDict["black"])
        imNew.putpixel((4, 17), colorsDict["black"])

        imNew.putpixel((0, 18), colorsDict["cape"])
        imNew.putpixel((1, 18), colorsDict["cape"])
        imNew.putpixel((2, 18), colorsDict["cape"])
        imNew.putpixel((3, 18), colorsDict["capeShade"])
        imNew.putpixel((4, 18), colorsDict["capeShade"])
        imNew.putpixel((5, 18), colorsDict["black"])

        imNew.putpixel((0, 19), colorsDict["cape"])
        imNew.putpixel((1, 19), colorsDict["cape"])
        imNew.putpixel((2, 19), colorsDict["cape"])
        imNew.putpixel((3, 19), colorsDict["cape"])
        imNew.putpixel((4, 19), colorsDict["cape"])
        imNew.putpixel((5, 19), colorsDict["capeShade"])
        imNew.putpixel((6, 19), colorsDict["black"])
        imNew.putpixel((7, 19), colorsDict["capeShade"])
        imNew.putpixel((8, 19), colorsDict["capeShade"])
        imNew.putpixel((9, 19), colorsDict["cape"])
        imNew.putpixel((10, 19), colorsDict["black"])
        imNew.putpixel((11, 19), colorsDict["black"])
        imNew.putpixel((12, 19), colorsDict["black"])
        imNew.putpixel((13, 19), colorsDict["black"])

        imNew.putpixel((0, 20), colorsDict["cape"])
        imNew.putpixel((1, 20), colorsDict["cape"])
        imNew.putpixel((2, 20), colorsDict["cape"])
        imNew.putpixel((3, 20), colorsDict["black"])
        imNew.putpixel((4, 20), colorsDict["cape"])
        imNew.putpixel((5, 20), colorsDict["cape"])
        imNew.putpixel((6, 20), colorsDict["cape"])
        imNew.putpixel((7, 20), colorsDict["capeShade"])
        imNew.putpixel((8, 20), colorsDict["black"])
        imNew.putpixel((9, 20), colorsDict["black"])
        imNew.putpixel((10, 20), colorsDict["cape"])
        imNew.putpixel((11, 20), colorsDict["cape"])
        imNew.putpixel((12, 20), colorsDict["cape"])
        imNew.putpixel((13, 20), colorsDict["capeShade"])
        imNew.putpixel((14, 20), colorsDict["black"])

        imNew.putpixel((0, 21), colorsDict["capeShade"])
        imNew.putpixel((1, 21), colorsDict["black"])
        imNew.putpixel((2, 21), colorsDict["black"])
        imNew.putpixel((4, 21), colorsDict["black"])
        imNew.putpixel((5, 21), colorsDict["black"])
        imNew.putpixel((6, 21), colorsDict["black"])
        imNew.putpixel((7, 21), colorsDict["black"])
        imNew.putpixel((10, 21), colorsDict["black"])
        imNew.putpixel((11, 21), colorsDict["black"])
        imNew.putpixel((12, 21), colorsDict["black"])
        imNew.putpixel((13, 21), colorsDict["black"])

        imNew.putpixel((0, 22), colorsDict["black"])

    im.paste(imNew, (0,0), mask=imNew)
