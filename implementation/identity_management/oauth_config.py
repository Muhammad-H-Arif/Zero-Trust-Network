
import os
from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = 'random_secret_key'
oauth = OAuth(app)

auth0 = oauth.register(
    'auth0',
    client_id=os.getenv('AUTH0_CLIENT_ID'),
    client_secret=os.getenv('AUTH0_CLIENT_SECRET'),
    api_base_url=f"https://{os.getenv('AUTH0_DOMAIN')}",
    access_token_url=f"https://{os.getenv('AUTH0_DOMAIN')}/oauth/token",
    authorize_url=f"https://{os.getenv('AUTH0_DOMAIN')}/authorize",
    client_kwargs={
        'scope': 'openid profile email',
    },
)

@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri=url_for('callback', _external=True))

@app.route('/callback')
def callback():
    auth0.authorize_access_token()
    userinfo = auth0.parse_id_token()
    session['user'] = userinfo
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return f"Welcome, {session['user']['name']}!"

if __name__ == '__main__':
    app.run()
