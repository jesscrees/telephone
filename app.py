import os
import nexmo


NEXMO_API_KEY = os.environ['NEXMO_API_KEY']
NEXMO_SECRET_KEY = os.environ['NEXMO_SECRET_KEY']

client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

# make a call
response = client.create_call({
    'to': [{'type': 'phone', 'number': '14843331234'}],
    'from': {'type': 'phone', 'number': '14843335555'},
    'answer_url': ['https://example.com/answer']
})

# stream sybnthesized speech to a call
response = client.send_speech(uuid, text='Still working right now at least.')

#Stop sending a synthesized speech message to a call
response = client.stop_speech(uuid)
