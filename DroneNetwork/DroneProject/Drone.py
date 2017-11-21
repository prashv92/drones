from DroneProject.Network import Network
from DroneProject.Cell import Cell
from Vehicle import Vehicle

class Drone:
    def meth(self):
        n = Network()
        netf = '/Users/prashanthvenkatraman/Documents/Austin/RA/Drone routing/CTM/SiouxFalls_net.txt'
        tripf = '/Users/prashanthvenkatraman/Documents/Austin/RA/Drone routing/CTM/SiouxFalls_trips.tntp.txt'
        nodesf = '/Users/prashanthvenkatraman/Documents/Austin/RA/Drone routing/CTM/SiouxFalls_node.tntp.txt'
        n.readNodesFromBargera(nodesf)
        n.readNetworkFromBargera(netf)
        n.readDemandFile(tripf)

        duration = 100
        for i in range(duration):
