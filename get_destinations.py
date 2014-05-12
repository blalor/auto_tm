#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import plistlib
import subprocess
import os
import sys


destinations = plistlib.readPlistFromString(
    subprocess.check_output(["tmutil", "destinationinfo", "-X"])
)["Destinations"]

availableDestinations = []

for destination in destinations:
    if destination["Kind"] == "Local":
        if os.path.exists("/Volumes/" + destination["Name"]):
            availableDestinations.append(destination)

if not availableDestinations:
    sys.exit(1)
else:
    if len(availableDestinations) > 1:
        ## multiple destinations mounted.  if one of them is the
        ## LastDestination, use it, otherwise use the first.
        lastDestination = [d for d in availableDestinations if d["LastDestination"] == 1]
        
        if lastDestination:
            print "/Volumes/" + lastDestination[0]["Name"]
        else:
            print "/Volumes/" + availableDestinations[0]["Name"]
    else:
        print "/Volumes/" + availableDestinations[0]["Name"]
