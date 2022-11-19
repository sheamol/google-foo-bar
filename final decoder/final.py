# requires python 3+
import base64
from itertools import cycle

message = """
FEUWEQIQDRYSSk9WT0UCFgQSHEJNTUgPAA4JAQAUHQBGTVVMSAcWEAQWBQAFSkNMSAcDAg4BHBZG
TVVMSAsLBxMWDAwDAQpLQ0JCBQIbAQAXCAIJARZCRFtTTxAPAQAPBAcBQ01TTxcADw0FGxFCRFtT TxYACwpLQ0JCAg4cT0VbTUgbBgxEQxw=
"""

key = bytes("obedasheamol", "utf-8")
code = bytes(a ^ b for a, b in zip(base64.b64decode(message), cycle(key)))
res = eval(code.decode("utf-8"))

[print(key, ':', value) for key, value in res.items()]
