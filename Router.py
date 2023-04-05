#Router class used for RIP protocol
#Tim Lindbom & Ben Ireland
#8/3/23

import socket

class Router:

    def __init__(self, parameters):
        self.id = parameters[0]        
        self.inputs = parameters[1]
        self.outputs = parameters[2]
        self.routingTable = []
        self.localIP = "127.0.0.1"
        self.sockets = {}

    def PrintParams(self):
        """used for testing"""
        print(self.id, self.inputs, self.outputs, self.routingTable, "\n")

        return


    def OpenSockets(self):
        """iterates over the inputs list and 
        each of the sockets"""
        for port in self.inputs:
            self.sockets[port] = port
