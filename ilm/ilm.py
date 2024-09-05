import xml.etree.ElementTree as ET
from urllib.request import urlopen

url = "https://www.ilmateenistus.ee/ilma_andmed/xml/observations.php"

xml_veebist = urlopen(url)
xml_baidid = xml_veebist.read()

sisu = ET.fromstring(xml_baidid)

jaamad = sisu.findall('station')
for jaam in jaamad:
    vaatlus_jaam = jaam.find('name').text
    temperatuur = str(jaam.find('airtemperature').text)
    tuulekiirus = str(jaam.find('windspeed').text)
    print(vaatlus_jaam + " vaatlusjaamas on " + temperatuur + " kraadi. Ning tuul puhub " + tuulekiirus + " m/s.")
