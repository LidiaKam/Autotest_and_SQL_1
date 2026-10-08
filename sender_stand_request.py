import requests
import configuration
import data

def create_orders(body):
    res = requests.post(configuration.URL_SERVICE + configuration.URL_CREATE_ORDERS,
                         headers = data.headers,
                         json = body)

    result = res.json()
    return result["track"]

def get_orders_track(track):
    return requests.get(configuration.URL_SERVICE+configuration.URL_GET_ORDERS_TRACK+"?t="+str(track),
                       headers=data.headers)
     