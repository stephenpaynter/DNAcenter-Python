import requests
import json

from pprint import pprint

base_url = 'https://sandboxdnac.cisco.com/dna/'
auth_endpoint = 'system/api/v1/auth/token'

user = 'devnetuser'
password = 'Cisco123!'

auth_response = requests.post(url=f"{base_url}{auth_endpoint}", auth=(user,password)).json()

token = auth_response['Token']

headers = {
    "x-auth-token":token,
    "Accept":"application/json",
    "Content-Type":"application/json"
}

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

payload = None

inv_response = requests.request('GET', url, headers=headers, data = payload)

pprint(inv_response.text)
