# twitter-bot-post-images
A Twitter bot that posts/tweets images/videos once every hour. This script is used to automate posts for the [@hourlytakasugi](https://twitter.com/hourlytakasugi) twitter account.

**Steps:**
1. You need to get a Developer Account first. This will give you some authentication keys that we will need to run the code. It is very simple to get a Developer Account, you just need to fill in some information about what your bot is going to do. To get a Developer Account, you can follow Steps 1-4 from the website [here](https://blog.hubspot.com/website/how-to-make-a-twitter-bot)
2. Once you have a Developer Account, edit values in `twitter-bot-tweet-images.py` with your own keys and image directory. The comments will help you understand which variables to edit.
3. Now run the code! Command: `python3 twitter-bot-tweet-images.py`
4. The code runs forever. So you'll need a machine which can keep it running. I run it inside tmux on AWS.
5. The code can tweet images and videos of most extensions (.png, .mp4, .gif, .jpg, .jpeg etc). Regarding videos, it can upload small videos, but larger videos might require some code modification. You'll have to test it out! To see size limit for images/videos, see [this documentation](https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/overview).

**FAQ/Notes:**
1. This code works with the Free version of the Developer Account. That is, you will have v2 Access, and Limited v1.1 Access. This is enough for our needs.
2. If you want to include a caption with your image in the tweet, simply do: `response = client_v2.create_tweet(text="my caption", media_ids=[media.media_id])`
3. If you want to insert more than one image in the tweet (upto 4 images), you'll have to get a media-id for each image. Then, replace the code with `response = client_v2.create_tweet(text="my caption", media_ids=[media1.media_id, media2.media_id, media3.media_id, media4.media_id])`
4. In the Developer Portal, make sure you edit the "User authentication set up" so that you have both "Read and Write" permissions. Regenerate your authentication keys if you make such a change.
5. Again, under "User authentication set up", you can set the callback url as http://127.0.0.1:5000/oauth/callback ; Regenerate your authentication keys if you make such a change.
6. Since an image is chosen randomly, there can be repeats before the entire list is exhausted. If you don't want to repeat images, I just use `os.rename` or `shutil.move` to move the tweeted file to another directory, say `backup_dir`. Once all the images have been tweeted, then `image_folder` will be empty. Now you can move all the files from `backup_dir` to `image_folder` and the process will start over. The code for this is simple so in case you need it, see the snippet [here](https://github.com/Saumya-Gupta-26/twitter-bot-post-images/issues/1#issuecomment-2314315882).
7. Please raise issues in case you need any help! Good luck!
