from StoreUrls import storeUrl
from pymongo import MongoClient

def ConvertUrl(url):
    storeUrl(url)
    poss=''
    if url[-1]=='/':
        poss=url[:len(url)-1]
    else:
        poss=url+'/'
    client = MongoClient()
    db = client.tinyurl
    urls=db.url_convert
    for i in urls.find():
        if url==i['actual_url'] or poss==i['actual_url'] :
            return i['shorten_url']

    return None

print ConvertUrl('https://leetcode.com/problemset/algorithms')