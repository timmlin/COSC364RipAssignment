def readFile(name):
    """'''"""
    file = open(name, 'r')
    config = file.read().splitlines()
    return config

def getInfo(info):
    routerInfo = info.split(", ") 
    processed_inputs = []
    processed_outputs = []
    processed_timers = []

    id = int(routerInfo[0].split(" ")[1])
    
    inputs = routerInfo[1].split(" ")[1:]
    for input in inputs:
            processed_inputs.append(int(input))

    outputs = routerInfo[2].split(" ")[1:]
    for output in outputs:
        peer_input, metric, peer_id = output.split("-")
        processed_outputs.append([int(peer_input), int(metric), int(peer_id)])

    if len(routerInfo) == 4:
        timers = (routerInfo[3].split(" ")[1:])
        for timer in timers:
            processed_timers.append(int(timer))
    else: 
        processed_timers = [180, 30,30]
    
    return [id, processed_inputs, processed_outputs, processed_timers]


def verify(id, inputs, outputs):
    """'''"""
    
