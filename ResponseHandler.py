#Generates and processes RIP Response packets
#Tim Lindbom & Benjamin Ireland 
#23/2/23
from Router import  *
import socket
from BellmanFordAlgorithm import *
import threading 
import random

def GenerateResponse(router):
    """Generates response packet to be sent to other routers"""
    response = bytearray(4)
    response[0] = 2 # Indicating response message
    response[1] = 2 # Version 2
    response[2] = router.id >> 8
    response[3] = router.id & 0xFF #Router ID
    for routerID, route in router.routingTable.items():  # Assuming routing table is of the format {Router ID: Metric, etc.} // NEED TO CHANGE TO DICTIONARY

        # will need to account for fact that message can only be max 504 bytes and MIN 24 bytes 
        # Also need to address the the Split-Horizon Poisoned Reverse
        # ie/ If a route is learned from that router set the metric to infinity
        # if router.id = learnedID or something along those lines
        
        RTE = bytearray(20)
        RTE[0] = 0x0
        RTE[1] = 0x0
        RTE[2] = 0x0
        RTE[3] = 0x0
        RTE[4] = 0x0
        RTE[5] = 0x0
        RTE[6] = routerID >> 8          # Add Router ID
        RTE[7] = routerID & 0xFF
        RTE[8] = 0x0
        RTE[9] = 0x0
        RTE[10] = 0x0
        RTE[11] = 0x0
        RTE[12] = 0x0
        RTE[13] = 0x0
        RTE[14] = 0x0
        RTE[15] = 0x0
        RTE[16] = 0x0
        RTE[17] = 0x0
        RTE[18] = route[0] & 0xFF00 # Add Metric to router
        RTE[19] = route[0] & 0xFF
        response =  response + RTE      # Add RTE onto the end of response message
    return response

def SendResponses(router):
    """Used to send a response message to a specified Port"""
    i = 0
    while i < len(router.outputs) - 1:   # Enter a loop cycling through the output list and sending each peer router their designated message
        port = router.outputs[i][0]
        soc = router.sockets[i]
        response = GenerateResponse(router)
        soc.sendto(response, (router.localIP, port))
        i += 1
    
    
           

def ReadResponse(response):
    """Used to unpack recieved response message to use in the Bellman Ford algorithm"""
    i = 0
    peerRouterEntries = []
    responseHeader = bytearray(response[:4]) # Will need to query to see why this was done previously
    entries = bytearray(response[4:])
    messageType = responseHeader[0]         # Gets the message, version, and router ID
    versionType = responseHeader[1]
    peerRouterID = responseHeader[2] << 8 | response[3]
    while i < len(entries) - 1:             # Adds each router entry into a list
        peerRouterEntries.append([entries[i + 6] << 8 | entries[i + 7], entries[i + 18] << 8 | entries[i + 19]])
        i += 20
    return [messageType, versionType, peerRouterID], peerRouterEntries

def ResponseTimer(router):
    """Initialises the response timer for a specified router """
    random.seed()
    responseTimer = router.timers[0]
    interval = random.randint(responseTimer - 5, responseTimer + 5)
    print(interval)
    SendResponses(router)
    threading.Timer(interval, ResponseTimer, [router]).start()

# ---- TESTING BASE FUNCTIONALITY ----
# router1 = Router([0, [701, 702, 777], [[5000, 1, 1], [5002, 5, 4]]])
# ComputeRoutingAlgorithm(router1, 1, [[1, 0], [3, 3]])
# router1.PrintParams()
# ComputeRoutingAlgorithm(router1, 4, [[4, 0], [3, 2]])
# router1.PrintParams()
# UpdateRoute(router1, 4, 3, 1)
# router1.PrintParams()
# response = GenerateResponse(router1)
# print(ReadResponse(response))

# ---- TESTING SENDING FUNCTIONALITY ----
router1 = Router([0, [701, 702, 777], [[5000, 1, 1], [5002, 5, 4]], [6, 180, 240]])
router1.OpenSockets()
ComputeRoutingAlgorithm(router1, 1, [[1, 0], [3, 3]])
router1.PrintParams()

ResponseTimer(router1)


ComputeRoutingAlgorithm(router1, 4, [[4, 0], [3, 2]])
router1.PrintParams()
UpdateRoute(router1, 4, 3, 1)
router1.PrintParams()
response = GenerateResponse(router1)
print(ReadResponse(response))