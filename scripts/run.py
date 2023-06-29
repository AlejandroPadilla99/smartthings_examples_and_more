"""
Author: Padilla Flores Alejandro
Description: the idea is to ""compile"" after to update a edge driver a run the logs to check errors
"""


import os

data = {
    "id_driver": '',
    "id_channel": '',
    "id_hub": '',
    "ip_hub": 'xxx.xxx.xx.xx'
}

os.system('smartthings edge:drivers:package')
os.system(f'smartthings edge:channels:assign {data["id_driver"]} -C {data["id_channel"]}')
os.system(f'smartthings edge:drivers:install {data["id_driver"]} -C {data["id_channel"]} -H {data["id_hub"]}')
os.system(f'smartthings edge:drivers:logcat {data["id_driver"]} --hub-address={data["ip_hub"]}')