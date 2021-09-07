
# import packages
from facebook_business.adobjects.post import Post
from facebook_business.api import FacebookAdsApi

# variables
ACCESS_TOKEN = XXX
F_PID = XXX

# initialize facebook api connection
FacebookAdsApi.init(access_token=ACCESS_TOKEN, debug=True)

# get comments
comments = Post(F_PID).get_comments(
            params={'filter': 'stream',
                    'summary': '1'})

# get count of comments
comments_total = f_post_comments.total()
