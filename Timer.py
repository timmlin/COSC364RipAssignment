# Timer file, handles all timer related events.
#Tim Lindbom & Benjamin Ireland 
#23/2/23

import threading 
import random
from Router import *
from ResponseHandler import *

# TEST IMPORTS
#from BellmanFordAlgorithm import *

def ResponseTimer(router):
    """Initialises and runs the response timer for a specified router"""
    random.seed()
    responseVal = router.timers[0]
    interval = random.randint(responseVal - 5, responseVal + 5)     # Uses the user specified timer value adding +- 5 seconds timer randomness as specified in RIP spec
    print(interval)
    SendResponses(router)       # Sends Responses to neighbours and then starts the timer
    threading.Timer(interval, ResponseTimer, [router]).start()



def InitTimeout(router, entryID):
    """Initialse the timeout timer"""
    timeoutVal = router.timers[1]
    timeoutTimer = threading.Timer(timeoutVal, InitGarbageColector, [router, entryID])
    timeoutTimer.start()
    return timeoutTimer



def ResetTimeout(router, entryID):
    """Resets the Timeout timer for a route"""
    timeoutTimer = router.routingTable.get(entryID)[3][0]
    timeoutTimer.cancel()
    return InitTimeout(router, entryID)



def InitGarbageColector(router, entryID):
    """Initialises the garbage collector timer and processes the timeout"""
    garbageCollectionVal = router.timers[2]
    garbageCollectionTimer = threading.Timer(garbageCollectionVal, DeleteRoute, [router, entryID])
    garbageCollectionTimer.start()
    return garbageCollectionTimer



def DeleteRoute(router, entryID):
    """Deletes the route from the routers routing table""" 
    del router.routingTable[entryID]            # Might make redundent due to minimal amount of lines

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