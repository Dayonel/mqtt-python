import random
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883

def connect_mqtt():
    def on_connect(client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")
    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client