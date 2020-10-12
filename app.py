from flask import Flask, render_template, redirect
from urllib.parse import urlencode #urllib requires Python3
import configparser
import startup
from flask import request


app = Flask(__name__)

def get_client_id():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Client_ID']['id']

@app.route('/')
def index():
    response = startup.getUser()
    return redirect(response)

@app.route('/callback/')
def callback():
    startup.getUserToken(request.args['code'])
    return "hi"


# @app.route('/login')
# def login():
#     r = redirect('https://accounts.spotify.com/authorize?' +
#     urlencode({
#         'response_type': 'code',
#         'client_id': get_client_id(),
#         'scope': 'user-read-private user-read-email',
#         'redirect_uri': 'http://localhost:5000/callback' 
#     }))
#     print(r)
#     return r
# INVALID_CLIENT: Invalid client
# need to specify redirect uri on spotify

if __name__ == '__main__':
    app.run()