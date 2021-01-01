import keys
from requests_oauthlib import OAuth1

def get_auth():
    consumer_key = keys.CONSUMER_KEY
    consumer_secret = keys.CONSUMER_SECRET
    access_key = keys.ACCESS_KEY
    access_secret = keys.ACCESS_SECRET

    auth = OAuth1(consumer_key,
                client_secret=consumer_secret,
                resource_owner_key=access_key,
                resource_owner_secret=access_secret)

    return auth

txgvg_dt = {
    0: 25,
    1: 24,
    2: 23,
    3: 22,
    4: 28,
    5: 27,
    6: 26
}