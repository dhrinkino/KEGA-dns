# This program is part of KEGA project
# Made by Dominik Hrinkino

import socket
import time
import sys

# OPTIONS
HOSTNAME = 'kai.fpv.ucm.sk'
NUM_OF_REQUESTS = 10
DEFAULT_DELAY = 0.1
MIKROTIK_DELAY = 5
if __name__ == "__main__":

    times = []

    for i in range(NUM_OF_REQUESTS):
        # Measure dns response time
        t1 = time.time()
        socket.gethostbyname(HOSTNAME)
        t2 = time.time()
        times.append((t2 - t1) * 1000) # Calculate time and convert to milliseconds
        # since mikrotik don't have any settings to disable internal DNS cache, best practice to avoid caching is set
        # 1 second TTL in cache settings. Mikrotik adds overhead, entries in cache is aren't wiped exactly after one
        # second and are deleted after ≈5 seconds to enable 5 sec delay (this can be changed by constants),
        # it is required to use arg 'mikrotik' example ./SingleHostname.py mikrotik otherwise, DNS will send request
        # with 0.1 sec delay (also this can be changed via options).
        if len(sys.argv) == 2:
            if sys.argv[1] == 'mikrotik':
                time.sleep(MIKROTIK_DELAY)
        else:
            time.sleep(DEFAULT_DELAY)
    print(times) # output array of times
