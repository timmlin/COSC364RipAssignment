#Generates and processes RIP Response packets
#Tim Lindbom & Benjamin Ireland 
#23/2/23
import Router

def GenerateResponse(router):
    """Generates response packet to be sent to other routers"""
    response = bytearray(4)
    response[0] = 2 # Indicating response message
    response[1] = 2 # Version 2
    response[3] = router.id >> 4
    response[4] = router.id & 0xF #Router ID
    for route in router.routingTable:
        RTE = bytearray(20)
        