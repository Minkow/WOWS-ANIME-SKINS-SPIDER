import urllib.request
import re
import os
import random
import socket
import time

pattern = 'down:<a href="(.*)" rel'
pattern0 = 'kNO = "(.*)"'

dlist = []
plist = []


useragent = [
    "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
    "Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
    "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
    "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)"
]

header={
    "User-Agent":random.choice(useragent)
}

for i in range(1,121):
    print('now ' + str(i))
    url = 'https://forum.worldofwarships.com/topic/18357-skin-bottom-sound-wows-skin-share-discussion/?page=' + str(i)
    req = urllib.request.Request(url,headers = header)
    html = urllib.request.urlopen(req)
    doc = html.read().decode('utf8')
    html.close()
    url_list = list(set(re.findall(pattern, doc)))
    dlist += url_list

# for i in dlist:
#     req = urllib.request.Request(i,headers = header)
#     html = urllib.request.urlopen(req)
#     doc = html.read().decode('utf8')
#     html.close()
#     urlnow = re.findall(pattern0, doc)
#     plist += urlnow
#     time.sleep(5)

fp = open('skins1.txt','w')
for i in dlist:
    print(i)
    fp.write(i + '\n')
fp.close()