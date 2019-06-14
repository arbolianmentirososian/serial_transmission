import aiohttp
import asyncio
import certifi
import ssl
import requests

url = "http://192.168.29.27:8086/query?db=vDCMdb&&pretty=true --data-urlencode q=SELECT * FROM \"DVBS2\" WHERE " \
     "(\"host\" = 'DCM_192_168_29_57' AND \"board\" = '4' AND \"port\" = '3' AND \"type\" = 'CN_Margin') " \
     "AND \"time\" >=  now() - 10s order by desc limit"


#url2 = 'https://192.168.20.70:3000/api/datasources/proxy/10/query?db=vDCMdb&q=SELECT mean(\"value\") FROM \"DVBS2\" WHERE (\"host\" = \'DCM_192_168_29_57\' AND \"board\" = \'4\' AND \"port\" = \'3\' AND \"type\" = \'CN_Margin\') AND time >= now() - 10s GROUP BY time(100ms) fill(null)&epoch=ms'
url2 = 'https://192.168.20.70:3000/api/datasources/proxy/10/query?db=vDCMdb&q=SELECT mean(\"value\") FROM \"DVBS2\" WHERE (\"host\" = \'DCM_192_168_29_57\' AND \"board\" = \'4\' AND \"port\" = \'3\' AND \"type\" = \'CN_Margin\')' 

url3 = 'http://192.168.29.27:8086/query?db=vDCMdb --data-urlencode \"q=SELECT * FROM \"DVBS2\" WHERE (\"host\" = \'DCM_192_168_29_57\' AND \"board\" = \'1\' AND \"port\" = \'3\' AND \"type\" = \'CN_Margin\') AND \"time\" >=  now() - 10s order by desc limit 1" -H "Accept: application/json"'

url5 = 'http://192.168.29.27:8086/query?db=vDCMdb&q=SELECT * FROM \"DVBS2\" WHERE (\"host\" = \'DCM_192_168_29_57\' AND \"board\" = \'3\' AND \"port\" = \'0\' AND \"type\" = \'CN_Margin\') AND \"time\" >=  now() - 10s order by desc limit 1'

#params = {'db': 'vDCMdb', 'epoch' : 'ms', 'q' : 'SELECT mean("value") FROM "DVBS2" WHERE ("host" = 'DCM_192_168_29_57' AND "board" = \'4\' AND "port" = \'2\' AND "type" = \'CN_Margin\') AND time >= now() - 10s GROUP BY time(100ms) fill(null)'


async def start():
    #async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
    async with aiohttp.ClientSession() as session:

         #async with session.request('GET', url2) as resp:
          async with session.get(url5) as resp:
             print(resp.status)
             x = await resp.json()
             print(x['results'][0]['series'][0]['values'][0][5])
             
		


loop = asyncio.get_event_loop()
loop.run_until_complete(start())

#r = requests.get('https://192.168.20.70:3000')
#print(r.status_code)
#print(r.text)
