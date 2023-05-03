#Router configuration file 
#Tim Lindbom & Ben Ireland
#8/3/23

import sys
import ErrorHandler


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

    try:
        #id represents a unique identifier for each router
        id = (routerInfo[0].split(" ")[1])
    except IndexError:
        print("invalid router ID \n Please make sure the router ID configuartion follows the specified configuarion")
        sys.exit()

    try:
        #inputs is a list of ports that a router can receive data from
        inputs = routerInfo[1].split(" ")[1:]
    except IndexError:
        print("ivalid input routers \n Please make sure the router inputs configuartion follows the specified configuarion")
        sys.exit()

    try:
        #outputs is a nested list each list in outputs represents a port that the
        #router can output data. Each inner list is of the form [x, y, z] where
        #x is the port number, y is the weight/distance and z is the recieving router
        outputs = routerInfo[2].split(" ")[1:]
    except IndexError:
        print("Invalid Output Router configuration \n Please make sure the router outputs configuartion follows the specified configuarion")
        sys.exit()


    # Allows for Timers to be set.
    timers = []
    if len(routerInfo) == 4:
        tempTimers = (routerInfo[3].split(" ")[1:])
        for timer in tempTimers:
            timers.append(int(timer))
    else: 
        timers = [30, 180, 120]  #[T, 6*T, 4*T]


#--------------------------------------------------------
#------------------ERROR-CHECKS--------------------------
#--------------------------------------------------------


    #runs error checks on the id value
    #if all the tests pass, id is converted to an int
    id = ErrorHandler.RouterIdCheck(id)

    #error checks the inputs values. If all tests passes
    #processed inputs is assigned to a list of ints of the port numbers 
    processedInputs = ErrorHandler.PortNumberChecks(inputs)
 
    #processedOutputs conatins all the output port inormation
    #outputPortNumbers is just the port numbers
    processedOutputs, outputPortNumbers = ErrorHandler.RouterOutputCheck(outputs)

    #comapres the input/output port number to confirm that none appear in both lists
    ErrorHandler.CompareInputsOutputs(processedInputs, outputPortNumbers)

    #makes sure the timer values follow the correct formatting
    processedTimers = ErrorHandler.TimerChecks(timers)

    

    return [id, processedInputs, processedOutputs, processedTimers]



    
