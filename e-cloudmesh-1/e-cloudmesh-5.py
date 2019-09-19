# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:59:02 2019

@author: Siddhesh
"""

from cloudmesh.common.StopWatch import StopWatch
import time

StopWatch.start("test")
time.sleep(2)
StopWatch.stop("test")

print(StopWatch.get("test"))
