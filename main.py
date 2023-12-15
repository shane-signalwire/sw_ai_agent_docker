#!/usr/bin/env python3
# Author: Shane Harrell
# Email: shane.harrell@signalwire.com

import ngrok
from flask import Flask, request, render_template

listener = ngrok.forward(5000, authtoken_from_env=True)

global ngrok_tunnel_url
ngrok_tunnel_url = listener.url()

global global_ai_prompt
global_ai_prompt = '''You are the default helper bot.  Let the caller know that you are not yet configured, but want to help.'''

#print (ngrok_tunnel_url)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def my_form():
    response = f"Set your SignalWire Phone Number to Handle calls using a SWML Script and use the following webhook address: {ngrok_tunnel_url}"
    return render_template('my-form.html', result=response)

@app.route('/set_ai_prompt', methods=['POST'])
def set_ai_prompt():
    global global_ai_prompt
    global_ai_prompt = request.form.get("ai_prompt")
    print (global_ai_prompt)
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def main_ai_prompt():
    swml_web_hook_base_url = '<your_webhook_url>'
    swml_ai_prompt = global_ai_prompt

    swml = {}
    swml['sections'] = {
        'main': [{
            'ai': {
                'voice': 'en-US-Standard-A',
                'params': {
                    'confidence': 0.6,
                    'barge_confidence': 0.1,
                    'top_p': 0.3,
                    'temperature': 1.0,
                    'swaig_allow_swml': True,
                    'conscience': True
                },
                'prompt': {
                    'text': swml_ai_prompt
                }
            }
        }]
    }

    return (swml)



if __name__ == '__main__':
    app.run(host="0.0.0.0")