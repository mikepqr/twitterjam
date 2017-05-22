# twitterjam

Block your twitter advertiser list

## Usage

 1. Clone this repo
 2. Install the dependencies
    - The command line utility `ps2ascii` (found in the `ghostscript` package
      on Linux/macOS)
    - The python package `tweepy`
 3. Create a Twitter application and add your keys to `twitterjam.py`
    - Go to [Twitter apps](https://apps.twitter.com/)
    - Click [create new app](https://apps.twitter.com/app/new) and fill in the
      form
    - Click the **keys and tokens** tab
    - Click **create my access token**
    - Edit your copy of `twitterjam.py` to add your `consumer_key`,
      `consumer_secret`, `access_token` and `access_token_secret`. 
 4. Get a copy of your twitter_advertiser_list.pdf by clicking **Request
    Advertiser List** on [Your Twitter
    Data](https://twitter.com/settings/your_twitter_data). They will email you a file `twitter_advertiser_list.pdf`.
 5. Finally run this command
    ```bash
    $ python twitterjam /path/to/twitter_advertiser_list.pdf
    ```
