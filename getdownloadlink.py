import urllib.request
import random
import re
import time

useragent = [
    "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
    "Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
    "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
    "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)"
]
fp0 = open('skins1.txt','r')
fp1 = open('skins.txt','a')
pattern = 'kNO = "(.*)"'
plist=[]
for i in fp0.readlines():
    i.strip()

    header={
        "User-Agent":random.choice(useragent)
    }


    url = i
    req = urllib.request.Request(url,headers = header)

    html = urllib.request.urlopen(req)
    doc = html.read().decode('utf8')
    html.close()
    urlnow = re.findall(pattern, doc)
    fp1.write(urlnow[0] + '\n')
    print(urlnow[0])
    fp1.flush()
    time.sleep(5)
    
fp1.close()