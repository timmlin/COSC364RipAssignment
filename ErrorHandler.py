# Error checks for RIP protocol
# Tim Lindbom & Ben Ireland
# 18/4/23

import sys


def RouterIdCheck(id):
    """runs Error checks on the ID to make 
    sure the given value is valid"""
    numericCheck(id)
    id = int(id)
    if not (1 <= id <= 64000):
        print(f"{id} is not a valid ID number. \
              \n please give an id value between 1 and 64000")
        sys.exit()

    return id




def RouterOutputCheck(outputs):
    """performs error checks on the output lists. 
    Returns list of all the output port info 
    as well as a list of just output port numbers"""
    processedOutputs = []
    portNumbers = []

    for output in outputs:
        outputData = output.split("-")
        tempOutputs = []
        index = 0

        for value in outputData:
            numericCheck(value)
            tempOutputs.append(int(value))
            if index == 0:
                portNumbers.append(value)
            index += 1
             
        processedOutputs.append(tempOutputs)

    PortNumberChecks(portNumbers)

    return (processedOutputs, portNumbers)



def PortNumberChecks(portNumbers):
    """perfroms error checks on each 
    input port number in the inputs list
    and returns a list of processed inputs"""

    processedPortNumbers = []

    for portNum in portNumbers:

        numericCheck(portNum)
        portNum = int(portNum)

        if not (1024 <= portNum <= 64000):
            print(f"input port number {portNum} is not a valid port number. \n \
                  Please make sure all input numbers are within 1024-64000")
            sys.exit()

        if portNum in processedPortNumbers:
            print(f"input port number {portNum} has been used more than once. \n \
                  Please make sure all input numbers are unique")
            sys.exit()

        processedPortNumbers.append(portNum)

    return processedPortNumbers



def CompareInputsOutputs(inputs, outputs):
    """comapres the input port and output port lists to 
    make sure that no ports appear in both lists"""
    for inputPort in inputs:
        if inputPort in outputs:
            print(f"port number {inputPort} appears in both inputs and outputs")
            sys.exit()
    
    for outputPort in outputs:
        if outputPort in inputs:
            print(f"port number {outputPort} appears in both inputs and outputs")
            sys.exit()



def numericCheck(value):
    """checks that an excpected integer 
    is the correct the correct type  """
    if value.isnumeric() == False:
        print(f"'{value}' is not a numeric value, please input a numeric value")
        sys.exit()



def TimerChecks(timers):
    """runs error check on the timer values"""
    firstTimer = timers[0]
    
    if (timers[1] == 6*firstTimer) & (timers[2] == 4*firstTimer):
        return timers  
    else:
        print(f"timer values do not follow the correct format \n \
              please make sure the timers follow the [T, 6*T, 4*T] formatting")
        sys.exit()