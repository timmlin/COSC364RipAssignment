#Main RIP protocol file
#Tim Lindbom & Ben Ireland
#8/3/23

import routerConfig
from Router import *
from select import select
import sys

def main():
    routers = routerConfig.readFile(sys.argv[1])
    routersList = []
    
    #initialises a router class for each router in the file 
    for strRouter in routers:
        currentRouter = routerConfig.getInfo(strRouter)
        routersList.append(Router(currentRouter))

    for router in routersList:
        router.OpenSockets()
        router.PrintParams()


    #enter the programs main infinite loop
    while(1):
        for router in routersList:
            readSockets, writeSockets, null = select([router.sockets],[],[])
            






if __name__ == "__main__":

    main()


