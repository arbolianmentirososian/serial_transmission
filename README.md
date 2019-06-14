This is a project written in Python for displaying C/N margin values in digital displays in master control room.
There's a class responsible for retrieving C/N margin values from database. It uses asyncio and aiohttp libraries for making asynchronous requests. Another class is responsible for sending values over serial (RS-233).
