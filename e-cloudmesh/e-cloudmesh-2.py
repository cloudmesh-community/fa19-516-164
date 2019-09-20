# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:36:43 2019

@author: Siddhesh
"""

from cloudmesh.common.dotdict import dotdict

data = { "name" : "Siddhesh"}
data = dotdict(data)

print("Using dotdict")
print(data.name)

if(data.name == "Siddhesh"):
    print("His Last Name Must Be Mirjankar")