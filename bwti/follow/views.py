from django.conf import settings
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from twython import Twython

from .models import BWTweeter

def index(request):
  all_twitters = BWTweeter.objects.order_by('-twitter_un')
  twitter = Twython(settings.API_KEY,
    settings.API_SECRET,
    settings.APP_KEY,
    settings.APP_SECRET
  )

  data = {}

  for tweeter in all_twitters:
      tweet = twitter.get_user_timeline(screen_name=tweeter.twitter_un)[0]
      embed_url = tweet['entities']['urls'][0]['expanded_url'].replace("/i", "")
      embed = twitter.get_oembed_tweet(url=embed_url, maxwidth=280)
      data[tweeter.twitter_un] = embed['html']

  template = loader.get_template('index.html')
  return HttpResponse(template.render({'tweeters': data}, request))
