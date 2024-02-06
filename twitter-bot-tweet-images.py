# Use pip/conda to make sure the following libraries exist in your enviroment
import os, random, tweepy, time, schedule

# Fill in your credentials here; Alternatively, use os.environ if you want to use environment variables instead
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

# Twitter API v2 --- Will be used to post the tweet
client_v2 = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_KEY,
    access_token_secret=ACCESS_SECRET
)

# Twitter API v1.1 --- Will be used to obtain media-id that is needed to post the tweet
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(
    ACCESS_KEY,
    ACCESS_SECRET,
)
api_v1 = tweepy.API(auth)

# Directory where images are stored
image_folder = '/path/to/directory'

def tweet_random_image():
    images = [img for img in os.listdir(image_folder)]

    random_image = random.choice(images)
    image_path = os.path.join(image_folder, random_image)
    
    try:
        # Post the image via v1.1 first, get the media-id and then use v2
        media = api_v1.media_upload(image_path)
        response = client_v2.create_tweet(media_ids=[media.media_id])
    except:
        print("Error {} for file: {}".format(response, random_image))

# Schedule the tweet to be sent now and then once every hour
tweet_random_image()
schedule.every().hour.do(tweet_random_image)

# Code runs forerver. After every second, it checkes whether there is a scheduled job, and if there is, it calls tweet_random_image()
while True:
    schedule.run_pending()
    time.sleep(1)