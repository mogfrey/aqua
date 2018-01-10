import time
from w1thermsensor import w1thermsensor
from array import *
import datetime
import json

sensor = w1Thermsensor()
now = datetime.datetime.now()

def get_temps():
    While True:
        data = []
        temperature = (sensor.get_temperature())
        data.append({
            'temp':temperature,
            'date':now
        })

        print json.dumps(data)
        time.sleep(1)
