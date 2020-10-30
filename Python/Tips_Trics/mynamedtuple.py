from collections import namedtuple
import json


Dynamo = namedtuple('Dynamo',["instancename","instancetype","instancesize"])

d1 = Dynamo("dinesh","ml.t3.medium",5)
print(d1)
print(d1._asdict())
print(type(d1._asdict()))
print(json.dumps(d1._asdict()))
