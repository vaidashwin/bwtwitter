from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from twython import Twython

from .models import BWTweeter

import logging

def getTwitter():
  return Twython(
  settings.API_KEY,
  settings.API_SECRET,
  settings.APP_KEY,
  settings.APP_SECRET
  )

def index(request):
  all_twitters = BWTweeter.objects.order_by('-twitter_un')
  twitter = getTwitter()

  tweet_data = {}

  header_map = dict(BWTweeter.TIER_CHOICES)
  for tier_name in header_map.values():
   tweet_data[tier_name] = []

  try:
    for tweeter in all_twitters:
      tweet_data[header_map[tweeter.tier]].append(twitter.get_oembed_tweet(
      url = 'https://twitter.com/%s' % tweeter.twitter_un,
      chrome = 'noheader nofooter',
      maxheight = 300,
      dnt = True
    )['html'])
  except RuntimeError:
    logging.error("Something went wrong " + sys.exc_info()[0])

  template = loader.get_template('index.html')
  return HttpResponse(template.render({
   'grouped_tweets': tweet_data
  }, request))

def tryauth(request):
  twitter = getTwitter()
  auth = twitter.get_authentication_tokens()
  request.session['oauth_token_secret'] = auth['oauth_token_secret']
  return HttpResponseRedirect(auth['auth_url'])


def massfollow(request):
  OAUTH_TOKEN = request.GET.get('oauth_token', '')
  OAUTH_TOKEN_SECRET = request.session['oauth_token_secret']
  twitter = Twython(settings.APP_KEY,
    settings.APP_SECRET,
    OAUTH_TOKEN,
    OAUTH_TOKEN_SECRET
  )

  oauth_verifier = request.GET.get('oauth_verifier', '')
  final_step = twitter.get_authorized_tokens(oauth_verifier)
  utwitter = Twython(settings.APP_KEY,
    settings.APP_SECRET,
    final_step['oauth_token'],
    final_step['oauth_token_secret']
  )
  print(utwitter.client.auth)
  print(utwitter.verify_credentials())

  all_twitters = BWTweeter.objects.order_by('-twitter_un')

  try:
    for tweeter in all_twitters:
      twitter.create_friendship(
        screen_name = tweeter.twitter_un,
        follow = 'true'
      )
  except RuntimeError:
    logging.error("Something went wrong " + sys.exc_info()[0])

  return HttpResponseRedirect('')
