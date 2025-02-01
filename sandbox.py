import datetime
import json

print(datetime.datetime.today())
print(datetime.datetime.today().time())

key1 = "test_key"
value1 = 69
key2 = "test_key2"
value2 = 70
key_values = {key1: 69, key2: 70}
print(json.dumps(key_values))