# E.Cloudmesh.Common.5

## Develop a program that demonstartes the use of StopWatch

from cloudmesh.common.StopWatch import StopWatch
import os


StopWatch.start("Program Starting")
os.times()

StopWatch.stop("Program Ending")

StopWatch.benchmark(sysinfo=True)


