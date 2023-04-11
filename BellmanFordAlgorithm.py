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

        #Checks if router is in the table. If not add the router to table.
        entryID = entry[0]
        if entryID not in hostRouter.routingTable:    
            AddNewRoute(hostRouter, peerRouterID, entryID, metric)
        else:
            UpdateRoute(hostRouter, peerRouterID, entryID, metric)

            

def AddNewRoute(hostRouter, peerRouterID, entryID, metric):
    """Adds a new route to the routing table if the entry does not exist"""
    if metric < 16:
        routeChangeFlag = 0
        timeoutTimer = InitTimeout(hostRouter, entryID)
        hostRouter.routingTable[entryID] = [metric, peerRouterID, routeChangeFlag, [timeoutTimer, None]]


def UpdateRoute(hostRouter, peerRouterID, entryID, newMetric):
    """Updates the current route if ir has been changed and resets timers."""
    currentNextHopID = hostRouter.routingTable.get(entryID)[1]
    currentMetric = hostRouter.routingTable.get(entryID)[0]
    timeoutTimer = ResetTimeout(hostRouter, entryID) 
    if currentNextHopID == peerRouterID:
        if newMetric >= 16:
            garbageColectionTimer = InitGarbageColector(hostRouter, entryID)
            ### BEGIN ROUTE TEARDOWN P24,25
        elif newMetric != currentMetric:
            hostRouter.routingTable[entryID] = [newMetric, currentNextHopID, 0, [timeoutTimer, None]]
    else:
        if newMetric < currentMetric:
            hostRouter.routingTable[entryID] = [newMetric, peerRouterID, 0]

# router_id 0, inputs 701 702 777, outputs 5000-1-1 5002-5-4
# router1 = Router([0, [701, 702, 777], [[5000, 1, 1], [5002, 5, 4]], [30, 180, 240]])
# ComputeRoutingAlgorithm(router1, 1, [[1, 0], [3, 3]])
# router1.PrintParams()
# ComputeRoutingAlgorithm(router1, 4, [[4, 0], [3, 2]])
# router1.PrintParams()

# UpdateRoute(router1, 4, 3, 1)
# router1.PrintParams()

