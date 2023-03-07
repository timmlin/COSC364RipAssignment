#Main RIP protocol file
#Tim Lindbom & Ben Ireland
#8/3/23

import routerConfig
from router import *



def main():
    config = routerConfig.readFile("Routers.txt")
    defaultRouterName = "router"
    routersList = []
    #initilises a router class for each router in the file 
    for strRouter in config:

        currentRouter = routerConfig.getInfo(strRouter)
        routername = f"{defaultRouterName}{currentRouter[0]}"
        #print(routername, currentRouter)

        routersList.append(Router(currentRouter))
        

    for router in routersList:
        router.PrintParams()




if __name__ == "__main__":

    main()


