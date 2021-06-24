"""

"""
import math
import os
import datetime
import sys
from random import random
import requests
#
# num1 = 23.44
#
# print(math.ceil(num1))  # .ceil() round up
# print(math.floor(num1))  # round down
# print(math.pi)
#
# print(random())  # generate random number between 0.0 to 0.9
#
# work_dir = os.getcwd()
# print(work_dir)
#
# print(os.cpu_count())
# print(os.getuid())
# print(os.uname())
#
# print(datetime.date.today())
# print(sys.path)

# import requests: a package to interact with a live API
# we can make api call to any web addre

requests_api = requests.get("https://www.bbc.co.uk/")

print(requests_api.status_code)
print(requests_api.headers)
print(requests_api.content)

