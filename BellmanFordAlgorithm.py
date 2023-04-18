#Bellman Ford Algorithm for use in a RIP routing protocol
#Tim Lindbom & Benjamin Ireland 
#23/2/23
from Router import *
from Timer import *


def ComputeRoutingAlgorithm(hostRouter, peerRouterID, peerRouterEntries):
    """Computes RIP routing algorithm and updates the routing table"""
    for entry in peerRouterEntries: 
        # Match the Peer Router ID to one of the IDs in the output list to get the cost of the link 
        
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
        hostRouter.routingTable[entryID] = [metric, peerRouterID, 1, [None, None]]
        InitTimeout(hostRouter, entryID)


def UpdateRoute(hostRouter, peerRouterID, entryID, newMetric):
    """Updates the current route if it has been changed and resets timers."""
    currentNextHopID = hostRouter.routingTable.get(entryID)[1]
    currentMetric = hostRouter.routingTable.get(entryID)[0]

    # Check if the router the update is coming from is the same router as in routing table
    if currentNextHopID == peerRouterID:
        # If the metric is greater infinity we start the Timeout process
        if newMetric >= 16:
            if currentMetric != newMetric:
                Timeout(hostRouter, entryID)
                SendResponses(hostRouter, True)
        elif newMetric != currentMetric:
            hostRouter.routingTable[entryID] = [newMetric, currentNextHopID, 1, [None, None]]
            InitTimeout(hostRouter, entryID)
        elif newMetric == currentMetric:
            hostRouter.routingTable[entryID][2] = 0
            InitTimeout(hostRouter, entryID)
    else:
        if newMetric < currentMetric:
            hostRouter.routingTable[entryID] = [newMetric, peerRouterID, 1, [None, None]]
            InitTimeout(hostRouter, entryID)




