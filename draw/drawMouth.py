from PIL import Image
from colors import colorsDict, backgroundLookup
from traitEncodings import TRAIT_ENCODINGS

typesWithoutHighEyes = ["s", "z", "a"]

def drawMouth(im, trait, typeEncoding, backgroundColor):
    imNew = Image.new('RGBA', (32, 32), (0, 0, 0, 0))

    decodedType = TRAIT_ENCODINGS["mouth"][trait]
    if decodedType == "Bubblegum":

        imNew.putpixel((18, 18), colorsDict["bubblegumOutline"])
        imNew.putpixel((19, 18), colorsDict["bubblegumOutline"])
        imNew.putpixel((20, 18), colorsDict["bubblegumOutline"])

        imNew.putpixel((17, 19), colorsDict["bubblegumOutline"])
        imNew.putpixel((18, 19), colorsDict["bubblegum"])
        imNew.putpixel((19, 19), colorsDict["bubblegum"])
        imNew.putpixel((20, 19), colorsDict["bubblegum"])
        imNew.putpixel((21, 19), colorsDict["bubblegumOutline"])

        imNew.putpixel((16, 20), colorsDict["bubblegumOutline"])
        imNew.putpixel((17, 20), colorsDict["bubblegum"])
        imNew.putpixel((18, 20), colorsDict["white"])
        imNew.putpixel((19, 20), colorsDict["bubblegum"])
        imNew.putpixel((20, 20), colorsDict["bubblegum"])
        imNew.putpixel((21, 20), colorsDict["bubblegum"])
        imNew.putpixel((22, 20), colorsDict["bubblegumOutline"])

        imNew.putpixel((16, 21), colorsDict["bubblegumOutline"])
        imNew.putpixel((17, 21), colorsDict["white"])
        imNew.putpixel((18, 21), colorsDict["bubblegum"])
        imNew.putpixel((19, 21), colorsDict["bubblegum"])
        imNew.putpixel((20, 21), colorsDict["bubblegum"])
        imNew.putpixel((21, 21), colorsDict["bubblegum"])
        imNew.putpixel((22, 21), colorsDict["bubblegumOutline"])

        imNew.putpixel((16, 22), colorsDict["bubblegumOutline"])
        imNew.putpixel((17, 22), colorsDict["bubblegum"])
        imNew.putpixel((18, 22), colorsDict["bubblegum"])
        imNew.putpixel((19, 22), colorsDict["bubblegum"])
        imNew.putpixel((20, 22), colorsDict["white"])
        imNew.putpixel((21, 22), colorsDict["bubblegum"])
        imNew.putpixel((22, 22), colorsDict["bubblegumOutline"])

        imNew.putpixel((17, 23), colorsDict["bubblegumOutline"])
        imNew.putpixel((18, 23), colorsDict["bubblegum"])
        imNew.putpixel((19, 23), colorsDict["bubblegum"])
        imNew.putpixel((20, 23), colorsDict["bubblegum"])
        imNew.putpixel((21, 23), colorsDict["bubblegumOutline"])

        imNew.putpixel((18, 24), colorsDict["bubblegumOutline"])
        imNew.putpixel((19, 24), colorsDict["bubblegumOutline"])
        imNew.putpixel((20, 24), colorsDict["bubblegumOutline"])

    elif decodedType == "Booger":
        imNew.putpixel((12, 15), colorsDict["booger"])
    elif decodedType == "Drool":
        imNew.putpixel((10, 17), colorsDict["drool"])
        imNew.putpixel((10, 19), colorsDict["drool"])
    elif decodedType == "ClownNose":
        imNew.putpixel((11, 14), colorsDict["clownNose"])
        imNew.putpixel((11, 15), colorsDict["clownNose"])
        imNew.putpixel((12, 14), colorsDict["clownNose"])
        imNew.putpixel((12, 15), colorsDict["clownNose"])
    elif decodedType == "Bacon":
        imNew.putpixel((11, 16), colorsDict["baconOuter"])
        imNew.putpixel((12, 16), colorsDict["baconOuter"])
        imNew.putpixel((15, 16), colorsDict["baconOuter"])
        imNew.putpixel((16, 16), colorsDict["baconOuter"])
        imNew.putpixel((17, 16), colorsDict["baconOuter"])
        imNew.putpixel((20, 16), colorsDict["baconOuter"])

        imNew.putpixel((11, 17), colorsDict["baconInner"])
        imNew.putpixel((12, 17), colorsDict["baconInner"])
        imNew.putpixel((13, 17), colorsDict["baconOuter"])
        imNew.putpixel((14, 17), colorsDict["baconOuter"])
        imNew.putpixel((15, 17), colorsDict["baconInner"])
        imNew.putpixel((16, 17), colorsDict["baconInner"])
        imNew.putpixel((17, 17), colorsDict["baconInner"])
        imNew.putpixel((18, 17), colorsDict["baconOuter"])
        imNew.putpixel((19, 17), colorsDict["baconOuter"])
        imNew.putpixel((20, 17), colorsDict["baconInner"])

        imNew.putpixel((11, 18), colorsDict["baconOuter"])
        imNew.putpixel((12, 18), colorsDict["baconOuter"])
        imNew.putpixel((13, 18), colorsDict["baconInner"])
        imNew.putpixel((14, 18), colorsDict["baconInner"])
        imNew.putpixel((15, 18), colorsDict["baconOuter"])
        imNew.putpixel((16, 18), colorsDict["baconOuter"])
        imNew.putpixel((17, 18), colorsDict["baconOuter"])
        imNew.putpixel((18, 18), colorsDict["baconInner"])
        imNew.putpixel((19, 18), colorsDict["baconInner"])
        imNew.putpixel((20, 18), colorsDict["baconOuter"])

        imNew.putpixel((13, 19), colorsDict["baconOuter"])
        imNew.putpixel((14, 19), colorsDict["baconOuter"])
        imNew.putpixel((18, 19), colorsDict["baconOuter"])
        imNew.putpixel((19, 19), colorsDict["baconOuter"])
    elif decodedType == "Cigarette":
        imNew.putpixel((28, 14), colorsDict["pipeSmoke"])
        imNew.putpixel((27, 15), colorsDict["pipeSmoke"])
        imNew.putpixel((28, 16), colorsDict["pipeSmoke"])
        imNew.putpixel((27, 17), colorsDict["pipeSmoke"])

        imNew.putpixel((17, 19), colorsDict["cigaretteYellow"])
        imNew.putpixel((18, 19), colorsDict["cigaretteYellow"])
        imNew.putpixel((19, 19), colorsDict["cigaretteYellow"])
        imNew.putpixel((20, 19), colorsDict["cigarette"])
        imNew.putpixel((21, 19), colorsDict["cigarette"])
        imNew.putpixel((22, 19), colorsDict["cigarette"])
        imNew.putpixel((23, 19), colorsDict["cigarette"])
        imNew.putpixel((24, 19), colorsDict["cigarette"])
        imNew.putpixel((25, 19), colorsDict["cigarette"])
        imNew.putpixel((26, 19), colorsDict["cigaretteOrange"])
    elif decodedType == "Twig":
        imNew.putpixel((21, 14), colorsDict["twigLeaf1"])

        imNew.putpixel((14, 15), colorsDict["twig"])
        imNew.putpixel((15, 15), colorsDict["twig"])
        imNew.putpixel((19, 15), colorsDict["twig"])
        imNew.putpixel((20, 15), colorsDict["twig"])

        imNew.putpixel((11, 16), colorsDict["twig"])
        imNew.putpixel((12, 16), colorsDict["twig"])
        imNew.putpixel((13, 16), colorsDict["twig"])
        imNew.putpixel((16, 16), colorsDict["twig"])
        imNew.putpixel((17, 16), colorsDict["twig"])
        imNew.putpixel((18, 16), colorsDict["twig"])
        imNew.putpixel((21, 16), colorsDict["twig"])

        imNew.putpixel((17, 17), colorsDict["twigLeaf1"])
        imNew.putpixel((20, 17), colorsDict["twigLeaf2"])
        imNew.putpixel((22, 17), colorsDict["twigLeaf1"])

    # elif decodedType == "Cookie":
    #     imNew.putpixel((13, 14), colorsDict["cookieOutline"])
    #     imNew.putpixel((14, 14), colorsDict["cookieOutline"])
    #     imNew.putpixel((15, 14), colorsDict["cookieOutline"])


    #     imNew.putpixel((16, 17), colorsDict["twigLeaf1"])
    elif decodedType == "Cookie":
        imNew.putpixel((18, 18), colorsDict["cookieOutline"])
        imNew.putpixel((19, 18), colorsDict["cookieOutline"])
        imNew.putpixel((20, 18), colorsDict["cookieOutline"])

        imNew.putpixel((17, 19), colorsDict["cookieOutline"])
        imNew.putpixel((18, 19), colorsDict["cookie"])
        imNew.putpixel((19, 19), colorsDict["cookieChip"])
        imNew.putpixel((20, 19), colorsDict["cookie"])
        imNew.putpixel((21, 19), colorsDict["cookieOutline"])

        imNew.putpixel((16, 20), colorsDict["cookieOutline"])
        imNew.putpixel((17, 20), colorsDict["cookie"])
        imNew.putpixel((18, 20), colorsDict["cookie"])
        imNew.putpixel((19, 20), colorsDict["cookie"])
        imNew.putpixel((20, 20), colorsDict["cookie"])
        imNew.putpixel((21, 20), colorsDict["cookie"])
        imNew.putpixel((22, 20), colorsDict["cookieOutline"])

        imNew.putpixel((16, 21), colorsDict["cookieOutline"])
        imNew.putpixel((17, 21), colorsDict["cookieChip"])
        imNew.putpixel((18, 21), colorsDict["cookie"])
        imNew.putpixel((19, 21), colorsDict["cookieChip"])
        imNew.putpixel((20, 21), colorsDict["cookie"])
        imNew.putpixel((21, 21), colorsDict["cookie"])
        imNew.putpixel((22, 21), colorsDict["cookieOutline"])

        imNew.putpixel((16, 22), colorsDict["cookieOutline"])
        imNew.putpixel((17, 22), colorsDict["cookie"])
        imNew.putpixel((18, 22), colorsDict["cookie"])
        imNew.putpixel((19, 22), colorsDict["cookie"])
        imNew.putpixel((20, 22), colorsDict["cookie"])
        imNew.putpixel((21, 22), colorsDict["cookieChip"])
        imNew.putpixel((22, 22), colorsDict["cookieOutline"])

        imNew.putpixel((17, 23), colorsDict["cookieOutline"])
        imNew.putpixel((18, 23), colorsDict["cookieChip"])
        imNew.putpixel((19, 23), colorsDict["cookie"])
        imNew.putpixel((20, 23), colorsDict["cookie"])
        imNew.putpixel((21, 23), colorsDict["cookieOutline"])

        imNew.putpixel((18, 24), colorsDict["cookieOutline"])
        imNew.putpixel((19, 24), colorsDict["cookieOutline"])
        imNew.putpixel((20, 24), colorsDict["cookieOutline"])
    elif decodedType == "Ball":
        imNew.putpixel((13, 14), colorsDict["ballOutline"])
        imNew.putpixel((14, 14), colorsDict["ballOutline"])
        imNew.putpixel((15, 14), colorsDict["ballOutline"])

        imNew.putpixel((12, 15), colorsDict["ballOutline"])
        imNew.putpixel((13, 15), colorsDict["ball"])
        imNew.putpixel((14, 15), colorsDict["ball"])
        imNew.putpixel((15, 15), colorsDict["ballShine"])
        imNew.putpixel((16, 15), colorsDict["ballOutline"])

        imNew.putpixel((11, 16), colorsDict["ballOutline"])
        imNew.putpixel((12, 16), colorsDict["ball"])
        imNew.putpixel((13, 16), colorsDict["ball"])
        imNew.putpixel((14, 16), colorsDict["ball"])
        imNew.putpixel((15, 16), colorsDict["ball"])
        imNew.putpixel((16, 16), colorsDict["ballShine"])
        imNew.putpixel((17, 16), colorsDict["ballOutline"])

        imNew.putpixel((11, 17), colorsDict["ballOutline"])
        imNew.putpixel((12, 17), colorsDict["ball"])
        imNew.putpixel((13, 17), colorsDict["ball"])
        imNew.putpixel((14, 17), colorsDict["ballNotch"])
        imNew.putpixel((15, 17), colorsDict["ball"])
        imNew.putpixel((16, 17), colorsDict["ball"])
        imNew.putpixel((17, 17), colorsDict["ballOutline"])

        imNew.putpixel((11, 18), colorsDict["ballOutline"])
        imNew.putpixel((12, 18), colorsDict["white"])
        imNew.putpixel((13, 18), colorsDict["white"])
        imNew.putpixel((14, 18), colorsDict["white"])
        imNew.putpixel((15, 18), colorsDict["white"])
        imNew.putpixel((16, 18), colorsDict["white"])
        imNew.putpixel((17, 18), colorsDict["ballOutline"])

        imNew.putpixel((12, 19), colorsDict["ballOutline"])
        imNew.putpixel((13, 19), colorsDict["white"])
        imNew.putpixel((14, 19), colorsDict["white"])
        imNew.putpixel((15, 19), colorsDict["white"])
        imNew.putpixel((16, 19), colorsDict["ballOutline"])

        imNew.putpixel((13, 20), colorsDict["ballOutline"])
        imNew.putpixel((14, 20), colorsDict["ballOutline"])
        imNew.putpixel((15, 20), colorsDict["ballOutline"])

    elif decodedType == "BeerBottle":
        imNew.putpixel((21, 17), colorsDict["beerBottle"])
        imNew.putpixel((22, 17), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((23, 17), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((24, 17), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((25, 17), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((26, 17), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((27, 17), colorsDict["beerBottle"])

        imNew.putpixel((17, 18), colorsDict["beerBottleTop"])
        imNew.putpixel((18, 18), colorsDict["beerBottleTop"])
        imNew.putpixel((19, 18), colorsDict["beerBottle"])
        imNew.putpixel((20, 18), colorsDict["beerBottle"])
        imNew.putpixel((21, 18), colorsDict["beerBottle"])
        imNew.putpixel((22, 18), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((23, 18), colorsDict["beerBottleLabelRed"])
        imNew.putpixel((24, 18), colorsDict["beerBottleLabelGray"])
        imNew.putpixel((25, 18), colorsDict["beerBottleLabelRed"])
        imNew.putpixel((26, 18), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((27, 18), colorsDict["beerBottle"])

        imNew.putpixel((16, 19), colorsDict["beer"])
        imNew.putpixel((17, 19), colorsDict["beerBottleTop"])
        imNew.putpixel((18, 19), colorsDict["beerBottleTop"])
        imNew.putpixel((19, 19), colorsDict["beerBottleShade"])
        imNew.putpixel((20, 19), colorsDict["beerBottleShade"])
        imNew.putpixel((21, 19), colorsDict["beerBottleShade"])
        imNew.putpixel((22, 19), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((23, 19), colorsDict["beerBottleLabelRed"])
        imNew.putpixel((24, 19), colorsDict["beerBottleLabelGray"])
        imNew.putpixel((25, 19), colorsDict["beerBottleLabelRed"])
        imNew.putpixel((26, 19), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((27, 19), colorsDict["beerBottleShade"])

        imNew.putpixel((21, 20), colorsDict["beerBottleShade"])
        imNew.putpixel((22, 20), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((23, 20), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((24, 20), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((25, 20), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((26, 20), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((27, 20), colorsDict["beerBottleShade"])
    elif decodedType == "Smile":
        decodedTypeForPrimary = TRAIT_ENCODINGS["type"][typeEncoding]
        if decodedTypeForPrimary == "Green":
            primaryColor = colorsDict["blobGreen"]
        if decodedTypeForPrimary == "Rose":
            primaryColor = colorsDict["blobRose"]
        if decodedTypeForPrimary == "Yellow":
            primaryColor = colorsDict["blobYellow"]
        if decodedTypeForPrimary == "Blue":
            primaryColor = colorsDict["blobBlue"]
        if decodedTypeForPrimary == "Purple":
            primaryColor = colorsDict["blobPurple"]
        if decodedTypeForPrimary == "Orange":
            primaryColor = colorsDict["blobOrange"]
        if decodedTypeForPrimary == "Black":
            primaryColor = colorsDict["typeBlack"]
        if decodedTypeForPrimary == "Zombie":
            primaryColor = colorsDict["typeZombie"]
        if decodedTypeForPrimary == "Alien":
            primaryColor = colorsDict["typeAlien"]
        if decodedTypeForPrimary == "Devil":
            primaryColor = colorsDict["typeDevil"]
        if decodedTypeForPrimary == "Clear":
            primaryColor = colorsDict["blobClear"]
        if decodedTypeForPrimary == "Rainbow":
            primaryColor = colorsDict["blobGreen"]
        imNew.putpixel((14, 19), colorsDict["black"])
        imNew.putpixel((15, 19), primaryColor)
        imNew.putpixel((16, 19), primaryColor)
        imNew.putpixel((17, 19), colorsDict["black"])

        imNew.putpixel((15, 20), colorsDict["black"])
        imNew.putpixel((16, 20), colorsDict["black"])
    elif decodedType == "Rose":
        imNew.putpixel((21, 17), colorsDict["roseOutline"])
        imNew.putpixel((22, 17), colorsDict["roseOutline"])
        imNew.putpixel((23, 17), colorsDict["roseOutline"])

        imNew.putpixel((20, 18), colorsDict["roseOutline"])
        imNew.putpixel((21, 18), colorsDict["roseOutline"])
        imNew.putpixel((22, 18), colorsDict["rose"])
        imNew.putpixel((23, 18), colorsDict["roseLight"])

        imNew.putpixel((12, 19), colorsDict["roseStem"])
        imNew.putpixel((13, 19), colorsDict["roseStem"])
        imNew.putpixel((14, 19), colorsDict["roseStem"])
        imNew.putpixel((15, 19), colorsDict["roseMouth"])
        imNew.putpixel((16, 19), colorsDict["roseMouth"])
        imNew.putpixel((17, 19), colorsDict["roseStem"])
        imNew.putpixel((18, 19), colorsDict["roseStem"])
        imNew.putpixel((19, 19), colorsDict["roseStem"])
        imNew.putpixel((20, 19), colorsDict["roseOutline"])
        imNew.putpixel((21, 19), colorsDict["rose"])
        imNew.putpixel((22, 19), colorsDict["roseLight"])
        imNew.putpixel((23, 19), colorsDict["rose"])

        imNew.putpixel((20, 20), colorsDict["roseOutline"])
        imNew.putpixel((21, 20), colorsDict["roseOutline"])
        imNew.putpixel((22, 20), colorsDict["rose"])
        imNew.putpixel((23, 20), colorsDict["roseLight"])

        imNew.putpixel((21, 21), colorsDict["roseOutline"])
        imNew.putpixel((22, 21), colorsDict["roseOutline"])
        imNew.putpixel((23, 21), colorsDict["roseOutline"])
    elif decodedType == "Blushing":
        imNew.putpixel((7, 15), colorsDict["blushing"])
        imNew.putpixel((16, 15), colorsDict["blushing"])
    elif decodedType == "Surprised":
        imNew.putpixel((9, 15), colorsDict["white"])
        imNew.putpixel((14, 15), colorsDict["white"])
    elif decodedType == "Kazoo":
        imNew.putpixel((16, 15), colorsDict["kazooWhistle"])
        imNew.putpixel((17, 15), colorsDict["kazooWhistle"])

        imNew.putpixel((11, 16), colorsDict["kazooTop"])
        imNew.putpixel((12, 16), colorsDict["kazooTop"])
        imNew.putpixel((13, 16), colorsDict["kazooTop"])
        imNew.putpixel((14, 16), colorsDict["kazooTop"])
        imNew.putpixel((15, 16), colorsDict["kazooTop"])
        imNew.putpixel((16, 16), colorsDict["kazooTop"])
        imNew.putpixel((17, 16), colorsDict["kazooTop"])

        imNew.putpixel((13, 17), colorsDict["kazooBottom"])
        imNew.putpixel((14, 17), colorsDict["kazooBottom"])
        imNew.putpixel((15, 17), colorsDict["kazooBottom"])
        imNew.putpixel((16, 17), colorsDict["kazooBottom"])
        imNew.putpixel((17, 17), colorsDict["kazooBottom"])
    elif decodedType == "Money":
        imNew.putpixel((11, 16), colorsDict["moneyOuter"])
        imNew.putpixel((12, 16), colorsDict["moneyOuter"])
        imNew.putpixel((13, 16), colorsDict["moneyOuter"])
        imNew.putpixel((14, 16), colorsDict["moneyOuter"])
        imNew.putpixel((15, 16), colorsDict["moneyOuter"])
        imNew.putpixel((16, 16), colorsDict["moneyOuter"])
        imNew.putpixel((17, 16), colorsDict["moneyOuter"])
        imNew.putpixel((18, 16), colorsDict["moneyOuter"])

        imNew.putpixel((11, 17), colorsDict["moneyOuter"])
        imNew.putpixel((12, 17), colorsDict["moneyAccent"])
        imNew.putpixel((13, 17), colorsDict["moneyInner"])
        imNew.putpixel((14, 17), colorsDict["black"])
        imNew.putpixel((15, 17), colorsDict["moneyInner"])
        imNew.putpixel((16, 17), colorsDict["moneyInner"])
        imNew.putpixel((17, 17), colorsDict["moneyAccent"])
        imNew.putpixel((18, 17), colorsDict["moneyOuter"])

        imNew.putpixel((11, 18), colorsDict["moneyOuter"])
        imNew.putpixel((12, 18), colorsDict["moneyAccent"])
        imNew.putpixel((13, 18), colorsDict["moneyInner"])
        imNew.putpixel((14, 18), colorsDict["moneyInner"])
        imNew.putpixel((15, 18), colorsDict["black"])
        imNew.putpixel((16, 18), colorsDict["moneyInner"])
        imNew.putpixel((17, 18), colorsDict["moneyAccent"])
        imNew.putpixel((18, 18), colorsDict["moneyOuter"])

        imNew.putpixel((11, 19), colorsDict["moneyOuter"])
        imNew.putpixel((12, 19), colorsDict["moneyOuter"])
        imNew.putpixel((13, 19), colorsDict["moneyOuter"])
        imNew.putpixel((14, 19), colorsDict["moneyOuter"])
        imNew.putpixel((15, 19), colorsDict["moneyOuter"])
        imNew.putpixel((16, 19), colorsDict["moneyOuter"])
        imNew.putpixel((17, 19), colorsDict["moneyOuter"])
        imNew.putpixel((18, 19), colorsDict["moneyOuter"])
    elif decodedType == "FireBreath":
        imNew.putpixel((20, 10), colorsDict["fireRed"])

        imNew.putpixel((22, 11), colorsDict["fireRed"])

        imNew.putpixel((17, 12), colorsDict["fireRed"])
        imNew.putpixel((18, 12), colorsDict["fireRed"])
        imNew.putpixel((19, 12), colorsDict["fireRed"])
        imNew.putpixel((20, 12), colorsDict["fireRed"])

        imNew.putpixel((16, 13), colorsDict["fireRed"])
        imNew.putpixel((17, 13), colorsDict["fireOrange"])
        imNew.putpixel((18, 13), colorsDict["fireRed"])

        imNew.putpixel((14, 14), colorsDict["fireRed"])
        imNew.putpixel((15, 14), colorsDict["fireOrange"])
        imNew.putpixel((16, 14), colorsDict["fireOrange"])
        imNew.putpixel((17, 14), colorsDict["fireYellow"])
        imNew.putpixel((18, 14), colorsDict["fireOrange"])
        imNew.putpixel((19, 14), colorsDict["fireRed"])
        imNew.putpixel((21, 14), colorsDict["fireRed"])

        imNew.putpixel((13, 15), colorsDict["fireRed"])
        imNew.putpixel((14, 15), colorsDict["fireOrange"])
        imNew.putpixel((15, 15), colorsDict["fireYellow"])
        imNew.putpixel((16, 15), colorsDict["fireYellow"])
        imNew.putpixel((17, 15), colorsDict["fireYellow"])
        imNew.putpixel((18, 15), colorsDict["fireYellow"])
        imNew.putpixel((19, 15), colorsDict["fireOrange"])
        imNew.putpixel((20, 15), colorsDict["fireRed"])

        imNew.putpixel((11, 16), colorsDict["fireYellow"])
        imNew.putpixel((12, 16), colorsDict["fireYellow"])
        imNew.putpixel((13, 16), colorsDict["fireYellow"])
        imNew.putpixel((14, 16), colorsDict["fireYellow"])
        imNew.putpixel((15, 16), colorsDict["fireYellow"])
        imNew.putpixel((16, 16), colorsDict["fireYellow"])
        imNew.putpixel((17, 16), colorsDict["fireYellow"])
        imNew.putpixel((18, 16), colorsDict["fireYellow"])
        imNew.putpixel((19, 16), colorsDict["fireYellow"])
        imNew.putpixel((20, 16), colorsDict["fireOrange"])
        imNew.putpixel((21, 16), colorsDict["fireRed"])
        imNew.putpixel((22, 16), colorsDict["fireRed"])

        imNew.putpixel((13, 17), colorsDict["fireRed"])
        imNew.putpixel((14, 17), colorsDict["fireOrange"])
        imNew.putpixel((15, 17), colorsDict["fireYellow"])
        imNew.putpixel((16, 17), colorsDict["fireYellow"])
        imNew.putpixel((17, 17), colorsDict["fireYellow"])
        imNew.putpixel((18, 17), colorsDict["fireYellow"])
        imNew.putpixel((19, 17), colorsDict["fireOrange"])
        imNew.putpixel((20, 17), colorsDict["fireRed"])

        imNew.putpixel((14, 18), colorsDict["fireRed"])
        imNew.putpixel((15, 18), colorsDict["fireOrange"])
        imNew.putpixel((16, 18), colorsDict["fireOrange"])
        imNew.putpixel((17, 18), colorsDict["fireYellow"])
        imNew.putpixel((18, 18), colorsDict["fireOrange"])
        imNew.putpixel((19, 18), colorsDict["fireRed"])
        imNew.putpixel((23, 18), colorsDict["fireRed"])

        imNew.putpixel((15, 19), colorsDict["fireRed"])
        imNew.putpixel((16, 19), colorsDict["fireRed"])
        imNew.putpixel((17, 19), colorsDict["fireOrange"])
        imNew.putpixel((18, 19), colorsDict["fireRed"])

        imNew.putpixel((17, 20), colorsDict["fireRed"])
        imNew.putpixel((18, 20), colorsDict["fireRed"])
        imNew.putpixel((19, 20), colorsDict["fireRed"])
        imNew.putpixel((20, 20), colorsDict["fireRed"])
        imNew.putpixel((22, 20), colorsDict["fireRed"])

        imNew.putpixel((20, 22), colorsDict["fireRed"])
    elif decodedType == "Bone":

        imNew.putpixel((11, 15), colorsDict["black"])
        imNew.putpixel((12, 15), colorsDict["black"])
        imNew.putpixel((19, 15), colorsDict["black"])
        imNew.putpixel((20, 15), colorsDict["black"])

        imNew.putpixel((10, 16), colorsDict["black"])
        imNew.putpixel((11, 16), colorsDict["bone"])
        imNew.putpixel((12, 16), colorsDict["bone"])
        imNew.putpixel((13, 16), colorsDict["black"])
        imNew.putpixel((18, 16), colorsDict["black"])
        imNew.putpixel((19, 16), colorsDict["bone"])
        imNew.putpixel((20, 16), colorsDict["bone"])
        imNew.putpixel((21, 16), colorsDict["black"])

        imNew.putpixel((10, 17), colorsDict["black"])
        imNew.putpixel((11, 17), colorsDict["bone"])
        imNew.putpixel((12, 17), colorsDict["bone"])
        imNew.putpixel((13, 17), colorsDict["bone"])
        imNew.putpixel((14, 17), colorsDict["black"])
        imNew.putpixel((15, 17), colorsDict["black"])
        imNew.putpixel((16, 17), colorsDict["black"])
        imNew.putpixel((17, 17), colorsDict["black"])
        imNew.putpixel((18, 17), colorsDict["white"])
        imNew.putpixel((19, 17), colorsDict["bone"])
        imNew.putpixel((20, 17), colorsDict["bone"])
        imNew.putpixel((21, 17), colorsDict["black"])

        imNew.putpixel((11, 18), colorsDict["black"])
        imNew.putpixel((12, 18), colorsDict["bone"])
        imNew.putpixel((13, 18), colorsDict["bone"])
        imNew.putpixel((14, 18), colorsDict["bone"])
        imNew.putpixel((15, 18), colorsDict["bone"])
        imNew.putpixel((16, 18), colorsDict["bone"])
        imNew.putpixel((17, 18), colorsDict["bone"])
        imNew.putpixel((18, 18), colorsDict["bone"])
        imNew.putpixel((19, 18), colorsDict["white"])
        imNew.putpixel((20, 18), colorsDict["black"])

        imNew.putpixel((10, 19), colorsDict["black"])
        imNew.putpixel((11, 19), colorsDict["boneShade"])
        imNew.putpixel((12, 19), colorsDict["bone"])
        imNew.putpixel((13, 19), colorsDict["bone"])
        imNew.putpixel((14, 19), colorsDict["black"])
        imNew.putpixel((15, 19), colorsDict["black"])
        imNew.putpixel((16, 19), colorsDict["black"])
        imNew.putpixel((17, 19), colorsDict["black"])
        imNew.putpixel((18, 19), colorsDict["bone"])
        imNew.putpixel((19, 19), colorsDict["bone"])
        imNew.putpixel((20, 19), colorsDict["bone"])
        imNew.putpixel((21, 19), colorsDict["black"])

        imNew.putpixel((10, 20), colorsDict["black"])
        imNew.putpixel((11, 20), colorsDict["boneShade"])
        imNew.putpixel((12, 20), colorsDict["boneShade"])
        imNew.putpixel((13, 20), colorsDict["black"])
        imNew.putpixel((18, 20), colorsDict["black"])
        imNew.putpixel((19, 20), colorsDict["boneShade"])
        imNew.putpixel((20, 20), colorsDict["bone"])
        imNew.putpixel((21, 20), colorsDict["black"])

        imNew.putpixel((11, 21), colorsDict["black"])
        imNew.putpixel((12, 21), colorsDict["black"])
        imNew.putpixel((19, 21), colorsDict["black"])
        imNew.putpixel((20, 21), colorsDict["black"])

    elif decodedType == "DiamondBone":

        imNew.putpixel((11, 15), colorsDict["black"])
        imNew.putpixel((12, 15), colorsDict["black"])
        imNew.putpixel((19, 15), colorsDict["black"])
        imNew.putpixel((20, 15), colorsDict["black"])

        imNew.putpixel((10, 16), colorsDict["black"])
        imNew.putpixel((11, 16), colorsDict["diamondBoneShade1"])
        imNew.putpixel((12, 16), colorsDict["diamondBone"])
        imNew.putpixel((13, 16), colorsDict["black"])
        imNew.putpixel((18, 16), colorsDict["black"])
        imNew.putpixel((19, 16), colorsDict["diamondBone"])
        imNew.putpixel((20, 16), colorsDict["white"])
        imNew.putpixel((21, 16), colorsDict["black"])

        imNew.putpixel((10, 17), colorsDict["black"])
        imNew.putpixel((11, 17), colorsDict["diamondBoneShade2"])
        imNew.putpixel((12, 17), colorsDict["diamondBone"])
        imNew.putpixel((13, 17), colorsDict["diamondBone"])
        imNew.putpixel((14, 17), colorsDict["black"])
        imNew.putpixel((15, 17), colorsDict["black"])
        imNew.putpixel((16, 17), colorsDict["black"])
        imNew.putpixel((17, 17), colorsDict["black"])
        imNew.putpixel((18, 17), colorsDict["diamondBoneShade1"])
        imNew.putpixel((19, 17), colorsDict["diamondBone"])
        imNew.putpixel((20, 17), colorsDict["diamondBone"])
        imNew.putpixel((21, 17), colorsDict["black"])

        imNew.putpixel((11, 18), colorsDict["black"])
        imNew.putpixel((12, 18), colorsDict["diamondBone"])
        imNew.putpixel((13, 18), colorsDict["diamondBoneShade1"])
        imNew.putpixel((14, 18), colorsDict["diamondBone"])
        imNew.putpixel((15, 18), colorsDict["diamondBoneShade1"])
        imNew.putpixel((16, 18), colorsDict["diamondBoneShade1"])
        imNew.putpixel((17, 18), colorsDict["diamondBone"])
        imNew.putpixel((18, 18), colorsDict["diamondBone"])
        imNew.putpixel((19, 18), colorsDict["diamondBone"])
        imNew.putpixel((20, 18), colorsDict["black"])

        imNew.putpixel((10, 19), colorsDict["black"])
        imNew.putpixel((11, 19), colorsDict["diamondBoneShade2"])
        imNew.putpixel((12, 19), colorsDict["diamondBone"])
        imNew.putpixel((13, 19), colorsDict["diamondBone"])
        imNew.putpixel((14, 19), colorsDict["black"])
        imNew.putpixel((15, 19), colorsDict["black"])
        imNew.putpixel((16, 19), colorsDict["black"])
        imNew.putpixel((17, 19), colorsDict["black"])
        imNew.putpixel((18, 19), colorsDict["diamondBoneShade2"])
        imNew.putpixel((19, 19), colorsDict["diamondBone"])
        imNew.putpixel((20, 19), colorsDict["diamondBoneShade1"])
        imNew.putpixel((21, 19), colorsDict["black"])

        imNew.putpixel((10, 20), colorsDict["black"])
        imNew.putpixel((11, 20), colorsDict["diamondBoneShade2"])
        imNew.putpixel((12, 20), colorsDict["diamondBoneShade2"])
        imNew.putpixel((13, 20), colorsDict["black"])
        imNew.putpixel((18, 20), colorsDict["black"])
        imNew.putpixel((19, 20), colorsDict["diamondBoneShade2"])
        imNew.putpixel((20, 20), colorsDict["diamondBone"])
        imNew.putpixel((21, 20), colorsDict["black"])

        imNew.putpixel((11, 21), colorsDict["black"])
        imNew.putpixel((12, 21), colorsDict["black"])
        imNew.putpixel((19, 21), colorsDict["black"])
        imNew.putpixel((20, 21), colorsDict["black"])
    
    elif decodedType == "ChickenBone":

        imNew.putpixel((19, 14), colorsDict["black"])
        imNew.putpixel((20, 14), colorsDict["black"])

        imNew.putpixel((11, 15), colorsDict["black"])
        imNew.putpixel((12, 15), colorsDict["black"])
        imNew.putpixel((17, 15), colorsDict["black"])
        imNew.putpixel((18, 15), colorsDict["black"])
        imNew.putpixel((19, 15), colorsDict["chickenBone2"])
        imNew.putpixel((20, 15), colorsDict["chickenBone2"])
        imNew.putpixel((21, 15), colorsDict["black"])

        imNew.putpixel((10, 16), colorsDict["black"])
        imNew.putpixel((11, 16), colorsDict["bone"])
        imNew.putpixel((12, 16), colorsDict["bone"])
        imNew.putpixel((13, 16), colorsDict["black"])
        imNew.putpixel((16, 16), colorsDict["black"])
        imNew.putpixel((17, 16), colorsDict["chickenBone1"])
        imNew.putpixel((18, 16), colorsDict["chickenBone1"])
        imNew.putpixel((19, 16), colorsDict["chickenBone1"])
        imNew.putpixel((20, 16), colorsDict["chickenBone1"])
        imNew.putpixel((21, 16), colorsDict["chickenBone2"])
        imNew.putpixel((22, 16), colorsDict["black"])

        imNew.putpixel((10, 17), colorsDict["black"])
        imNew.putpixel((11, 17), colorsDict["bone"])
        imNew.putpixel((12, 17), colorsDict["bone"])
        imNew.putpixel((13, 17), colorsDict["bone"])
        imNew.putpixel((14, 17), colorsDict["black"])
        imNew.putpixel((15, 17), colorsDict["black"])
        imNew.putpixel((16, 17), colorsDict["black"])
        imNew.putpixel((17, 17), colorsDict["chickenBone1"])
        imNew.putpixel((18, 17), colorsDict["chickenBone1"])
        imNew.putpixel((19, 17), colorsDict["chickenBone1"])
        imNew.putpixel((20, 17), colorsDict["chickenBone1"])
        imNew.putpixel((21, 17), colorsDict["chickenBone1"])
        imNew.putpixel((22, 17), colorsDict["chickenBone2"])
        imNew.putpixel((23, 17), colorsDict["black"])

        imNew.putpixel((11, 18), colorsDict["black"])
        imNew.putpixel((12, 18), colorsDict["bone"])
        imNew.putpixel((13, 18), colorsDict["bone"])
        imNew.putpixel((14, 18), colorsDict["bone"])
        imNew.putpixel((15, 18), colorsDict["bone"])
        imNew.putpixel((16, 18), colorsDict["chickenBone3"])
        imNew.putpixel((17, 18), colorsDict["chickenBone1"])
        imNew.putpixel((18, 18), colorsDict["chickenBone1"])
        imNew.putpixel((19, 18), colorsDict["chickenBone1"])
        imNew.putpixel((20, 18), colorsDict["chickenBone1"])
        imNew.putpixel((21, 18), colorsDict["chickenBone1"])
        imNew.putpixel((22, 18), colorsDict["chickenBone1"])
        imNew.putpixel((23, 18), colorsDict["black"])

        imNew.putpixel((10, 19), colorsDict["black"])
        imNew.putpixel((11, 19), colorsDict["boneShade"])
        imNew.putpixel((12, 19), colorsDict["bone"])
        imNew.putpixel((13, 19), colorsDict["bone"])
        imNew.putpixel((14, 19), colorsDict["black"])
        imNew.putpixel((15, 19), colorsDict["black"])
        imNew.putpixel((16, 19), colorsDict["black"])
        imNew.putpixel((17, 19), colorsDict["chickenBone1"])
        imNew.putpixel((18, 19), colorsDict["chickenBone1"])
        imNew.putpixel((19, 19), colorsDict["chickenBone1"])
        imNew.putpixel((20, 19), colorsDict["chickenBone1"])
        imNew.putpixel((21, 19), colorsDict["chickenBone1"])
        imNew.putpixel((22, 19), colorsDict["chickenBone3"])
        imNew.putpixel((23, 19), colorsDict["black"])

        imNew.putpixel((10, 20), colorsDict["black"])
        imNew.putpixel((11, 20), colorsDict["boneShade"])
        imNew.putpixel((12, 20), colorsDict["boneShade"])
        imNew.putpixel((13, 20), colorsDict["black"])
        imNew.putpixel((16, 20), colorsDict["black"])
        imNew.putpixel((17, 20), colorsDict["chickenBone3"])
        imNew.putpixel((18, 20), colorsDict["chickenBone3"])
        imNew.putpixel((19, 20), colorsDict["chickenBone1"])
        imNew.putpixel((20, 20), colorsDict["chickenBone1"])
        imNew.putpixel((21, 20), colorsDict["chickenBone3"])
        imNew.putpixel((22, 20), colorsDict["black"])

        imNew.putpixel((11, 21), colorsDict["black"])
        imNew.putpixel((12, 21), colorsDict["black"])
        imNew.putpixel((17, 21), colorsDict["black"])
        imNew.putpixel((18, 21), colorsDict["black"])
        imNew.putpixel((19, 21), colorsDict["chickenBone3"])
        imNew.putpixel((20, 21), colorsDict["chickenBone3"])
        imNew.putpixel((21, 21), colorsDict["black"])

        imNew.putpixel((19, 22), colorsDict["black"])
        imNew.putpixel((20, 22), colorsDict["black"])

    elif decodedType == "TongueOut":
        imNew.putpixel((14, 19), colorsDict["black"])
        imNew.putpixel((15, 19), colorsDict["tongue"])
        imNew.putpixel((16, 19), colorsDict["tongue"])
        imNew.putpixel((17, 19), colorsDict["black"])
        imNew.putpixel((15, 20), colorsDict["tongue"])
        imNew.putpixel((16, 20), colorsDict["tongue"])
        imNew.putpixel((15, 21), colorsDict["tongue"])
        imNew.putpixel((16, 21), colorsDict["tongue"])

    elif decodedType == "Joint":
        imNew.putpixel((25, 12), colorsDict["jointSmoke"])

        imNew.putpixel((24, 13), colorsDict["jointSmoke"])
        imNew.putpixel((25, 13), colorsDict["jointSmoke"])
        imNew.putpixel((26, 13), colorsDict["jointSmoke"])

        imNew.putpixel((24, 14), colorsDict["jointSmoke"])
        imNew.putpixel((25, 14), colorsDict["jointSmoke"])
        imNew.putpixel((26, 14), colorsDict["jointSmoke"])

        if typeEncoding not in typesWithoutHighEyes:
            imNew.putpixel((12, 15), colorsDict["jointEyes"])
            imNew.putpixel((18, 15), colorsDict["jointEyes"])

        imNew.putpixel((25, 15), colorsDict["jointSmoke"])

        imNew.putpixel((25, 17), colorsDict["jointSmoke"])

        imNew.putpixel((15, 19), colorsDict["black"])
        imNew.putpixel((16, 19), colorsDict["joint"])
        imNew.putpixel((17, 19), colorsDict["black"])
        imNew.putpixel((25, 19), colorsDict["jointSmoke"])

        imNew.putpixel((15, 20), colorsDict["black"])
        imNew.putpixel((16, 20), colorsDict["black"])
        imNew.putpixel((17, 20), colorsDict["joint"])
        imNew.putpixel((18, 20), colorsDict["black"])

        imNew.putpixel((17, 21), colorsDict["black"])
        imNew.putpixel((18, 21), colorsDict["joint"])
        imNew.putpixel((19, 21), colorsDict["black"])
        imNew.putpixel((20, 21), colorsDict["black"])
        imNew.putpixel((21, 21), colorsDict["black"])
        imNew.putpixel((24, 21), colorsDict["jointSmoke"])

        imNew.putpixel((18, 22), colorsDict["black"])
        imNew.putpixel((19, 22), colorsDict["joint"])
        imNew.putpixel((20, 22), colorsDict["jointBurn"])
        imNew.putpixel((21, 22), colorsDict["black"])
        imNew.putpixel((23, 22), colorsDict["jointSmoke"])

        imNew.putpixel((19, 23), colorsDict["black"])
        imNew.putpixel((20, 23), colorsDict["black"])
        imNew.putpixel((21, 23), colorsDict["black"])

    elif decodedType == "Pipe":
        imNew.putpixel((24, 14), colorsDict["pipeSmoke"])
        imNew.putpixel((25, 14), colorsDict["pipeSmoke"])
        imNew.putpixel((26, 14), colorsDict["pipeSmoke"])
        imNew.putpixel((24, 15), colorsDict["pipeSmoke"])
        imNew.putpixel((25, 15), colorsDict["pipeSmoke"])
        imNew.putpixel((26, 15), colorsDict["pipeSmoke"])
        imNew.putpixel((25, 16), colorsDict["pipeSmoke"])
        imNew.putpixel((25, 18), colorsDict["pipeSmoke"])

        imNew.putpixel((15, 20), colorsDict["black"])
        imNew.putpixel((16, 20), colorsDict["pipe"])
        imNew.putpixel((17, 20), colorsDict["black"])
        imNew.putpixel((24, 20), colorsDict["pipeSmoke"])

        # imNew.putpixel((15, 21), colorsDict["black"])
        imNew.putpixel((16, 21), colorsDict["black"])
        imNew.putpixel((17, 21), colorsDict["pipe"])
        imNew.putpixel((18, 21), colorsDict["black"])
        imNew.putpixel((22, 21), colorsDict["black"])
        imNew.putpixel((23, 21), colorsDict["black"])
        imNew.putpixel((24, 21), colorsDict["black"])
        imNew.putpixel((25, 21), colorsDict["black"])

        imNew.putpixel((17, 22), colorsDict["black"])
        imNew.putpixel((18, 22), colorsDict["pipe"])
        imNew.putpixel((19, 22), colorsDict["black"])
        imNew.putpixel((22, 22), colorsDict["black"])
        imNew.putpixel((23, 22), colorsDict["pipe"])
        imNew.putpixel((24, 22), colorsDict["pipe"])
        imNew.putpixel((25, 22), colorsDict["black"])

        imNew.putpixel((18, 23), colorsDict["black"])
        imNew.putpixel((19, 23), colorsDict["pipe"])
        imNew.putpixel((20, 23), colorsDict["black"])
        imNew.putpixel((22, 23), colorsDict["black"])
        imNew.putpixel((23, 23), colorsDict["pipe"])
        imNew.putpixel((24, 23), colorsDict["pipe"])
        imNew.putpixel((25, 23), colorsDict["black"])

        imNew.putpixel((19, 24), colorsDict["black"])
        imNew.putpixel((20, 24), colorsDict["pipe"])
        imNew.putpixel((21, 24), colorsDict["black"])
        imNew.putpixel((22, 24), colorsDict["black"])
        imNew.putpixel((23, 24), colorsDict["pipe"])
        imNew.putpixel((24, 24), colorsDict["pipe"])
        imNew.putpixel((25, 24), colorsDict["black"])
       
        imNew.putpixel((20, 25), colorsDict["black"])
        imNew.putpixel((21, 25), colorsDict["pipe"])
        imNew.putpixel((22, 25), colorsDict["pipe"])
        imNew.putpixel((23, 25), colorsDict["pipe"])
        imNew.putpixel((24, 25), colorsDict["black"])

        imNew.putpixel((21, 26), colorsDict["black"])
        imNew.putpixel((22, 26), colorsDict["black"])
        imNew.putpixel((23, 26), colorsDict["black"])
    
        
    elif decodedType == "Vape":
        imNew.putpixel((26, 16), colorsDict["pipeSmoke"])

        imNew.putpixel((25, 17), colorsDict["pipeSmoke"])
        # imNew.putpixel((22, 14), backgroundLookup[backgroundColor])
        imNew.putpixel((26, 17), colorsDict["vapeInnerSmoke"])
        imNew.putpixel((27, 17), colorsDict["pipeSmoke"])

        imNew.putpixel((25, 18), colorsDict["pipeSmoke"])
        # imNew.putpixel((22, 15), backgroundLookup[backgroundColor])
        imNew.putpixel((26, 18), colorsDict["vapeInnerSmoke"])
        imNew.putpixel((27, 18), colorsDict["pipeSmoke"])

        imNew.putpixel((15, 19), colorsDict["black"])
        imNew.putpixel((16, 19), colorsDict["vape"])
        imNew.putpixel((17, 19), colorsDict["black"])
        imNew.putpixel((26, 19), colorsDict["pipeSmoke"])
    
        imNew.putpixel((15, 20), colorsDict["black"])
        imNew.putpixel((16, 20), colorsDict["black"])
        imNew.putpixel((17, 20), colorsDict["vape"])
        imNew.putpixel((18, 20), colorsDict["black"])

        imNew.putpixel((17, 21), colorsDict["black"])
        imNew.putpixel((18, 21), colorsDict["vape"])
        imNew.putpixel((19, 21), colorsDict["black"])
        imNew.putpixel((26, 21), colorsDict["pipeSmoke"])

        imNew.putpixel((18, 22), colorsDict["black"])
        imNew.putpixel((19, 22), colorsDict["vape"])
        imNew.putpixel((20, 22), colorsDict["black"])
        imNew.putpixel((21, 22), colorsDict["black"])
        imNew.putpixel((22, 22), colorsDict["black"])
  
        imNew.putpixel((19, 23), colorsDict["black"])
        imNew.putpixel((20, 23), colorsDict["vape"])
        imNew.putpixel((21, 23), colorsDict["vapeLight"])
        imNew.putpixel((22, 23), colorsDict["black"])
        imNew.putpixel((25, 23), colorsDict["pipeSmoke"])
        
        imNew.putpixel((20, 24), colorsDict["black"])
        imNew.putpixel((21, 24), colorsDict["black"])
        imNew.putpixel((22, 24), colorsDict["black"]) 

    im.paste(imNew, (0,0), mask=imNew)
