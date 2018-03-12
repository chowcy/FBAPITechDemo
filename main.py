import requests
import json
import sys

#Group ID for a sample group
FB_GROUP_ID = '1834901519863165'
# get access token from
# https://developers.facebook.com/tools/explorer"
#TODO fill in access token
#Access token needs permission: publish actions (set to public), user managed groups, user posts
access_token = None
if access_token == None:
    access_token = input("\nCopy and paste token from https://developers.facebook.com/tools/explorer\n>  ")

FB_BASEURL = "https://graph.facebook.com/v2.12/"

#function that prints json nicely (for debugging only)
def pretty(obj):
    return json.dumps(obj, sort_keys = True, indent = 2)

# Building the Facebook parameters dictionary for GET request
url_params = {}
url_params["access_token"] = access_token
#post messages, from
url_params["fields"] = "message,from"

# Building the Facebook parameters dictionary for POST request
data_params = {}
data_params["access_token"] = access_token
data_params["message"] = 'Hello from Python File'

#get feed information
r = requests.get('{}/{}/feed'.format(FB_BASEURL, FB_GROUP_ID), params=url_params)
print(pretty(json.loads(r.text)))
#Test posting to a Facebook Group
r = requests.post('{}/{}/feed'.format(FB_BASEURL, FB_GROUP_ID), data=data_params)
print(r.status_code)
#get feed information, see that a post was posted
r = requests.get('{}/{}/feed'.format(FB_BASEURL, FB_GROUP_ID), params=url_params)
print(pretty(json.loads(r.text)))
