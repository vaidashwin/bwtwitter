from django.http import HttpResponse
from django.shortcuts import render
from .models import BWTweeter

def index(request):
  all_twitters = BWTweeter.objects.order_by('-twitter_un')
  output = ', '.join([str(t) for t in all_twitters])
  return HttpResponse(output)
