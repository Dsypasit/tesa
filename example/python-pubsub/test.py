import paho.mqtt.client as mqtt
import time
# This is the Publisher

client = mqtt.Client()
client.connect("localhost")
i = 0
client.loop_start()
while True:
    client.publish("topic/test", f"Hello world!{i}")
    i+=1
    time.sleep(1)
    if i == 10:
        client.disconnect()
        break
# client.loop_stop()
