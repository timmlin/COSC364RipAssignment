# Timer file, handles all timer related events.
#Tim Lindbom & Benjamin Ireland 
#23/2/23

import random
import time

from ResponseHandler import *
from Router import *


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
                SendResponses(router, True)

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

  
