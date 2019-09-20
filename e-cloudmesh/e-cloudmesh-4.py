# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:53:19 2019

@author: Siddhesh
"""

from cloudmesh.common.Shell import Shell

result = Shell.execute('pwd')
print(result)

result = Shell.execute('ls', ["-l", "-a"])
print(result)

result = Shell.execute('ls', "-l -a")
print(result)

result = Shell.ls("-aux")
print(result)

result = Shell.ls("-a","-u","-x")
print(result)

result = Shell.pwd()
print(result)