class Packet:

    def __init__(self, routerID):
        "intitlise the header for the packet"
        self.packet = bytearray(3)
        self.packet[0] = 2
        self.pacekt[1] = 2
        self.packet[2] = routerID
        
