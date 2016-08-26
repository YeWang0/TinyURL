from pymongo import MongoClient
from hashDict import NumDict
import json
from hash import Long2Short
from hash import Short2Long
def storeUrl(url):
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
            return False
    index=db.url_convert.count()+1
    ShortUrl=Long2Short(index,len(NumDict.keys()),NumDict)
    result={'index':index,'actual_url':url,'shorten_url':ShortUrl}
    print result
    urls.insert_one(result)

storeUrl('https://leetcode.com/problemset/algorithms')



