
#   ResponseHandler
# ---- TESTING BASE FUNCTIONALITY ----
# router1 = Router([0, [701, 702, 777], [[5000, 1, 1], [5002, 5, 4]], [30, 180, 240]])
# ComputeRoutingAlgorithm(router1, 1, [[1, 0], [3, 3]])
# ComputeRoutingAlgorithm(router1, 4, [[4, 0], [3, 2]])
# router1.PrintParams()
# response = GenerateResponse(router1)
# print(ReadResponse(response))

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