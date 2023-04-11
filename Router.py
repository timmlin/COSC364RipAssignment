#Router class used for RIP protocol
#Tim Lindbom & Ben Ireland
#8/3/23

import socket

class Router:

    def __init__(self, parameters):
        self.id = parameters[0]        
        self.inputs = parameters[1]
        self.outputs = parameters[2]
        self.timers = parameters[3]
        # Routing table must contain Router ID of Destination, Metric, and next hop ID (Maybe Timers and flag) 
        self.routingTable = {}
        self.localIP = "127.0.0.1"
        self.sockets = []

        self.routingTable.update({self.id: [0,0,0, [None, None]]})      # Layout follows [Entry ID : Metric, Next-Hop, RouteInvalidFlag, [TimeOutTimer, GarbageTimer]

    def PrintParams(self):
        """used for testing"""

        print( "id: ", self.id,"\n",\
            "inputs: ", self.inputs,"\n",\
            "outputs", self.outputs, "\n",\
            "routing table: ", self.routingTable, "\n", \
            "sockets: ", self.sockets, "\n")

        return


    def OpenSockets(self):
        """iterates over the input list, creates and binds sockets for each port"""
        for port in self.inputs:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind(('', port))
            self.sockets.append(sock)





        