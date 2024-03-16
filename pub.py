from client import connect_mqtt
from paho.mqtt import client as mqtt_client
import sys
import time

topic = sys.argv[1]
msg = sys.argv[2]
 
def publish(client):
    while True:
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        time.sleep(10)


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == '__main__':
    run()