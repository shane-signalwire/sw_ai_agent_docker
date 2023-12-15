# SignalWire AI Agent

This standalone docker container allows configuration and customization of a SignalWire AI Agent to be used with your pre-existing SignalWire Space.  The container includes a python web server, and example of how to progammatically configure the agent using Python.

## Prerequisites
 - An NGROK account and auth token (ngrok.com)
 - Docker desktop (docker.com)

## RUN VIA DOCKER
```console
# Build the Docker image:
docker build -t sw_aibot --build-arg "NGROK_AUTHTOKEN_ARG=<NGROK AUTH TOKEN> .

# Run the container
docker run -p 8000:5000 sw_aibot
```

## Configuration and Set Up
In a web broswer:
1.  Navigate to http://localhost:8000
2.  Copy the NGROK tunnel address
3.  Navigate to <your-signalwire-space>.signalwire.com
4.  Navigate to the desired 'Phone Number' and edit
5.  Set the number to:
    - Handle Calls Using:  A SWML Script
    - When A Call Comes In:  Paste in the NGROK tunnel address
