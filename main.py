import requests
import json
import sys

#Group ID for a sample group
FB_GROUP_ID = '1834901519863165'
# get access token from
# https://developers.facebook.com/tools/explorer"
#TODO fill in access token
#Access token needs permission: publish actions (set to public)
access_token = 'EAACEdEose0cBAPtKkpwg06r5htisBTFahIlTOD6AABl1lbi9rah33pcARLa6roTONi4wMvWZACgMIyvk7uU0LPdqfoBYC2VDddSsm6O46QAfbCj8TZC2VQ9jVopBZCZAmx4BhM6Bth1yagSOZAGk4Ys38zA86MyImq0Ljf77rjWFYepdtaWgUstDUFvZAcVLYZD'
if access_token == None:
    access_token = raw_input("\nCopy and paste token from https://developers.facebook.com/tools/explorer\n>  ")

FB_BASEURL = "https://graph.facebook.com/v2.12/{}".format(FB_GROUP_ID)
# CACHE_FNAME = 'cache.json'

#function that prints json nicely (for debugging only)
def pretty(obj):
    return json.dumps(obj, sort_keys = True, indent = 2)

# Building the Facebook parameters dictionary
url_params = {}
url_params["access_token"] = access_token
#post messages, from
url_params["fields"] = "message,from"

#get feed information
r = requests.get('{}/feed'.format(FB_BASEURL), params=url_params)
print(pretty(json.loads(r.text)))
#Test posting to a Facebook Group
r = requests.post('{}/feed'.format(FB_BASEURL), data={'message': 'Hello from Python File', 'access_token': access_token})
print(r.status_code)
r = requests.get('{}/feed'.format(FB_BASEURL), params=url_params)
print(pretty(json.loads(r.text)))
