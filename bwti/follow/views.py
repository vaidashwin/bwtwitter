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

  tweet_data = {}

  header_map = dict(BWTweeter.TIER_CHOICES)
  for tier_name in header_map.values():
    tweet_data[tier_name] = []

  for tweeter in all_twitters:
    tweet_data[header_map[tweeter.tier]].append(twitter.get_oembed_tweet(
      url = 'https://twitter.com/%s' % tweeter.twitter_un,
      chrome = 'noheader nofooter',
      maxheight = 300,
      dnt = True
    )['html'])

  template = loader.get_template('index.html')
  return HttpResponse(template.render({
    'grouped_tweets': tweet_data
  }, request))
