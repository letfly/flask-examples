from flask import Flask, url_for, session, request, flash, redirect
from flask_oauthlib.client import OAuth
from flask_oauthlib.client import OAuthException

app = Flask(__name__)
app.debug = True
app.secret_key = '53a01e6bd34caef997eed24f5ee9'
oauth = OAuth(app)

def _change_weibo_header(uri, headers, body):
    auth = headers.get('Authorization')
    if auth:
        auth = auth.replace('Bearer', 'OAuth2')
        headers['Authorization'] = auth
    return uri, headers, body

weibo = oauth.remote_app(
    'weibo',
    consumer_key='1814846457',
    consumer_secret='164733c9f63e4912dbe05c0a820480a5',
    request_token_params={'scope': 'email,statuses_to_me_read'},
    base_url='https://api.weibo.com/2/',
    authorize_url='https://api.weibo.com/oauth2/authorize',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://api.weibo.com/oauth2/access_token',

    # force to parse the response in applcation/json
    content_type='application/json',
)

weibo.pre_request = _change_weibo_header

def get_next():
    next_url = request.args.get('next')
    if not next_url:
        next_url = '/'
    return next_url

def authorize(approach, next_url, callback):
    session['%s_oauthredir' % approach] = next_url #<SecureCookieSession {u'weibo_oauthredir': '/'}>
    social_approach = oauth.remote_apps.get(approach) #<flask_oauthlib.client.OAuthRemoteApp object at 0x7f5c63beec10>
    return social_approach.authorize(callback=callback) #<Response 631 bytes [302 FOUND]>

@app.route('/')
def index():
    return 'hello'

@app.route('/authorize-use/<approach>')
def authorize_use(approach='weibo'):
    next_url = get_next() #/
    callback = url_for('.oauth_authorized',
                       approach=approach,
                       next=next_url,
                       _external=True) #http://dev.zaih.com:5000/oauth_authorized/weibo?next=%2F
    return authorize(approach, next_url, callback)

@app.route('/oauth_authorized/<approach>')
def oauth_authorized(approach='weibo'):
    next_url = get_next()
    auth = None
    
    social_approach = oauth.remote_apps.get(approach)
    resp = social_approach.authorized_response() #{u'access_token': u'2.00fPGn5CDTuoyBb55d9432700m5K5k', u'remind_in': u'666277', u'expires_in': 666277, u'uid': u'2198599835'}

    if resp is None or isinstance(resp, OAuthException):
        flash(u'You denied the request to sign in.')
        return redirect(next_url)
    
    identity = resp['uid'] #2198599835
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
