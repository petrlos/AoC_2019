#Advent of Code 2019 - Day 8
from Picture import Picture
from datetime import datetime
start = datetime.now()

textFile = open("data.txt", "r")
textToInput = ""

for textImport in textFile:
    textToInput = textImport[:-1]
textFile.close()

#zalozi instanci objektu Picture s definovanou vyskou + sirkou
picture = Picture(textToInput, 25, 6)

#Task1:
#najdi vrstvu, ktera obsahuje nejmene nul a vrat soucin poctu jednicek a dvojek:
print("Task 1: {0}".format(picture.resultTask1()))

#Task2:
#prekryj vrstvy podle pravidel
result = picture.overlayLayers()
#nahrad jednicky ve vysledku *, nuly mezerou
message = picture.decodeMessage(result)

print("Task 2: \n{0}".format(message))

print("Runtime:",datetime.now()-start)