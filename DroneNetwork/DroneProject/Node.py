

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