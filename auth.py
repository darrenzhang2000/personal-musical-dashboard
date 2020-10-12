import base64
import requests
import datetime


import configparser

def get_client_id():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Client_ID']['id']

def get_client_secret():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Client_Secret']['secret']

print(get_client_id)
print(get_client_secret)

client_creds = "{}:{}".format(get_client_id(), get_client_secret())
print(client_creds)

# cient_creds.encode() changes to bytes
client_creds_b64 = base64.b64encode(client_creds.encode())
type(client_creds_b64)

token_url = 'https://accounts.spotify.com/api/token'
method = 'POST'
token_data = {
    "grant_type": "client_credentials"
}
# base64 encoded string
token_headers = {
    "Authorization": f"Basic {client_creds_b64.decode()}"
}

r = requests.post(token_url, data=token_data, headers=token_headers)

valid_request = r.status_code in range(200, 299)
if valid_request:
    token_response_data = r.json()
    now = datetime.datetime.now()
    access_token = token_response_data['access_token']
    expires_in = token_response_data['expires_in'] #secs
    expires = now + datetime.timedelta(seconds=expires_in)
    print(access_token, expires_in)
