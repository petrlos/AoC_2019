class Cable:

    def __init__(self, path):
        self.pathStr = path
        self.path = []
        self.distance = []

    def __str__(self):
        return str(self.pathStr)

    def getPath(self):
        x, y = 0, 0
        deltax, deltay = 0, 0
        steps = 0
        for instruction in self.pathStr:
            if "R" in instruction:
                deltax = 1
                deltay = 0
            if "L" in instruction:
                deltax = -1
                deltay = 0
            if "D" in instruction:
                deltax = 0
                deltay = -1
            if "U" in instruction:
                deltax = 0
                deltay = 1
            for _ in range(0, int(instruction[1:])):
                x += deltax
                y += deltay
                steps += 1
                self.path.append((x,y))
                self.distance.append((x,y,steps))
        #print(self.distance)


