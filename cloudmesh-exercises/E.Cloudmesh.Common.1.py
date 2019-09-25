# E.Cloudmesh.Common.1

## Develop a program that demonstartes the use of banner, HEADING, and VERBOSE.

from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE

## Defining variables

Text1 = "Jagadeesh First heading Test"

## Demonstrated use of banner
banner(Text1, "*", color="BLUE")

## Demonstrated use of HEADING

Text2 = "Jagadeesh First Banner Test"

HEADING(Text2)

## Demonstrated use of VERBIOSE
verboseData = {"Text1": Text1, "Text2": Text2}

VERBOSE(verboseData)

