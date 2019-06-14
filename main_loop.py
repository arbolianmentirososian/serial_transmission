import asyncio
import time

from timeit import default_timer as timer

from config import config_dict, url_dict
from data_read import DataRead
from serial_transmission import SerialTransmission


def mainloop():
    port_name = list(config_dict.values())[0]
    data = DataRead()
    transmit = SerialTransmission(port_name)
    #counter = 1
    #file_name = 'values.txt'
    #transmit.clear_file_content(file_name)

    while 1:
        #start = timer()
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(data.run(url_dict, 0.5))
        loop.run_until_complete(future)
        for key, value in sorted(data.responses.items()):
            transmit.send_data(key, value)
            #string = transmit.set_output_text(key, value)
            #print(string)
            #transmit.save_to_txt(file_name, string)
        #end = timer()
        #print(f"Iteration no: {counter}, time: {end - start}")
        #  counter += 1
        time.sleep(1)


if __name__ == '__main__':
    mainloop()
