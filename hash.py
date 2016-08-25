from hashDict import NumDict

def hash(id,base,NumDict):
    res=''
    while id>0:
        t=id%base
        res+=NumDict[t]
        id=id/base
    while len(res)<6:
        res+='0'
    return res[::-1]

print hash(123123123291238928912312918,62,NumDict)

def reverseHash(shortUrl,base,NumDict):
    res=0
    for i in xrange(len(shortUrl)):
        for k,v in NumDict.iteritems():
            if v==shortUrl[i]:
                res=res*base+k
                break
    return res

print reverseHash('9VwINrlQtai1kc6',62,NumDict)==123123123291238928912312918