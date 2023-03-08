def readFile(name):
    """'''"""
    file = open(name, 'r')
    config = file.read().splitlines()
    return config

def getInfo(info):
    id, inputs, outputs = info.split(", ")

    processed_inputs = []

    processed_outputs = []

    id = int(id.split(" ")[1])
    
    inputs = inputs.split(" ")[1:]
    for input in inputs:
            processed_inputs.append(int(input))

    outputs = outputs.split(" ")[1:]
    for output in outputs:
        peer_input, metric, peer_id = output.split("-")
        processed_outputs.append([int(peer_input), int(metric), int(peer_id)])


def verify(id, inputs, outputs):
    """'''"""
    
