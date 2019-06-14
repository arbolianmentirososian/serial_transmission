# ---------------------------------------------------------------------------------------------------------------
# this file keeps configuration steps                                                                            |
# 'config_dict' is a dictionary keeping configuration of serial port name;                                       |
# to change serial port that is used for transmission                                                            |
# you only need to change the value of this dictionary to port which will be used to serial transmission         |
# Windows ports: 'COMX' where X is positive integer, Linux format: '/dev/ttyX', where X is positive integer      |
# ---------------------------------------------------------------------------------------------------------------
# 'url_dict' is a dictionary mapping transponder names [from 1 to 6 and A to D] to URLs where EB/N0 value from
# those transponder can be downloaded
# ---------------------------------------------------------------------------------------------------------------

config_dict = {"port_name": "COM1"}     # for Windows tests
# config_dict = {"port_name": "/dev/tty2"} # check if this port is correct on Raspberry Pi

url_dict = {'1': 'http://192.168.29.27:8086/query?db=vDCMdb&q=SELECT * FROM \"DVBS2\" WHERE (\"host\" = \'DCM_192_168_29_57\' AND \"board\" = \'4\' AND \"port\" = \'0\' AND \"type\" = \'CN_Margin\') AND \"time\" >=  now() - 10s order by desc limit 1',
            'B': 'http://192.168.29.27:8086/query?db=vDCMdb&q=SELECT * FROM \"DVBS2\" WHERE (\"host\" = \'DCM_192_168_29_57\' AND \"board\" = \'4\' AND \"port\" = \'2\' AND \"type\" = \'CN_Margin\') AND \"time\" >=  now() - 10s order by desc limit 1',
            '5': 'http://192.168.29.27:8086/query?db=vDCMdb&q=SELECT * FROM \"DVBS2\" WHERE (\"host\" = \'DCM_192_168_29_57\' AND \"board\" = \'4\' AND \"port\" = \'1\' AND \"type\" = \'CN_Margin\') AND \"time\" >=  now() - 10s order by desc limit 1',
            '4': 'http://192.168.29.27:8086/query?db=vDCMdb&q=SELECT * FROM \"DVBS2\" WHERE (\"host\" = \'DCM_192_168_29_57\' AND \"board\" = \'4\' AND \"port\" = \'3\' AND \"type\" = \'CN_Margin\') AND \"time\" >=  now() - 10s order by desc limit 1',
            '3': 'http://192.168.29.27:8086/query?db=vDCMdb&q=SELECT * FROM \"DVBS2\" WHERE (\"host\" = \'DCM_192_168_29_58\' AND \"board\" = \'4\' AND \"port\" = \'0\' AND \"type\" = \'CN_Margin\') AND \"time\" >=  now() - 10s order by desc limit 1',
            '2': 'http://192.168.29.27:8086/query?db=vDCMdb&q=SELECT * FROM \"DVBS2\" WHERE (\"host\" = \'DCM_192_168_29_58\' AND \"board\" = \'4\' AND \"port\" = \'1\' AND \"type\" = \'CN_Margin\') AND \"time\" >=  now() - 10s order by desc limit 1',
            '6': 'http://192.168.29.27:8086/query?db=vDCMdb&q=SELECT * FROM \"DVBS2\" WHERE (\"host\" = \'DCM_192_168_29_58\' AND \"board\" = \'4\' AND \"port\" = \'2\' AND \"type\" = \'CN_Margin\') AND \"time\" >=  now() - 10s order by desc limit 1',
            'C': 'http://192.168.29.27:8086/query?db=vDCMdb&q=SELECT * FROM \"DVBS2\" WHERE (\"host\" = \'DCM_192_168_29_58\' AND \"board\" = \'4\' AND \"port\" = \'3\' AND \"type\" = \'CN_Margin\') AND \"time\" >=  now() - 10s order by desc limit 1',
            }

