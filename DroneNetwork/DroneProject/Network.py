import numpy as np
from DroneProject.Link import Link
from DroneProject.Node import Node
from Vehicle import Vehicle
from random import *


# Network Class
class Network():
    attributes = []
    vehicles = []
    timeStep = 6
    timeHorizon = 100000
    cells = []
    links = []
    nodes = {}
    dynamicOD = []

    # Method to read network from Bargera file
    def readNetworkFromBargera(self, bargeraNetworkFile):
        try:
            with open(bargeraNetworkFile) as networkFile:
                for line in networkFile:
                    try:
                        data = line.strip().split('\t')
                        #print(line)
                        #print(data)
                        if line.startswith('~'):
                            continue

                        #print(data)

                        print('edge yet to be added')
                        ffs = float(data[3])/float(data[4])
                        source = self.nodes.get(int(data[0]))
                        dest = self.nodes.get(int(data[1]))

                        link = Link(int(data[0]), int(data[1]), float(data[2]), float(data[3]), ffs, 0.5*ffs, float(data[5]), float(data[6]), float(data[7]), float(data[8]), float(data[9]))
                        source.addOutgoingLink(link)
                        dest.addIncomingLink(link)

                        link.populateCells(self.timeStep)
                        self.links.append(link)

                        #self.add_edge(int(data[0]), int(data[1]), capacity = float(data[2]), length = float(data[3]), fft = float(data[4]), ws = 0.5*float(data[4]), b = float(data[5]), power = float(data[6]), speedLimit = float(data[7]), toll = float(data[8]), type = float(data[9]))  # errors out when attributes are added - expected 3 input variables but 4 provided. Must check.

                        print('Edge added')
                        #print(self.get_edge_data(int(data[0]), int(data[1])))
                        # print(self.get_edge_data(attributes['sourceNode'], attributes['destNode']))
                    except:
                        print('error reading file')
                        break



        except IOError as ioError:
            print('Error reading from file' + ioError)

        print(data)


    # Method to read network from Bargera file
    def readNodesFromBargera(self, bargeraNodesFile):
        try:
            with open(bargeraNodesFile) as nodeFile:
                for line in nodeFile:
                    try:
                        data = line.strip().split('\t')
                        # print(line)
                        # print(data)
                        if line.startswith('Node') or line.startswith('node'):
                            continue

                        # print(data)
                        node = Node(int(data[0]), int(data[1]), int(data[2]))

                        self.nodes[int(data[0])] = node
                        self.add_edge(int(data[0]), int(data[1]), capacity = float(data[2]), \
                            length = float(data[3]), fft = float(data[4]), ws = 0.5*float(data[4]), \
                                b = float(data[5]), power = float(data[6]), speedLimit = float(data[7]), \
                                    toll = float(data[8]), type = float(data[9]))
                        #  errors out when attributes are added - expected 3 input variables but 4 provided. Must check.

                        print('Node added')
                        # print(self.get_edge_data(int(data[0]), int(data[1])))
                        # print(self.get_edge_data(attributes['sourceNode'], attributes['destNode']))
                    except:
                        print('error reading file')
                        break

        except IOError as ioError:
            print('Error reading from file' + ioError)

        print(data)

    # Method to read demand File and create dynamic OD file
    def readDemandFile(self, demandFile):

        demandMatrix = []
        n = 0
        try:
            with open(demandFile) as demandF:
                for line in demandF:
                    try:
                        if line.startswith('<'):
                            print('Entered')
                            det = line.split('>')
                            if det[0] == '<NUMBER OF ZONES':
                                totalZones = int(det[1].strip())
                            continue

                        if line.startswith('\n'):
                            continue

                        if line.startswith('Origin'):
                            origDet = line.split('\t')
                            orig = int(origDet[1].strip())
                            continue


                        line = line.lstrip().rstrip()
                        demands = line.split(';')
                        print(demands)

                        for demand in demands:
                            if demand == '':
                                continue
                            print(demand)
                            d = demand.strip().split(':')
                            dest = int(d[0].strip())

                            if dest == orig:
                                continue
                            dem = float(d[1].lstrip())

                            demandTime = float(np.random.uniform(0,self.timeHorizon)/self.timeStep)

                            tup = (orig, dest, dem, demandTime)
                            self.dynamicOD.append(tup)

                    except:
                        print('error reading file')
                        break

        except IOError as ioError:
            print('Error reading from file' + ioError)

        return 0

    def getVehicles(self):
        for tup in self.dynamicOD:
            vehicle = Vehicle()