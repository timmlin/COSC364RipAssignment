def readFile(name):
    """'''"""
    file = open(name, 'r')
    config = file.read().splitlines()
    return config

def getInfo(info):
    routerInfo = info.split(", ") 
    processedInputs = []
    processedOutputs = []
    processedTimers = []

    
    id = (routerInfo[0].split(" ")[1])
    inputs = routerInfo[1].split(" ")[1:]
    outputs = routerInfo[2].split(" ")[1:]
    
    numericCheck(id)
    id = int(id)

    for input in inputs:
            numericCheck(input)
            processedInputs.append(int(input))

    for output in outputs:
        outputData = output.split("-")
        outputList = []
        for value in outputData:
            numericCheck(value)
            outputList.append(int(value))
        processedOutputs.append(outputList)

    if len(routerInfo) == 4:
        timers = (routerInfo[3].split(" ")[1:])
        for timer in timers:
            processedTimers.append(int(timer))
    else: 
        processedTimers = [180, 30,30]
    
    return [id, processedInputs, processedOutputs, processedTimers]


def numericCheck(value):
    """'''"""
    if value.isnumeric() == False:
        print(f"'{value}' is not a numeric value, please input a numeric value") 
        sys.exit()
    
