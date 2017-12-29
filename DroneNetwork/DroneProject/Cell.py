from Vehicle.Vehicle import Vehicle


######################
#### Cell in CTM
######################
class Cell:
    id = 0
    link = {}
    jamDensity = 0
    currentVehicles = []
    nextVehicles = []
    sendingFlow = 0
    receivingFlow = 0
    cellCapacity = 0
    waveSpeed = 0
    ffS = 0
    dx = 0
    dt = 6
    startCell = False
    endCell = False


    def __init__(self,id, link, prevCell, nextCell, ffS, waveSpeed, dx, dt, startCell, endCell):
        self.link = link
        self.id = id
        self.cellCapacity = int(link.capacity*self.dt/3600)
        self.ffS = ffS
        self.waveSpeed = waveSpeed
        self.dx = dx
        self.dt = dt
        self.prevCell = prevCell
        self.nextCell = nextCell
        self.startCell = startCell
        self.endCell = endCell


    ###########################################################
    #### Method to calculate sending flow at each time step
    ###########################################################
    def calculateSendingFlow(self):
        sendVehicles = []
        for x in range(self.sendingFlow):
            sendVehicles.append(self.currentVehicles[x])


        return sendVehicles

    def getSendingFlow(self):
        self.sendingFlow = int(min(self.cellCapacity, len(self.currentVehicles)))
        return self.sendingFlow

    ###########################################################
    #### Method to calculate receiving flow at each time step
    ###########################################################
    def calculateReceivingFlow(self):
        self.receivingFlow = int(min(self.cellCapacity, self.waveSpeed*(self.jamDensity - len(self.currentVehicles))/self.ffT))

        return self.receivingFlow

    ###########################################################
    #### Method to add vehicles to cell at each time step
    ###########################################################
    def addVehicle(self, vehicle):
        self.nextVehicles.append(vehicle)

    ###########################################################
    #### Method to get current vehicles in a cell
    ###########################################################
    def getOccupancy(self):
        return self.currentVehicles

    def step(self):
        y = min(self.calculateReceivingFlow(), self.prevCell.calculateSendingFlow())

        while y>0:
            v = self.prevCell.currentVehicles.pop(0)
            self.addVehicle(v)
            v.currentCell = self
            y-=1

    def update(self):

        for v in self.nextVehicles:
            self.currentVehicles.append(v)

        self.nextVehicles = []


