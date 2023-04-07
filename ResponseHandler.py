#Generates and processes RIP Response packets
#Tim Lindbom & Benjamin Ireland 
#23/2/23
import Router 
import socket

def GenerateResponse(router):
    """Generates response packet to be sent to other routers"""
    response = bytearray(4)
    response[0] = 2 # Indicating response message
    response[1] = 2 # Version 2
    response[3] = router.id >> 8
    response[4] = router.id & 0xFF #Router ID
    for route in router.routingTable:  # Assuming routing table is of the format [Router ID, Metric, etc.]

        # will need to account for fact that message can only be max 504 bytes and MIN 24 bytes 
        # Also need to address the the Split-Horizon Poisoned Reverse
        # ie/ If a route is learned from that router set the metric to infinity
        # if router.id = learnedID or something along those lines
        
        RTE = bytearray(20)
        RTE[6] = route[1] >> 8          # Add Router ID
        RTE[7] = route[1] & 0xFF
        # RTE[16] = route[2] & 0xFF000000     # Add Metric to router
        # RTE[17] = route[2] & 0xFF0000
        RTE[18] = route[2] & 0xFF00
        RTE[19] = route[2] & 0xFF
        response =  response + RTE      # Add RTE onto the end of response message
    
    return response

def SendResponse(router):
    """Used to send a response message to a specified Port"""
    for output in router.outputList:
        