"""
Pinterest reverse image search API used here
"""

import requests
import json

PINTEREST_API_GET = '''\
https://api.pinterest.com/v3/visual_search/flashlight/url/?\
url={}\
&x=0&y=0\
&w=1&h=1\
&base_scheme=https\
'''

def get_resp(img_url):
    '''
    Just the response from the API
    '''
    resp_ = requests.get(PINTEREST_API_GET.format(img_url)).json()

    # print(resp_)

    return resp_

if __name__ == "__main__":
    # print(
    get_resp("https://res.cloudinary.com/rootworld/image/upload/v1542648184/luffycuteandstuff.jpg")