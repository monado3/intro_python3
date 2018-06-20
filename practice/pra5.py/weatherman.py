import report as wr

description=wr.get_description()
print("Today's weather:", description)

from report import get_description as do
description=do()
print("Tomorrow's weather:", description)
