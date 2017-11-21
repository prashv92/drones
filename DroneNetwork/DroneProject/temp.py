#Latest code for importing from Bargera network and flow files,
#flow files are a bit tricky and network dependent

from __future__ import division
from __future__ import print_function
#import networkx as nx
import time
from networkx import *
from networkx import DiGraph
from networkx import linalg
import networkx.convert as convert
import numpy

#start = time.time()

#######################################################################
##################### General functions and methods ###################
#######################################################################

# Define the class and methods for generating the networks
class Network(DiGraph):
    def __init__(self, data=None, **attr):
        DiGraph.__init__(self, data, **attr)

    def readNetworkFromBargera(self, bargeraNetworkFile):
        try:
            with open(bargeraNetworkFile) as networkFile:
                for line in networkFile:
                    try:
                        data = line.strip().split('\t')
                        print(line)
                        print(data)
                        if data[0] == '~':
                            continue

                        print(data)

                        # assuming wave speed is 0.5*freeFlowSpeed
                        # attributes = Link(int(data[0]), int(data[1]), float(data[2]), float(data[3]), float(data[4]), 0.5*float(data[4]), float(data[5]), float(data[6]), float(data[7]), float(data[8]), float(data[9]))

                        # {'sourceNode': int(data[0]), 'destNode': int(data[1]), 'capacity': float(data[2]),
                        #             'length': float(data[3]), 'freeFlowTime': float(data[4]),
                        #            'waveSpeed': 0.5 *float(data[4]), 'b': float(data[5]), 'power': float(data[6]),
                        #           'speedLimit': float(data[7]), 'toll': float(data[8]), 'type': float(data[9])}
                        # self.links.append(attributes)

                        # print(attributes)
                        print('edge yet to be added')
                        self.add_edge(int(data[0]), int(data[1]), capacity = float(data[2]), length = float(data[3]), fft = float(data[4]), ws = 0.5*float(data[4]), b = float(data[5]), power = float(data[6]), speedLimit = float(data[7]), toll = float(data[8]), type = float(data[9]))  # errors out when attributes are added - expected 3 input variables but 4 provided. Must check.
                        print('Edge added')
                        print(self.get_edge_data(int(data[0]), int(data[1])))
                        # print(self.get_edge_data(attributes['sourceNode'], attributes['destNode']))
                    except:
                        print('error reading file')
                        break



        except IOError as ioError:
            print('Error reading from file' + ioError)

        print(data)

    def populate_volumes_costs(self,textfile):
        '''
        This function adds the attributes: cost of travel, volume
        Those attributes are obtained after running static traffic assignment
        They should be stored in a text file that has the following format
            First line: initialnode finalnode volume cost
            Second line: 1  2   300 0.5
            So on:
            The values on each line should be tab separated.
        '''
        try:
            with open(textfile) as results:
                results.readline()
                while True:
                    try:
                        data = results.readline()

                        ###################################################################
                        ################# CHECK HOW DATA IS DELIMITED! ####################
                        ###################################################################

                        #If you have Austin network of space separated flow file:
                        #newdata=data.rstrip() #remove \n from end and tidy up
                        #lod=newdata.split(' ')  #list of data, zero is first node, 1 is second node, 2 is volume, 3 is cost
                        #self.add_edge(int(lod[0]), int(lod[1]), {'volume': float(lod[3]), 'cost': float(lod[4])})

                        # If you have Chicago Sketch or tab separated flow file:
                        newdata=data.rstrip()
                        lod=newdata.split('\t')
                        for key,val in enumerate(lod):
                            lod[key]=val.rstrip()
                        self.add_edge(int(lod[0]), int(lod[1]), {'volume': float(lod[2]), 'cost': float(lod[3])})


                        # For the weird structure of the Anaheim network!
                        #newdata = data.rstrip()
                        #lod = newdata.split('\t')
                        #for key, val in enumerate(lod):
                        #    lod[key] = val.rstrip()
                        #self.add_edge(int(lod[0]), int(lod[1]), {'volume': float(lod[3]), 'cost': float(lod[4])})


                    except:
                        print("Error reading file")
                        break

        except IOError as ioerr:  # send an error message if filfe is not available
            print('File Error:' + str(ioerr))


f = '/Users/prashanthvenkatraman/Documents/Austin/RA/Drone routing/CTM/Austin_net.tntp.txt'
n = Network()
n.readNetworkFromBargera(f)
print(n.edges)