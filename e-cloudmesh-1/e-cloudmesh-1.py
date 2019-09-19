# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:37:50 2019

@author: Siddhesh
"""

from cloudmesh.common.console import Console
from cloudmesh.common.variables import Variables
from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE

msg = "Hello World!"
variables = Variables()

print("")
Console.ok(msg)
print("")
Console.error(msg)
print("")
Console.msg(msg)
print("")
Console.error(msg, prefix = True, traceflag = True)

variables['debug'] = True
variables['trace'] = True
variables['verbose'] = 10

print("Using Banner")
banner("Hello World!")

print("Using Heading")
class example(object):
    def doit(self):
        HEADING()
        print("Hello World!")
        
    doit("Hello World!")

print("Verbose")    
d = {"sample" : "value"}
VERBOSE(d)