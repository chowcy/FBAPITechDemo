import requests
import json
import sys

#Group ID for a sample group
FB_GROUP_ID = '1834901519863165'
# get access token from
# https://developers.facebook.com/tools/explorer"
#TODO fill in access token
#Access token needs permission: publish actions (set to public)
access_token = None
if access_token == None:
    access_token = raw_input("\nCopy and paste token from https://developers.facebook.com/tools/explorer\n>  ")

FB_BASEURL = "https://graph.facebook.com/v2.12/{}".format(FB_GROUP_ID)
CACHE_FNAME = 'cache.json'

#function that prints json nicely (for debugging only)
def pretty(obj):
    return json.dumps(obj, sort_keys = True, indent = 2)

# Building the Facebook parameters dictionary
url_params = {}
url_params["access_token"] = access_token
#post messages, likes, comments, subcomments, sublikes, submessages
url_params["fields"] = "message,from"
url_params['filter'] = 'stream'
url_params["limit"] = 200

#Get posts from the Facebook group
try:
    r = getWithCaching('{}/feed'.format(FB_BASEURL), params=url_params)
    fb_posts = json.loads(r)['data']
except:
    print('Failed to get data from group')
    sys.exit(0)


#Test posting to a Facebook Group
# r = requests.post('{}/feed'.format(FB_BASEURL), data={'message': 'Hello from Python File', 'access_token': access_token})
# print(r.status_code)

#Comment on posts that meet criteria
#for every post in the feed
for post in fb_posts:
    #check for 'message' key in post, which contains the text of the post
    if 'message' in post:
        #criteria for things in the message
        #dummy criteria below
        if 'Python' in post['message']:
            #get that post's ID
            ID = post['id']
            #post request to comment on that post
            #below request does not work because of api deprecation
            r = requests.post('{}/{}'.format(FB_BASEURL, ID), data={'message': 'commenting on all posts containing "Python"', 'access_token': access_token})
            print(r.status_code)
