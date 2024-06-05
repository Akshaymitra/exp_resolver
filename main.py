import paho.mqtt.client as mqtt
import json
from sources import DATA_SOURCES
import constants as c
import uuid
import time
import traceback
 
class MQTTClient:
    def __init__(self, topic, subtopic):
        self.topic = topic
        self.subtopic = subtopic
        self.pubtopic = "flow/compute/req"
        self.sent_data_source_ids = {}
        self.received_req_ids = []
 
        self.client = mqtt.Client(str(uuid.uuid1()))
        self.all_data_sources_processed = False
        self.setup_client()
       
    def setup_client(self):
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.client.on_publish = self.on_publish
        self.client.on_disconnect = self.on_disconnect
        self.client.username_pw_set(c.USERNAME, c.PASSWORD)
        self.client.connect(c.BROKER_ADDRESS, 1883, 60)
        self.client.subscribe("flow/compute/results/+")
 
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print('\nClient Connected')
            client.subscribe(self.subtopic, qos=0)
            print("Subscribed")
        else:
            print('\nBad Connection:', rc)
   
    def on_message(self, client, userdata, msg):
        response_data = json.loads(msg.payload.decode())
        received_req_id = response_data.get("reqID")
        self.sent_data_source_ids[received_req_id] = "Passed"
        num_passed_items = sum(value == 'Passed' for value in self.sent_data_source_ids.values())
        total_items = len(self.sent_data_source_ids)
        pass_percentage = (num_passed_items / total_items) * 100
        if num_passed_items < total_items:
            failed_sources = [source for source, result in self.sent_data_source_ids.items() if result != 'Passed']
            print(f"Still processing sources: {failed_sources}")
        else:
            print("All sources are passed.")
            print(f"Pass Percentage: {pass_percentage}% , passed {num_passed_items} out of {total_items}")
 
    def on_publish(self, client, userdata, mid):
        print("Message published with MID:", mid)
 
    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection from MQTT broker")
 
    def send_request(self, data_source_id, data_source):
        response_topic = f"flow/{self.topic}/results/+"
        self.client.subscribe(response_topic, qos=0)
        payload = {
            "reqID": data_source_id,
            "reqBody": {
                "cmd": "start",
                "timeOut": -1,
                "log": "true",
                "output": {"type": 0},
                "dataSource": data_source
            },
            "origin": "iosense.io/dashboard/xyz",
            "userID": "645a159222722a319ca5f5ad",
            "time": int(time.time() * 1000)
        }
        try:
            self.client.publish(self.pubtopic, json.dumps(payload))
            print("==========", payload)
        except Exception as e:
            print("=========================================")
            print('\nMQTT Error Occurred:', e)
            traceback.print_exc()
 
    def run_test(self):
        for data_source_id, data_source_params in DATA_SOURCES.items():
            print("Testing data source:", data_source_id)
            self.sent_data_source_ids[data_source_id] = "Processing"
            self.send_request(data_source_id, data_source_params)
            time.sleep(1)
           
        self.client.loop_start()  # Start MQTT client loop
 
    def check_failed_sources(self):
        time.sleep(10)  # Wait for 10 seconds
        failed_sources = [source for source, result in self.sent_data_source_ids.items() if result != 'Passed']
        if failed_sources:
            return f"Failed sources after 10 seconds: {failed_sources}"
        else:
            return "All sources are passed within 10 seconds."
       
if __name__ == '__main__':
    mqtt_client = MQTTClient(topic="compute", subtopic="flow/compute/results/+")
    mqtt_client.run_test()
 
    # Check for failed sources after 10 seconds
    response = mqtt_client.check_failed_sources()
    print("final result -->",response)