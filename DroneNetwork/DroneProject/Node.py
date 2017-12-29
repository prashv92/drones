

class Node:
    id = 0
    longitude = 0
    latitude = 0
    incomingLinks = []
    outgoingLinks = []


    def __init__(self,id,longitude,latitude):
        self.id = id
        self.longitude = longitude
        self.latitude = latitude

    def getLongitude(self):
        return self.longitude

    def getLatitude(self):
        return self.latitude

    def getId(self):
        return self.id

    def addIncomingLink(self, link):
        self.incomingLinks.append(link)

    def addOutgoingLink(self, link):
        self.outgoingLinks.append(link)

    def getIncomingLinks(self):
        return self.incomingLinks

    def getOutgoingLinks(self):
        return self.outgoingLinks

    def step(self):
        linksIn = self.getIncomingLinks()
        linksOut = self.getOutgoingLinks()
        for l in linksIn:
            sending = l.calculateSendingFlow()
            for v in sending:
                nextLink = v.getNextLink()
                if nextLink is None:
                    sending.pop(v)
                else:
                    if nextLink.remainingCapacity > 0:
                        nextLink.cells[0].append(v)
                        nextLink.remainingFlow-=1

