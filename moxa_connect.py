import requests
from requests import HTTPError
import json

MOXA_IP = "192.168.0.253"
status_URL = "http://" + MOXA_IP + "/api/slot/0/io/do"
# Prepare PUT headers.
getHeaders = {'Content-Type': 'application/json', 'Accept': 'vdn.dac.v1'}


def put_data(url=status_URL, headers=getHeaders, data=0):
    ramp_ON = {
                        "slot": 0,
                        "io": {
                            "do": [
                                {
                                    "doIndex": 0,
                                    "doMode": 0,
                                    "doStatus": 1
                                },
                                {
                                    "doIndex": 1,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 2,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 3,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 4,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 5,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 6,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 7,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 8,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 9,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 10,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 11,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 12,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 13,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 14,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 15,
                                    "doMode": 0,
                                    "doStatus": 0
                                }
                            ]
                        }
                        }
    ramp_OFF = {
                        "slot": 0,
                        "io": {
                            "do": [
                                {
                                    "doIndex": 0,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 1,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 2,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 3,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 4,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 5,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 6,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 7,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 8,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 9,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 10,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 11,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 12,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 13,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 14,
                                    "doMode": 0,
                                    "doStatus": 0
                                },
                                {
                                    "doIndex": 15,
                                    "doMode": 0,
                                    "doStatus": 0
                                }
                            ]
                        }
                        }
    ramp_ON = json.dumps(ramp_ON)
    ramp_OFF = json.dumps(ramp_OFF)
    putHeaders_do00Status = getHeaders.copy()
    putHeaders_do00Status['Content-Length'] = str(len(json.dumps(ramp_ON)))
    try:
        if data == 1:
            response = requests.put(url, headers=headers, data=ramp_ON)
            response.raise_for_status()
        else:
            response = requests.put(url, headers=headers, data=ramp_OFF)
            response.raise_for_status()
    except HTTPError as http_err:
        print("HTTP error occurred: %s" % http_err)
    except Exception as err:
        print("Other error occurred: %s" % err)
    else:
        if len(response.text) > 0:
            print("response.text:\n%s" % response.text)
        else:
            print("Success!")


if __name__ == '__main__':
    put_data(data=0)
