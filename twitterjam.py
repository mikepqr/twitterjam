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


def advertisers(pth):
    output = (check_output(['ps2ascii', pth])
              .strip().decode())
    return [o.strip() for o in output.split('@')]


if __name__ == '__main__':
    logging.basicConfig(filename='log.log',
                        format='%(levelname)s:%(asctime)s: %(message)s')
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger('tweepy').setLevel(logging.WARNING)

    api = make_api()
    for ad in advertisers(sys.argv[1]):
        try:
            logging.info('Blocking ' + ad)
            api.create_block(ad)
        except tweepy.error.TweepError:
            logging.exception(ad)
