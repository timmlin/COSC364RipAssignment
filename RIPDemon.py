#Main RIP protocol file
#Tim Lindbom & Ben Ireland
#8/3/23

from Router import *
from ResponseHandler import *
from BellmanFordAlgorithm import *
from select import select
import sys, random, routerConfig, time

def GetResponseTime(router):
    """Initialise the response timer for a specified router"""
    responseVal = router.timers[0]
    interval = random.uniform(responseVal * 0.8, responseVal*1.2)     # Uses the user specified timer value adding +- randomness as specified in RIP spec
    return interval



def main():
    # Reads router config file and creates a router object
    routerFile = routerConfig.readFile(sys.argv[1])
    routerInfo = routerConfig.getInfo(routerFile)   #Might rewrite
    router = Router(routerInfo)
    # Opens the  all Sockets
    router.OpenSockets()
    router.PrintTable()

    # Set up response timer 
    responsePeriod = GetResponseTime(router)  
    sysTime = time.time()
    responseTimer = responsePeriod  + sysTime

    # Enter the main program loop
    while 1:

        sysTime = time.time()
        if sysTime >= responseTimer:
            responsePeriod = GetResponseTime(router)
            responseTimer = responsePeriod  + sysTime
            SendResponses(router)
        else:
            # Wait for response messages to arrive 
            printTable = False
            readSockets, writeSockets, null = select(router.sockets,[],[], router.timers[0])
            if len(readSockets) != 0 :
                for soc in readSockets:
                    try:
                        response, addr = soc.recvfrom(504)
                    except ConnectionResetError:
                        continue
                    
                    headerInfo, peerRouterEntries = ReadResponse(response)

                    peerRouterID = headerInfo[2]

                    ComputeRoutingAlgorithm(router, peerRouterID, peerRouterEntries)

                    # Check if there has been a change to the routes
                    for route in router.routingTable.values():
                        routeChangeFlag = route[2]
                        if routeChangeFlag == 1:
                            printTable = True
                    
                    CheckTimers(router)

            if printTable == True:
                router.PrintTable()

            






if __name__ == "__main__":

    main()


