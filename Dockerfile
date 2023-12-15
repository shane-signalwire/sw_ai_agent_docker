FROM alpine

ARG NGROK_AUTHTOKEN_ARG
ENV NGROK_AUTHTOKEN=$NGROK_AUTHTOKEN_ARG

RUN apk add --update --no-cache python3
RUN apk add --update --no-cache py3-pip


# Add Authtoken param (Needs to be in quotes when added to env)

# Install the python scripts
RUN mkdir -p /root/templates

COPY main.py /root/main.py
RUN chmod +x /root/main.py
COPY requirements.txt /root/requirements.txt
COPY templates /root/templates

# PIP install requirements
RUN pip3 install --break-system-packages -r /root/requirements.txt

ENTRYPOINT /root/main.py


