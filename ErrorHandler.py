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
        sys.exit

    return id


def RouterInputsCheck(inputs):
    """perfroms error checks on each 
    input port number in the inputs list
    and returns a list of processed inputs"""
    processedInputs = []
    for inputNum in inputs:

        numericCheck(inputNum)
        inputNum = int(inputNum)

        if not (1024 <= inputNum <= 64000):
            print(f"input port number {inputNum} is not a valid port number. \n \
                  Please make sure all input numbers are within 1024-64000")
            sys.exit

        if inputNum in processedInputs:
            print(f"input port number {inputNum} has been used more than once. \n \
                  Please make sure all input numbers are unique")
            sys.exit

        processedInputs.append(inputNum)

    return processedInputs


def RouterOutputCheck(outputData):
    """performs error checks on the output lists
    and returns a proccessed list of ints"""
    processedOutputs = []

    for value in outputData:
        numericCheck(value)
        processedOutputs.append(int(value))

    return processedOutputs







def numericCheck(value):
    """checks that an excpected integer 
    is the correct the correct type  """
    if value.isnumeric() == False:
        print(f"'{value}' is not a numeric value, please input a numeric value")
        sys.exit()
