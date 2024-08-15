from xinference.client import Client

endpoint = 'http://localhost:9997'
client = Client(endpoint)
model = client.unregister_model(model_type="<model_type>", model_name='custom-llama-2')
