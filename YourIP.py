print(" *******************")

print(" *******************")

print(" KNOW YOUR IP TOOL BY b3ta_r00t")

print(" Instagram : b3ta_r00t ")

print(" *******************")

print(" *******************")

#!/usr/bin/python

import requests

url = 'http://api.ipify.org/'

response = requests.get(url)

ip=response.text

print("Your IP Address is :" + ip)
