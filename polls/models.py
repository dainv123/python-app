import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.question_text

  def was_published_recently(self):
    # return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text

class Book(models.Model):
  auth = models.ForeignKey(User, on_delete=models.CASCADE) 
  title = models.CharField(max_length=50)
  total_pages = models.IntegerField(default=0)
  rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
  photo = models.FileField(upload_to="media", null=True, blank=True)
  published_date = models.DateTimeField('date published')

  def __str__(self):
    return self.title


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(max_length=500, blank=True)
  location = models.TextField(max_length=30, blank=True)
  birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)
  instance.profile.save()
    

class Beast(models.Model):
    MOM_CLASSIFICATIONS = [
    ('XXXXX', 'Known Wizard  Killer'),
    ('XXXX', 'Dangerous'),
    ('XXX', 'Competent wizard should cope'),
    ('XX', 'Harmless'),
    ('X', 'Boring'),
 ]
    name = models.CharField(max_length=60)
    mom_classification = models.CharField(max_length=5, choices=MOM_CLASSIFICATIONS)
    description = models.TextField()
    media = models.FileField(upload_to="media", null=True, blank=True)