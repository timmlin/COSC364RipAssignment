#Router class used for RIP protocol
#Tim Lindbom & Ben Ireland
#8/3/23

class Router:
        
    def __init__(self, parameters):
        self.id = parameters[0]        
        self.inputs = parameters[1]
        self.outputs = parameters[2]
        self.timers = parameters[3]
        self.routingTable = []

    def PrintParams(self):
        """Print Parameters Used for Testing"""
        print(self.id, self.inputs, self.outputs, self.timers, "\n")
        return
    
    def OpenSockets(self):
        for input in self.inputs:
            return
