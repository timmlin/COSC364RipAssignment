#Router class used for RIP protocol
#Tim Lindbom & Ben Ireland
#8/3/23

import socket, time

class Router:

    def __init__(self, parameters):
        self.id = parameters[0]        
        self.inputs = parameters[1]
        self.outputs = parameters[2]
        self.timers = parameters[3]
        # Routing table must contain Router ID of Destination, Metric, and next hop ID (Maybe Timers and flag) 
        self.header = {}
        self.routingTable = {}
        self.localIP = "127.0.0.1"
        self.sockets = []

        
        self.routingTable.update({self.id: [0, self.id, 0, [None, None]]})      # Layout follows [Entry ID : Metric, Next-Hop, RouteChangeFlag, [TimeOutTimer, GarbageTimer]

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


    def PrintTable(self):
        """Prints a formatted version of the routing table"""
        sysTime = time.time()
        table = f"ROUTER ID: {self.id}\n| DESTINATION | COST | NEXT-HOP | TIMEOUT | GARBAGE COLLECTION |\n"
        for entry, route in self.routingTable.items():

            if route[3][0] == None:
                timeoutTimer = f"{'-':^9}"
            else: 
                timeoutTimer = f"{(route[3][0] - sysTime):^9.2f}"

            if route[3][1] == None:
                garbTimer = f"{'-':^20}"
            else: 
                garbTimer = f"{(route[3][1] - sysTime):^20.2f}"
            
            table = table + f"|{entry:^13}|{route[0]:^6}|{route[1]:^10}|{timeoutTimer}|{garbTimer}|\n"
        print(table)

            