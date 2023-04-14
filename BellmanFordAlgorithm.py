#Bellman Ford Algorithm for use in a RIP routing protocol
#Tim Lindbom & Benjamin Ireland 
#23/2/23
from Router import *
from Timer import *



def ComputeRoutingAlgorithm(hostRouter, peerRouterID, peerRouterEntries):
    """Computes RIP routing algorithm and updates the routing table"""
    for entry in peerRouterEntries: 
        # Match the Peer Router ID to one of the IDs in the output list to get the cost of the link 
        print(hostRouter.outputs)
        for output in hostRouter.outputs:
            outputRouterID = output[2] 
            outputCost = output[1]
            if outputRouterID == peerRouterID:
                linkCost = outputCost
        entryMetric = entry[1]
        metric = min(entryMetric + linkCost, 16)

        # Checks if router is in the table. If not add the router to table. Otherwise we update the route.
        entryID = entry[0]
        if entryID not in hostRouter.routingTable:    
            AddNewRoute(hostRouter, peerRouterID, entryID, metric)
        else:
            UpdateRoute(hostRouter, peerRouterID, entryID, metric)

            

def AddNewRoute(hostRouter, peerRouterID, entryID, metric):
    """Adds a new route to the routing table if the entry does not exist"""
    if metric < 16:
        # Adds the new router to the routing table and initialises the route timeout
        hostRouter.routingTable[entryID] = [metric, peerRouterID, 0, [None, None]]
        InitTimeout(hostRouter, entryID)


def UpdateRoute(hostRouter, peerRouterID, entryID, newMetric):
    """Updates the current route if it has been changed and resets timers."""
    currentNextHopID = hostRouter.routingTable.get(entryID)[1]
    currentMetric = hostRouter.routingTable.get(entryID)[0]

    # Check if the router the update is coming from is the same router as in routing table
    if currentNextHopID == peerRouterID:
        # If the metric is greater infinity we start the Timeout process
        if newMetric >= 16:
            Timeout(hostRouter, entryID)
        elif newMetric != currentMetric:
            hostRouter.routingTable[entryID] = [newMetric, currentNextHopID, 0, [None, None]]
            InitTimeout(hostRouter, entryID)
        else:
            InitTimeout(hostRouter, entryID)
    else:
        if newMetric < currentMetric:
            hostRouter.routingTable[entryID] = [newMetric, peerRouterID, 0, [None, None]]




# ---- TESTING ALGORITHM FUNCTIONALITY ----
# router_id 0, inputs 701 702 777, outputs 5000-1-1 5002-5-4
# router1 = Router([0, [701, 702, 777], [[5000, 1, 1], [5002, 5, 4]], [30, 180, 240]])
# ComputeRoutingAlgorithm(router1, 1, [[1, 0], [3, 3]])
# ComputeRoutingAlgorithm(router1, 4, [[4, 0], [3, 2]])
# UpdateRoute(router1, 4, 3, 1)
# router1.PrintParams()


# ---- TESTING TRIGGERED FUNCTIONALITY ----
# router1 = Router([0, [701, 702, 777], [[5000, 1, 1], [5002, 5, 4]], [30, 180, 240]])
# router1.OpenSockets()
# ComputeRoutingAlgorithm(router1, 4, [[4, 0], [3, 2]])
# ComputeRoutingAlgorithm(router1, 4, [[4, 0], [3, 16]])
# SendResponses(router1, True)

# ---- TESTING TIMER FUNCTIONALITY ----
# router1 = Router([0, [701, 702, 777], [[5000, 1, 1], [5002, 5, 4]], [3, 4, 3]])
# ComputeRoutingAlgorithm(router1, 1, [[1, 0], [3, 3]])
# ComputeRoutingAlgorithm(router1, 4, [[4, 0], [3, 2]])
# i = 0
# while(1):
#     CheckTimers(router1)
#     i += 1
#     if i == 1000000:
#         i = 0 
#         router1.PrintParams()

# ---- TESTING RESPONSE GENERATION AND READING ----
# router1 = Router([0, [701, 702, 777], [[5000, 1, 1], [5002, 5, 4]], [30, 180, 240]])
# ComputeRoutingAlgorithm(router1, 1, [[1, 0], [3, 3]])
# ComputeRoutingAlgorithm(router1, 4, [[4, 0], [3, 2]])
# router1.PrintParams()
# response = GenerateResponse(router1, 1)
# print(ReadResponse(response))