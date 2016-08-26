from hashDict import NumDict

def Long2Short(id,base,NumDict):
    res=''
    while id>0:
        t=id%base
        res+=NumDict[t]
        id=id/base
    while len(res)<6:
        res+='0'
    return res[::-1]

# print Long2Short(123123123291238928912312918,62,NumDict)

def Short2Long(shortUrl,base,NumDict):
    res=0
    for i in xrange(len(shortUrl)):
        for k,v in NumDict.iteritems():
            if v==shortUrl[i]:
                res=res*base+k
                break
    return res

# print Short2Long('9VwINrlQtai1kc6',62,NumDict)==123123123291238928912312918