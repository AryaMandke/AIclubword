import requests
import json

def get_prediction(input_user):
  data={"sentence":input_user}
  url = 'https://askai.aiclub.world/c7b46abf-026d-4a87-909a-c3388cbd4ab8'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  prediction = json.loads(json.loads(response)['body'])['predicted_label']
  return prediction