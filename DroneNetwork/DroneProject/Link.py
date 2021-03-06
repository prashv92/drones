import Vehicle as v
from DroneProject.Cell import Cell

class Link:
    cells = list()
    sourceNode = None
    destNode = None
    capacity = 0
    length = 0
    freeFlowSpeed = 0
    waveSpeed = 0
    b = 0
    power = 0
    speedLimit = 0
    toll = 0
    type = 0
    remainingFlow = 0

    def __init__(self, sourceNode, destNode, capacity, length, freeFlowSpeed, waveSpeed, b, power, speedLimit, toll, type):
        self.sourceNode = sourceNode
        self.destNode = destNode
        self.capacity = capacity
        self.length = length
        self.freeFlowSpeed = freeFlowSpeed
        self.waveSpeed = waveSpeed
        self.b = b
        self.power = power
        self.speedLimit = speedLimit
        self.toll = toll
        self.type = type


    def populateCells(self,timeStep):
        noOfCells = int(self.length/(self.freeFlowSpeed*timeStep))
        dx = self.length/noOfCells
        startCell = Cell(0, self, None, None, self.freeFlowSpeed, self.waveSpeed, dx, timeStep, True, False)
        self.cells.append(startCell)
        prevCell = startCell
        nextCell = None
        for i in range(1,noOfCells-1):
            cell = Cell(i, self, prevCell, None, self.freeFlowSpeed, self.waveSpeed, dx, timeStep, False, False)
            self.cells.append(cell)
            prevCell.nextCell = cell
            prevCell = cell

        endCell = Cell(noOfCells, self, prevCell, None, self.freeFlowSpeed, self.waveSpeed, dx, timeStep, False, True)
        self.cells.append(endCell)

        return 0

    ####################################################
    #### Method to update cells at each time step
    ####################################################
    def updateCells(self):
        for cell in self.cells:
            prev = cell.prevCell
            minY = min(cell.calculateReceivingFlow(), prev.calculateSendingFlow())
            currVehicles = prev.getOccupancy()

            for v in currVehicles:
                cell.addVehicle(v)
                currVehicles.pop(v)

        return 0

    def sendingFlow(self):
        length = len(self.cells)
        return self.cells[length-1].calculateSendingFlow()

    def density(self):
        count = 0
        for cell in self.cells:
            count+=len(cell.getOccupancy())

        return float(count/self.length)

    def step(self):
        for c in self.cells:
            c.step()

    def update(self):
        for c in self.cells:
            c.update()

    def getReceivingFlow(self):
        startCell = self.cells[0]
        self.remainingFlow = startCell.calculateReceivingFlow()
        return self.remainingFlow

    def remainingCapacity(self,flow):
        self.remainingFlow -= 1
        return self.remainingFlow

    def addVehicle(self, vehicle):
        self.cells[0].next.append(vehicle)

