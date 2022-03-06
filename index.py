from PIL import Image
import random
import os
import sys
import schema

imageSchema = schema.imageSchema
NUMBER_OF_IMAGES = schema.NUMBER_OF_IMAGES

createdIds = set()

#calculate how many possible combinations of images there are 
def maxNumOfImagesPossible():
    sum = 1 
    for i in range(len(imageSchema)):
        sum *= imageSchema[i]["amount"]
    return sum

# returns image2 ontop of image1
def layerTwoImages(image1, image2):
    image1.paste(image2, (0, 0), image2)
    return image1

# create unique id that is used to build the image
def generateUniqueImageID():
    generatedId =[] 
    for i in range(len(imageSchema)):
        currLayerAmount = imageSchema[i]["amount"]
        randLayerNum = random.randint(0, currLayerAmount - 1)
        generatedId.append(str(randLayerNum))

    if "".join(generatedId) in createdIds: 
        return 
    createdIds.add("".join(generatedId))
    return generatedId


def generateNumOfIds(numOfIds,array,numCreated = 0):
    if numCreated == numOfIds:
        return 
    
    if numCreated == maxNumOfImagesPossible():
        print("MAX NUMBER OF IMAGES PRINTED")
        return 

    _id = generateUniqueImageID() 
    if _id:
        array.append(_id)
        numCreated += 1

    generateNumOfIds(numOfIds, array, numCreated)


# create image from ID 
def buildImageFromID(id):
    imageComponents = [] 

    for i in range(len(imageSchema)):

        dirFiles = os.listdir(f'./{imageSchema[i]["name"]}')
        img = Image.open(f'./{imageSchema[i]["name"]}/{dirFiles[int(id[i])]}')

        imageComponents.append(img)
    layeredImage = imageComponents[0]
    for i in range(len(imageComponents)):
        if i + 1 >= len(imageComponents): break
        layeredImage = layerTwoImages(layeredImage, imageComponents[i + 1])

    return layeredImage


#create a number of Images from a list of IDs
def buildNumOfImages(listOfIDs):
    images = []
    for i in range(len(listOfIDs)):
        img = buildImageFromID(listOfIDs[i])
        images.append(img)
    return images

def saveImages(images):
    for  i in range(len(images)):
        images[i].save(f'./output/{i + 1}.png')


def main():

    sys.setrecursionlimit(10000)

    uniqueIds =[] 
    generateNumOfIds(NUMBER_OF_IMAGES, uniqueIds)

    Images = buildNumOfImages(uniqueIds)

    os.mkdir("./output")

    saveImages(Images)
    
    return 0
    

if __name__ == "__main__":
    main()