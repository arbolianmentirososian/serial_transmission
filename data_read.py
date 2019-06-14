# ---------------------------------------------------------------------------------------------------
# This class is used to get data from server and return values that are ready to send over serial.  |
# ---------------------------------------------------------------------------------------------------
import asyncio
import logging
import random
import aiohttp

from aiohttp import ClientSession
from aiohttp import ClientError


class DataRead(object):
    # -----------------------------------------------------------------------------------------------------------------
    # This dictionary keeps values of EB/N0 of each transponder in unsorted order, for example: 'A': '11.5'            |
    # It can be considered as map of transponder_name: EB/N0 values                                                    |
    # -----------------------------------------------------------------------------------------------------------------
    responses = {}

    # -----------------------------------------------------------------------------------------------------------------
    # This method does 2 things: connects to server and gets data, that are parsed over another, auxiliary method      |
    # and adds values of EB/N0 to the responses dictionary in order as it gets responses from server (unsorted)        |
    # as input parameters this method gets transponder name (to set this name in response dictionary), url (to connect |
    # there to fetch data) and session                                                                                 |
    # -----------------------------------------------------------------------------------------------------------------
    async def fetch(self, transponder, url, session):
        try:
            async with session.get(url) as response:
                resp = await response.json()
                margin = self.get_margin(resp)
                self.responses[transponder] = margin
        except ClientError:
            logging.error("Couldn't get data from server, check your network connection")
            self.responses[transponder] = 0.0
        except asyncio.TimeoutError:
            logging.error("Couldn't get data from server, check your network connection")
            self.responses[transponder] = 0.0

    # -----------------------------------------------------------------------------------------------------------------
    # This method is a heartbeat of getting data. It creates asynchronous request and manages them.                    |
    # To get data from server it calls 'fetch' method, here is only asynchronous part of this task                     |
    # -----------------------------------------------------------------------------------------------------------------
    async def run(self, url_file, timeout):
        tasks = []
        time = aiohttp.ClientTimeout(total=timeout)
        async with ClientSession(timeout=time) as session:
            for key, value in url_file.items():
                task = asyncio.create_task(self.fetch(key, value, session))
                tasks.append(task)
            await asyncio.gather(*tasks)


    # -----------------------------------------------------------------------------------------------------------------
    # This method is auxiliary and it's purpose is to show data stored in dictionary of responses. It had big meaning  |
    # in debugging and in final version it actually does nothing                                                       |
    # -----------------------------------------------------------------------------------------------------------------
    def show_values(self, json_fie):
        for x in json_fie.items():
            print(x)

    # -----------------------------------------------------------------------------------------------------------------
    # This method is used to get margin from server response. As input parameter it gets JSON file storing all data    |
    # incoming from server. It finds margin value, checks if this value is numeric and then it returns to main         |
    # function where it is used to be passed into response dictionary.                                                 |
    # -----------------------------------------------------------------------------------------------------------------
    def get_margin(self, json_file):
        try:
            margin = json_file['results'][0]['series'][0]['values'][0][5]
            #margin = round(random.uniform(float(json_file["results"][0]["series"][0]["values"][0][5] / 10000), 15.0), 1)
        except (ValueError, TypeError):
            logging.warning("Couldn't parse Eb/N0 value")
            margin = 0.0
        return margin
