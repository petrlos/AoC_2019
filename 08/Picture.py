class Picture:

    def __init__(self, input, width, height):
        self.height = height
        self.width = width
        self.input = input
        self.layers = []

        self.__getLayers()

    def __getLayers(self):
        layer = ""
        column, row = 1, 1
        for char in self.input:
            layer += char
            column += 1
            if column > self.width:
                column = 1
                layer += "\n"
                row += 1
            if row > self.height:
                row = 1
                self.layers.append(layer)
                layer = ""

    def __getLayerWithLeastZeros(self):
        zeros = []
        for layer in self.layers:
            zerosCount = layer.count("0")
            zeros.append(zerosCount)
        return self.layers[zeros.index(min(zeros))]

    def resultTask1(self):
        layerLeastZeros = self.__getLayerWithLeastZeros()
        oneCount = layerLeastZeros.count("1")
        twoCount = layerLeastZeros.count("2")
        return oneCount * twoCount

    def __transparentLayer(self):
        result = ""
        for i in range(0,self.height):
            for j in range(0, self.width):
                result += "2"
            result += "\n"
        return result

    def __replaceCharInString(self, strToReplace, char, index):
        return strToReplace[:index] + char + strToReplace[index + 1:]

    def overlayLayers(self):
        #zacina z 0. vrstvy ktera je komplet pruhledna
        result = self.__transparentLayer()
        #postupne prochazi znaky po vrstvach, a prepisuje je ve vysledku
        for layer in self.layers:
            for i in range(0,len(layer)):
                if layer[i] != "2" and result[i] == "2":
                    result = self.__replaceCharInString(result, layer[i], i)
        return result

    def decodeMessage(self, message):
        result = ""
        for char in message:
            if char == "1":
                result += "█"
            if char == "0":
                result += " "
            if char == "\n":
                result += "\n"
        return result

