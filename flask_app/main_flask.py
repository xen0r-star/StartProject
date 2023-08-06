from flask import Flask, request, render_template
import signal
import requests
import os
import sys
import logging
import webbrowser


app = Flask(__name__, template_folder='templates/')

CLIENT_ID = "8c57cd698a180f64c80e"
CLIENT_SECRET = os.environ.get('GITHUB_OAUTH_TOKEN_StartProject')
REDIRECT_URI = "http://localhost:5000/callback"
GITHUB_API_BASE_URL = "https://api.github.com"


# Erreur
logging.basicConfig(level=logging.INFO, filename='flask_app/errors.log')

def custom_excepthook(exc_type, exc_value, exc_traceback):
    logging.error("Une erreur est survenue :", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = custom_excepthook

@app.errorhandler(Exception)
def handle_all_errors(error):
    return render_template('Erreur.html')


@app.route('/')
def index():
    return render_template('login.html', client_id=CLIENT_ID)

access_token = None
@app.route('/callback')
def callback():
    code = request.args.get('code')
    if code:
        data = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'code': code,
            'redirect_uri': REDIRECT_URI
        }
        response = requests.post('https://github.com/login/oauth/access_token', data=data, headers={'Accept': 'application/json'})
        if response.status_code == 200:
            global access_token
            access_token = response.json()["access_token"]
            return render_template('success.html')

    return 'La connexion a échoué.'


@app.route('/open_app', methods=['POST'])
def open_app():
    print("open_app")
    global exit_thread
    exit_thread = access_token


@app.route('/exit', methods=['POST'])
def exit():
    print("exit")
    webbrowser.open("https://xen0r-star.github.io/StartProject/")
    


if __name__ == "__main__":
    app.run(debug=False, use_debugger=False, use_reloader=False)
