#Router configuration file 
#Tim Lindbom & Ben Ireland
#8/3/23

import sys


def readFile(name):
    """takes the config file name as a string and 
    splits the file by line into a list of strings"""
    file = open(name, 'r')
    config = file.read().splitlines()
    file.close()
    return config

    
def getInfo(info):
    print(info)
    routerInfo = info[0].split(", ") 
    processedInputs = []
    processedOutputs = []
    processedTimers = []

    
    id = (routerInfo[0].split(" ")[1])
    inputs = routerInfo[1].split(" ")[1:]
    outputs = routerInfo[2].split(" ")[1:]


    #id represents a unique identifier for each router
    numericCheck(id)
    id = int(id)

    #inputs is a list of ports that a router can receive data from
    for input in inputs:
            numericCheck(input)
            processedInputs.append(int(input))


    #outputs is a nested list each list in outputs represents a port that the
    #router can output data. Each inner list is of the form [x, y, z] where
    #x is the port number, y is the weight/distance and z is the recieving router
    for output in outputs:
        outputData = output.split("-")
        outputList = []
        for value in outputData:
            numericCheck(value)
            outputList.append(int(value))
        processedOutputs.append(outputList)

    # Allows for Timers to be set.
    if len(routerInfo) == 4:
        timers = (routerInfo[3].split(" ")[1:])
        for timer in timers:
            processedTimers.append(int(timer))
    else: 
        processedTimers = [30, 180, 120] # T, 6*T, 4*T 
    
    return [id, processedInputs, processedOutputs, processedTimers]


def numericCheck(value):
    """'''"""
    if value.isnumeric() == False:
        print(f"'{value}' is not a numeric value, please input a numeric value") 
        sys.exit()
    
