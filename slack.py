import requests
import json


def sendMessage():
    url = 'https://hooks.slack.com/services/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'
    payload=json.dumps({"text": "Hello Im Joel from python", "attachments":[{ "text":"here a new format" }]})
    x = requests.post(url, payload)
    print(x.text)

sendMessage()