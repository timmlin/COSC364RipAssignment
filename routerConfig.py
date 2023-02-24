def readFile(name):
    """'''"""
    file = open(name, 'r')
    config = file.read().splitlines()
    return config

def getInfo(info):
    inputs2 = []
    id, inputs, outputs = info.split(",")

    id = id.split(" ")[1]

    inputs = inputs.split(" ")[2:]

    outputs = outputs.split(" ")[2:]

    # for input in inputs:
    #     input.strip()
    #     print(input)
    #     inputs2.append(int(input))
    print(id)
    print(inputs)
    print(outputs)
