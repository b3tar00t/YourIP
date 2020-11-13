print("\033[1;36;40m*******************")

print("\034[1;36;40m*******************")

print(" KNOW YOUR IP TOOL BY b3ta_r00t")

print(" Instagram : b3ta_r00t ")

print("\033[1;36;40m*******************")

print("\033[1;36;40m*******************")

#!/usr/bin/python

import requests

url = 'http://api.ipify.org/'

response = requests.get(url)

ip=response.text

print("\033[1;32;40mYour IP Address is :" + ip)
