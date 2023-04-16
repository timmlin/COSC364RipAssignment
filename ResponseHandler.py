#Generates and processes RIP Response packets
#Tim Lindbom & Benjamin Ireland 
#23/2/23

from Router import  *
import socket

# TEST IMPORTS
# from BellmanFordAlgorithm import *

def GenerateResponse(router, recieverID, triggered=False):
    """Generates response packet to be sent to other routers"""

     ### Checks if the response is a triggered response send only the invalid routes
    if triggered == True:
        routingTable = GetInvalidRoutes(router)
        if len(routingTable) == 0:
            return None
    else:
        routingTable = router.routingTable
    ###
    response = bytearray(4)
    response[0] = 2 # Indicating response message
    response[1] = 2 # Version 2
    response[2] = router.id >> 8
    response[3] = router.id & 0xFF #Router ID
    
   
    for entryID, route in routingTable.items():  # Assuming routing table is of the format {Router ID: Metric, etc.} // NEED TO CHANGE TO DICTIONARY

        # will need to account for fact that message can only be max 504 bytes and MIN 24 bytes 
        # Also need to address the the Split-Horizon Poisoned Reverse
        # ie/ If a route is learned from that router set the metric to infinity
        # if router.id = learnedID or something along those lines
        learnedID = route[1]

        RTE = bytearray(20)
        # RTE[0:6] = 0x0
        RTE[6] = entryID >> 8          # Add Router ID
        RTE[7] = entryID & 0xFF
        # RTE[8:18] = 0x0

        if recieverID == learnedID:
            RTE[18] = 16 & 0xFF00       # If the route was learned from the router it sets the metric to INF 
            RTE[19] = 16 & 0xFF
        else:
            RTE[18] = route[0] & 0xFF00 # Add Metric to router
            RTE[19] = route[0] & 0xFF
        
        response =  response + RTE      # Add RTE onto the end of response message

    return response



def SendResponses(router, triggered=False):
    """Used to send a response message to a specified Port"""
    i = 0
    while i < len(router.outputs):   # Enter a loop cycling through the output list and sending each peer router their designated message
        port = router.outputs[i][0]
        recieverID = router.outputs[i][2]
        soc = router.sockets[i]
        response = GenerateResponse(router, recieverID, triggered)
        if response != None:
            soc.sendto(response, (router.localIP, port))
        i += 1
    
    
           

def ReadResponse(response):
    """Used to unpack recieved response message to use in the Bellman Ford algorithm"""
    i = 0
    peerRouterEntries = []
    responseHeader = response[:4] # Will need to query to see why this was done previously
    entries = response[4:]
    messageType = responseHeader[0]         # Gets the message, version, and router ID
    versionType = responseHeader[1]
    peerRouterID = responseHeader[2] << 8 | response[3]
    while i < len(entries) - 1:             # Adds each router entry into a list
        peerRouterEntries.append([entries[i + 6] << 8 | entries[i + 7], entries[i + 18] << 8 | entries[i + 19]])
        i += 20
    return [messageType, versionType, peerRouterID], peerRouterEntries


def GetInvalidRoutes(router):
    """When called will iterate over the routing table entries, if the route invalid flag is True then it will add the route to a temporary dictionary"""
    invalidRoutes = {}
    for entryID, route in router.routingTable.items(): 
        routeChangeFlag = route[2]
        metric = route[0]
        if routeChangeFlag == True and metric == 16:
            invalidRoutes[entryID] = route
    return invalidRoutes


# ---- TESTING BASE FUNCTIONALITY ----
# router1 = Router([0, [701, 702, 777], [[5000, 1, 1], [5002, 5, 4]], [30, 180, 240]])
# ComputeRoutingAlgorithm(router1, 1, [[1, 0], [3, 3]])
# ComputeRoutingAlgorithm(router1, 4, [[4, 0], [3, 2]])
# router1.PrintParams()
# response = GenerateResponse(router1)
# print(ReadResponse(response))
