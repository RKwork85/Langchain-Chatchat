import json
from xinference.client import Client

with open('config.json') as fd:
    model = fd.read()

# replace with real xinference endpoint
endpoint = 'http://localhost:9997'
client = Client(endpoint)
client.register_model(model_type="LLM", model=model, persist=False)