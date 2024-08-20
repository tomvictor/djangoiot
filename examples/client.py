from iotcore import IotCore
import time

def hello_subscription_call_back(data):
    print(f"my data: {data}")

def main():
    print("invoking the mqtt client")
    iot = IotCore(host="test.mosquitto.org",port=1883)

    iot.subscribe("iotcore",hello_subscription_call_back)
    print("wait for msgs")
    iot.background_loop_forever()
    while True:
        time.sleep(10)


if __name__=="__main__":
    main()
