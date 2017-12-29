from DroneProject.Link import Link
from DroneProject.Node import Node
from DroneProject.Network import Network

class Simulator:

    duration = 0
    stepsize = 0
    network = ()
    nodes = ()
    links = ()
    vehicles = ()
    time = 0
    exitCount = 0

    def __init__(self, duration, stepsize, network, vehicles):
        self.duration = duration
        self.stepsize = stepsize
        self.network = network
        self.vehicles = vehicles
        self.nodes = network.nodes
        self.links = network.links

    def simulate(self):
        while (self.time <= self.duration):
            self.addVehicles()

            self.moveVehicles()



            self.time += self.stepsize


    def addVehicles(self):
        while (self.exitCount <= self.vehicles.size()):
            for v in self.vehicles:

                if v.getPath is None:
                    self.exitCount+= 1

                elif v.depTime >= self.time:
                    v.nextLink.addVehicle()
                    self.exitCount += 1

                else:
                    break


    def moveVehicles(self):
        n = self.network.nodes

        for l in n.links:
            l.step()

        for n in n.nodes:
            n.step()

        for l in n.links:
            l.update()


    #In progress
    def vehiclePaths(self):
        for v in self.vehicles:
            origin = v.sourceNode
            dest = v.destNode
            depTime = v.depTime

            