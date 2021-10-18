from typing import Text
from django.db import models
from django.db.models.deletion import CASCADE

from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model): #Model is aclass that define the basic funtionality of a model
    """a topic that user create"""
    text = models.CharField(max_length=300) # use CharField when you want to creat a small amount of text
    date_added = models.DateTimeField(auto_now_add=True) #auto_now_add=True tells django that set time at current time
    owner = models.ForeignKey(User, on_delete=CASCADE)
    def __str__(self):
        """return the string representation of the model"""
        return self.text

class Entry(models.Model):
    """What have learn about the topic"""
    topic = models.ForeignKey(Topic, on_delete=CASCADE)#on_delete is specify
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """return string represenatation of the model""" 
        if len(self.text) <= 50:
            return self.text
        elif len(self.text) > 50:
            return self.text[:50] +'...' 
            