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
      embed = twitter.get_oembed_tweet(
        url = 'https://twitter.com/%s' % tweeter.twitter_un,
        maxwidth = 400,
        maxheight = 200,
        chrome = 'noheader nofooter',
        limit = 3,
        dnt = True
      )
      data[tweeter.twitter_un] = embed['html']

  template = loader.get_template('index.html')
  return HttpResponse(template.render({'tweeters': data}, request))
