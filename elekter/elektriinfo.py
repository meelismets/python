from urllib.request import urlopen
from json import loads
from datetime import datetime
from datetime import timedelta

datetime.now().isoformat()

start = datetime.now()
end = start + timedelta(hours=1) + timedelta(seconds=30)
url = "https://dashboard.elering.ee/api/nps/price?start="+start.isoformat()+"Z&end="+end.isoformat()+"Z"
print(url)

elektriInfoInternetist = urlopen(url)
baidid = elektriInfoInternetist.read()
massiiv = loads(baidid)
elektriInfoInternetist.close()
print(massiiv["data"]["ee"][0]["price"])