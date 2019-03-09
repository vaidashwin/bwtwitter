from django.db import models

# Create your models here.

class BWTweeter(models.Model):
  name = models.CharField(max_length = 64, primary_key = True, unique = True)
  twitter_un = models.CharField(
    max_length = 64,
    verbose_name = "Twitter Username",
    unique = True
  )
  BLIZZARD = 'OB'
  TOURNAMENT = 'TO'
  SCR_DEV = 'DV'
  CASTER = 'CR'
  PLAYER = 'PL'
  TIER_CHOICES = (
    (BLIZZARD, "Official Blizzard"),
    (TOURNAMENT, "Tournaments"),
    (SCR_DEV, "SC:R Developers"),
    (CASTER, "Casters"),
    (PLAYER, "Players")
  )
  tier = models.CharField(
    max_length = 2,
    choices = TIER_CHOICES,
    default = PLAYER
  )
  def __str__(self):
      return "%s (@%s)" % (self.name, self.twitter_un)
