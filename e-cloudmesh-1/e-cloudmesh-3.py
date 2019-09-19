# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:42:12 2019

@author: Siddhesh
"""

from cloudmesh.common.FlatDict import FlatDict

data = { 
        "name" : "Siddhesh",
        "address" : {
                    "city" : "Bloomington",
                    "state" : "Indiana"
                    }
        }
        
data = FlatDict(data)

print("Using FlatDict")
print(data)
