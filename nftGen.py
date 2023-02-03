import os, sys
import random
from PIL import Image
from draw.drawType import drawSolanaBackground, drawType
from draw.drawBody import drawBody
from draw.drawNeck import drawNeck
from draw.drawHat import drawHat
from draw.drawEyes import drawEyes
from draw.drawMouth import drawMouth
from draw.drawShadow import drawShadow
from traitCount import traitCountDict
from traitEncodings import TRAIT_ENCODINGS

numTraits = 7
traitAtIndex = ["background", "type", "body", "neck", "mouth", "hat", "eyes"]
hatsToDrawSecond = ["f", "W", "a"]
mouthsToDrawLast = ["g", "i", "a"]
bodiesToDrawLast = ["g"]
bodiesToDrawAfterShadow = ["p", "q", "r"]
typesOfCaps = ["N", "O", "P", "Q", "R", "S"]

def main():
    traitsDict = buildTraitsDict()
    random.seed(53337)

    #makeNewImage(5000, "gnJ__W_")
    # makeNewImage(0, "gs_____")
    makeNewImage(0, "bw____i")
    # makeNewImage(0, "pz____i")

    dogeId = 1
    dupesRetry = 0
    timeoutsTotal = 0
    allRolls = []
    while len(traitsDict["type"]) > 0 and len(traitsDict["background"]) > 0:
        foundRollOrTimeout = False
        while not foundRollOrTimeout:
            roll = makeTraitsRoll(traitsDict)
            #ignore background trait
            rollMinusBackground = "_" + roll[1:]
            if rollMinusBackground not in allRolls:
                allRolls.append(rollMinusBackground)
                foundRollOrTimeout = True
                makeNewImage(dogeId, roll)
                dogeId = dogeId + 1
            else:
                traitsDict[traitAtIndex[0]].append(roll[0])
                traitsDict[traitAtIndex[1]].append(roll[1])
                traitsDict[traitAtIndex[2]].append(roll[2])
                traitsDict[traitAtIndex[3]].append(roll[3])
                traitsDict[traitAtIndex[4]].append(roll[4])
                traitsDict[traitAtIndex[5]].append(roll[5])
                traitsDict[traitAtIndex[6]].append(roll[6])
            if dupesRetry >= 100:
                print("Timed out trying to de-dupe: " + roll)
                foundRollOrTimeout = True
                timeoutsTotal = timeoutsTotal + 1
                if timeoutsTotal >= 100:
                    print("Too many timeouts. Exiting.")
                    exit(-1)
            dupesRetry = dupesRetry + 1
        dupesRetry = 0
    
def isDrawShadow(traits):
    # Body / Environment
    if traits[2] in ["k", "o", "e", "h"]:
        return False
    return True

def makeNewImage(iter, traits):

    # Draw the tiny version
    im = Image.new('RGBA', (32, 32))
    #print("traits: " + str(traits))
    drawSolanaBackground(im, traits[0])
    drawType(im, traits[1], traits[0])
    #drawNeck(im, traits[2])
    if (traits[2] not in bodiesToDrawLast):
        drawBody(im, traits[2], traits[1], traits[0])
    if (isDrawShadow(traits)):
        drawShadow(im)
    if (traits[2] in bodiesToDrawAfterShadow):
        drawBody(im, traits[2], traits[1], traits[0])
    if (traits[4] not in mouthsToDrawLast):
        drawMouth(im, traits[4], traits[1], traits[0])
    if (traits[5] in hatsToDrawSecond):
        drawEyes(im, traits[6], traits[1])
        drawHat(im, traits[5], traits[1], traits[0])
    else:
        drawHat(im, traits[5], traits[1], traits[0])
        drawEyes(im, traits[6], traits[1])
    if (traits[4] in mouthsToDrawLast):
        drawMouth(im, traits[4], traits[1], traits[0])
    if (traits[2] in bodiesToDrawLast):
        drawBody(im, traits[2], traits[1], traits[0])
    #smallFileName = "images/" + str(iter) + "." + l1 + l2 + l3 + ".png"
    #im.save(smallFileName, "PNG")
    
    # Make a larger version which looks nicer
    im2 = im.resize((256, 256), resample=Image.NEAREST)
    #im2.show()
    largeFileName = "images\\" + str(iter) + "." + traits + ".256.png"
    im2.save(largeFileName, "PNG")

def buildTraitsDict():
    traitsDict = { "background": [], "type": [], "body": [], "neck": [], "mouth": [], "hat": [], "eyes": [] }

    useManualDict = False
    if useManualDict:
        traitsDict = {
            "background": ["g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g"], 
            "type": ["n", "l", "d", "b", "r", "k", "n", "v", "z", "a", "n", "n", "n", "n", "n", "n", "n"], 
            "body": ["p", "w", "l", "c", "i", "k", "o", "s", "n", "y", "r", "d", "t", "_", "_", "_", "_"], 
            "neck": ["b", "r", "g", "c", "y", "o", "e", "s", "u", "d", "f", "n", "p", "_", "_", "_", "_"], 
            "mouth": ["b", "t", "j", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"], 
            "hat": ["p", "b", "r", "g", "w", "m", "z", "c", "f", "j", "k", "o", "n", "l", "h", "_", "_"],
            "eyes": ["p", "c", "a", "h", "y", "g", "s", "t", "n", "n", "v", "_", "_", "_", "_", "_", "_"]
        }
    else:
        for key in TRAIT_ENCODINGS.keys():
            #print("key: " + str(key))
            for traitEncoding in TRAIT_ENCODINGS[key]:
                currTrait = TRAIT_ENCODINGS[key][traitEncoding]
                #print("trait: " + currTrait)
                if currTrait in traitCountDict[key]:
                    for i in range(traitCountDict[key][currTrait]):
                        traitsDict[key].append(traitEncoding)

    for key in traitsDict.keys():
        while len(traitsDict[key]) < len(traitsDict["type"]):
            traitsDict[key].append("_")

    # print("traitsDict[eyes].length: " + str(len(traitsDict["eyes"])))

    # Check that all entries are equal, else fail
    expectedLen = len(traitsDict["type"])
    for key in traitsDict.keys():
        if len(traitsDict[key]) != expectedLen:
            print("Error in buildTraitsDict(). " + str(key) + " does not match expectedLen: " + str(expectedLen) + " (" + str(len(traitsDict[key])) +")")
            exit(-1)

    return traitsDict

def makeTraitsRoll(traitsDict):
    traitStr = ""
    traitList = ["background", "type", "body", "neck", "mouth", "hat", "eyes"]
    for trait in traitList:
        roll = random.choice(traitsDict[trait])
        traitsDict[trait].remove(roll)
        traitStr = traitStr + roll
    # Hack to undo 9 out of 10 full trait rolls
    #print("TraitStr: " + traitStr)
    # if not "_" in traitStr:
    #     eightyPercentChance = random.randrange(100)
    #     if eightyPercentChance >= 80:
    #         # Remove two traits
    #         slots = [2, 3, 4, 5, 6]
    #         undoSlot1 = random.choice(slots)
    #         slots.remove(undoSlot1)
    #         traitsDict[traitList[undoSlot1]].append(traitStr[undoSlot1])
    #         traitStr = traitStr[0:undoSlot1] + "_" + traitStr[undoSlot1+1:numTraits]
    #         undoSlot2 = random.choice(slots)
    #         slots.remove(undoSlot2)
    #         traitsDict[traitList[undoSlot2]].append(traitStr[undoSlot2])
    #         traitStr = traitStr[0:undoSlot2] + "_" + traitStr[undoSlot2+1:numTraits]
    
    #print("TraitStr: " + traitStr)

    # # Devil's no floppy ear
    # if traitStr[1] == "v" and TRAIT_ENCODINGS["hat"][traitStr[5]] == "FloppyEar":
    #     traitsDict["hat"].append(traitStr[5])
    #     traitStr = traitStr[0:5] + "_" + traitStr[6:]
    # # Skeleton no floppy ear
    # if traitStr[1] == "s" and TRAIT_ENCODINGS["hat"][traitStr[5]] == "FloppyEar":
    #     traitsDict["hat"].append(traitStr[5])
    #     traitStr = traitStr[0:5] + "_" + traitStr[6:]
    # # Ghosts no floppy ear
    # if traitStr[1] == "g" and TRAIT_ENCODINGS["hat"][traitStr[5]] == "FloppyEar":
    #     traitsDict["hat"].append(traitStr[5])
    #     traitStr = traitStr[0:5] + "_" + traitStr[6:]
    # # Ghosts not fat
    # if traitStr[1] == "g" and TRAIT_ENCODINGS["body"][traitStr[2]] == "Fat":
    #     traitStr = traitStr[0:2] + "_" + traitStr[3:]
    # # Ghosts no rainbow shirt
    # if traitStr[1] == "g" and TRAIT_ENCODINGS["body"][traitStr[2]] == "RainbowShirt":
    #     traitStr = traitStr[0:2] + "_" + traitStr[3:]
    # # Ghosts no wink
    # if traitStr[1] == "g" and TRAIT_ENCODINGS["eyes"][traitStr[6]] == "Wink":
    #     traitStr = traitStr[0:6] + "_"
    # # Ghosts no happy eyes
    # if traitStr[1] == "g" and TRAIT_ENCODINGS["eyes"][traitStr[6]] == "Happy":
    #     traitStr = traitStr[0:6] + "_"
    # # No laughing eyes with caps
    # if traitStr[6] == "g" and traitStr[5] in typesOfCaps:
    #     traitStr = traitStr[0:6] + "_"
    # # No tongue out for skeletons
    # if traitStr[4] == "q" and traitStr[1] == "s":
    #     traitStr = traitStr[0:4] + "_" + traitStr[5:]
    return traitStr

# Entry point
main()
