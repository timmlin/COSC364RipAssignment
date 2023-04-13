# Timer file, handles all timer related events.
#Tim Lindbom & Benjamin Ireland 
#23/2/23

import time 
import random
from Router import *
from ResponseHandler import *

# TEST IMPORTS
#from BellmanFordAlgorithm import *




def GetResponseTime(router):
    """Initialise the response timer for a specified router"""
    responseVal = router.timers[0]
    interval = random.uniform(responseVal * 0.8, responseVal*1.2)     # Uses the user specified timer value adding +- randomness as specified in RIP spec
    return interval


def CheckTimers(router):
    """Used to check route timers, if there is a timeout the grabage collector will be started for that route.
    If the Garbage Collector expires the route is deleted"""

    # Keep track of all routes that need to be deleted
    garbageRoutes = []

    for entry, route in router.routingTable.items():
        systemTime = time.time()
        timeoutTime = route[3][0]
        garbageColTime = route[3][1]

        # If the timeout is reset while the garbage colector is running we clear the garbage timer.
        if timeoutTime != None and garbageColTime != None:
            route[3][1] = None

        # Check if a timeout has occured
        elif timeoutTime != None and garbageColTime == None:
            if systemTime >=  timeoutTime:
                Timeout(router, entry)

        # Track any routes that have expired
        elif garbageColTime != None and timeoutTime == None:
            if systemTime >= garbageColTime:
               garbageRoutes.append(entry) 

    # Delete expired routes
    for garbageEntry in garbageRoutes:
        del router.routingTable[garbageEntry]



def InitTimeout(router, entryID):
    """Initialse the timeout timer"""
    timeoutVal = router.timers[1]
    timeoutTime = time.time() + timeoutVal
    router.routingTable[entryID][3][0] = timeoutTime



def Timeout(router, entryID):
    """Initialises the garbage collector timer and processes the timeout"""
    garbageCollectionVal = router.timers[2]
    garbageColTime = time.time() + garbageCollectionVal
    router.routingTable[entryID][3][1] = garbageColTime
    router.routingTable[entryID][3][0] = None
    router.routingTable[entryID][0] = 16
    router.routingTable[entryID][2] = 1

  

# # ---- TESTING SENDING FUNCTIONALITY ----
# router1 = Router([0, [701, 702, 777], [[5000, 1, 1], [5002, 5, 4]], [6, 180, 240]])
# router1.OpenSockets()
# ComputeRoutingAlgorithm(router1, 1, [[1, 0], [3, 3]])
# router1.PrintParams()

# ResponseTimer(router1)

# ComputeRoutingAlgorithm(router1, 4, [[4, 0], [3, 2]])
# router1.PrintParams()
# UpdateRoute(router1, 4, 3, 1)
# router1.PrintParams()
# response = GenerateResponse(router1)
# print(ReadResponse(response))

router1 = Router([0, [701, 702, 777], [[5000, 1, 1], [5002, 5, 4]], [3, 18, 12]])

print(GetResponseTime(router1))