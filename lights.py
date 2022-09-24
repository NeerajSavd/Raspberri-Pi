import urllib.request
import requests
import time


IP = '192.168.86.29'
PORT = '3000'

def run():
    url = "http://" + IP + ":" + PORT + "/assistant"
    try:
        response = urllib.request.urlopen(url)
        if response.status == 200:
            print("Connected")
            data = {"user": "neeraj",
                "command": "Neeraj room lights on"
            }
            r = requests.post(url=url, data=data)
            print(r.text)
            print(r.status_code)
            # christmas(url)
            full_white(url)
            # off(url)
        else:
            print(response.status)
    except:
        print("Failed")


def christmas(url: str):
    for i in range(10):
        red = {
            "command": "Neeraj room lights red"
        }
        requests.post(url=url, data=red)
        time.sleep(1)
        green = {
            "command": "Neeraj room lights green"
        }
        requests.post(url=url, data=green)
        time.sleep(1)


def full_white(url: str):
    on = {
        "command": "Neeraj room lights on"
    }
    requests.post(url=url, data=on)
    white = {
        "command": "Neeraj room lights ivory"
    }
    requests.post(url=url, data=white)
    bright = {
        "command": "Neeraj room lights 100 percent brightness"
    }
    requests.post(url=url, data=bright)


def off(url: str):
    off = {
        "command": "Neeraj room lights off"
    }
    requests.post(url=url, data=off)


if __name__ == '__main__':
    run()
