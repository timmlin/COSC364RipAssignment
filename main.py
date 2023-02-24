from routerConfig import *


def main():
    config = readFile("Routers.txt")
    for router in config:
        getInfo(router)

main()
