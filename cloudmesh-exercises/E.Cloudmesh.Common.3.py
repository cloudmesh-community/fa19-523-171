# E.Cloudmesh.Common.3

## Develop a program that demonstartes the use of Flatdict


# E.Cloudmesh.Common.3

## Develop a program that demonstartes the use of FlatDict


from cloudmesh.common.FlatDict import FlatDict

Jagadeesh =  { "Name" : "Jagadeesh",
              "Class" : {
              "Course" : "CloudComputing",
              "Instructor" : "Gregor"
              }

              }

Jagadeesh = FlatDict(Jagadeesh)

print(Jagadeesh['Class__Course'])


