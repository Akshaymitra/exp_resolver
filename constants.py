# Built-In Functions
import os

# Third Party Functions
import pytz
from dotenv import load_dotenv

load_dotenv()

# MQTT Broker
USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")
BROKER_ADDRESS = os.getenv("MQTT_HOST")
PORT = int(os.getenv("MQTT_PORT"))

# Rabbit MQ Broker
RMQ_USER_ID = os.getenv("RABBITMQ_DEFAULT_USER")
RMQ_PASSWORD = os.getenv("RABBITMQ_DEFAULT_PASS")
RMQ_HOST = os.getenv("RMQ_HOST")
RMQ_PORT = int(os.getenv("RMQ_PORT"))

# Data Science API
URL = os.getenv("URL")
CONNECTION_STRING = b"WUHaM30tzELCSrfTypGF6A3KNubVIVHSiagTyZyWpUg="

if os.getenv("ONPREM").lower() == "true":
    ON_PREMISE = True
else:
    ON_PREMISE = False

# Timezone
IST = pytz.timezone("Asia/Kolkata")