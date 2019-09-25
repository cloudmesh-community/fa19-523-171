# E.Cloudmesh.Common.2

## Develop a program that demonstartes the use of dotdict


from cloudmesh.common.dotdict import dotdict
from pprint import pprint

Jagadeesh =  { "Name" : "Jagadeesh",
              "Class" : "Cloud Computing"
              }

Jagadeesh = dotdict(Jagadeesh)

pprint(Jagadeesh.Class)