import requests
from prometheus_client import CollectorRegistry, Gauge
from prometheus_client import push_to_gateway
import time
import random

from prometheus_client.exposition import basic_auth_handler

def my_auth_handler(url, method, timeout, headers, data):
    username = 'admin'
    password = 'admin'
    return basic_auth_handler(url, method, timeout, headers, data, username, password)

HOURLY_RED_HAT = "https://api.openweathermap.org/data/2.5/onecall?lat=59.4717&lon=24.4580&appid=b6187994e3efa0cf3bab314f7e457dfc"
def get_temperature():
    result = requests.get(HOURLY_RED_HAT)
    return round(result.json()["current"]["temp"] - 273.15)

def prometheus_temperature(num):
    registry = CollectorRegistry()
    g = Gauge("red_hat_temp", "Temperature at Red Hat HQ", registry=registry)
    g.set(num)
    return registry
def push_temperature(url):
    while True:
        temp = get_temperature()
        registry = prometheus_temperature(temp)
        #registry = prometheus_temperature(get_temperature())
        push_to_gateway(url, "temperature collector", registry, handler=my_auth_handler)
        print(temp)
        time.sleep(30)
        

urls="http://localhost:9091"
push_temperature(urls)