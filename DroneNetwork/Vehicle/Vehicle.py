
class Vehicle:
    sourceNode = None
    destNode = None
    id = 0
    path = list()
    currentLink = None
    nextLink = None
    currentCell = None
    depTime = 0

    def __init__(self, sourceNode, destNode, id, depTime):
        self.sourceNode = sourceNode
        self.destNode = destNode
        self.id = id
        self.depTime = depTime


    def getPath(self):
        return self.path

    def setPath(self, path):
        self.path = path