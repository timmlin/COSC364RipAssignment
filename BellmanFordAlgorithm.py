#Bellman Ford Algorithm for use in a RIP routing protocol
#Tim Lindbom & Ben Ireland 
#23/2/23


def ComputeRoutingAlgorithm(hostRouter, peerRouterID, peerRouterEntries):
    """Computes RIP routing algorithm and updates the routing table"""
    for entry in peerRouterEntries: 
        # Match the Peer Router ID to one of the IDs in the output list to get the cost of the link 
        for output in hostRouter.outputList:
            outputRouterID = output[2] 
            outputCost = output[1]
            if outputRouterID == peerRouterID:
                linkCost = outputCost
        entryMetric = entry[1]
        metric = min(entryMetric + linkCost, 16)

        entryID = entry[0]
        if entryID not in hostRouter.routingTable:     #Checks if router is in the table. If not add the router to table.
            AddNewRoute(hostRouter, peerRouterID, entryID, metric)
        else:
            UpdateRoute(hostRouter, peerRouterID, entryID, metric)

            

def AddNewRoute(hostRouter, peerRouterID, entryID, metric):
    """Adds a new route to the routing table if the entry does not exist"""
    if metric <= 16:
        routeChangeFlag = True
        hostRouter.routingTable[entryID] = [metric, peerRouterID, routeChangeFlag]
        InitRouteTimers() # yet to be implemented

def UpdateRoute(hostRouter, peerRouterID, entryID, metric):
    """Updates the current route if ir has been changed and resets timers."""