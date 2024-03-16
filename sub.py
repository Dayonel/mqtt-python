from client import connect_mqtt
from paho.mqtt import client as mqtt_client
import sys
import requests

base_url = 'http://localhost:54321/functions/v1' # supabase function
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6ImFub24iLCJleHAiOjE5ODM4MTI5OTZ9.CRXP1A7WOeoJeXxjNni43kdQwgnWNReilDMblYTn_I0"}
topic = sys.argv[1]

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        data = msg.payload.decode()
        print(f"Received `{data}` from `{msg.topic}` topic")
        sensor_id  = msg.topic.split("/")[1]
        url = f"{base_url}/sensor/{sensor_id}/light"
        payload = {'intensity': int(data)}
        x = requests.post(url, json=payload, headers=headers)
        print(x.text)

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()