import logging
import os
import sys
import tweepy

from subprocess import check_output

# edit this to
# consumer_key = "sdfmKLMKMW567KM656mmasdfq", etc.
consumer_key = None
consumer_secret = None
access_token = None
access_token_secret = None


def make_api():
    auth = tweepy.OAuthHandler(
        consumer_key or os.environ['consumer_key'],
        consumer_secret or os.environ['consumer_secret']
    )
    auth.set_access_token(
        access_token or os.environ['access_token'],
        access_token_secret or os.environ['access_token_secret']
    )
    return tweepy.API(auth, wait_on_rate_limit=True,
                      wait_on_rate_limit_notify=True)


def get_advertisers(pth):
    output = (check_output(['ps2ascii', pth])
              .strip().decode())
    return [o.strip() for o in output.split('@')
            if len(o.split()) == 1]  # if exactly one word on line


def block(account):
    try:
        logging.info('Blocking ' + account)
        api.create_block(account)
    except tweepy.error.TweepError:
        logging.exception(account)


if __name__ == '__main__':
    logging.basicConfig(filename='twitterjam.log',
                        format='%(levelname)s:%(asctime)s: %(message)s')
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger('tweepy').setLevel(logging.WARNING)
    api = make_api()
    for advertiser in get_advertisers(sys.argv[1]):
        block(advertiser)
