# Timer file, handles all timer related events.
#Tim Lindbom & Benjamin Ireland 
#23/2/23

import time
from threading import Timer
import random
from Router import *
from ResponseHandler import *

def InitResponseTimer(router):
    """Initialises the response timer for a specified router """
    random.seed()
    responseTimer = router.timers[0]
    interval = random.randint(responseTimer - 5, responseTimer + 5)
    Timer(interval, SendResponses(router)).start()