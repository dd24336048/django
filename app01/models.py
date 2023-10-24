
# Create your models here.
from django.db import models
class EnglishOptional(models.Model):
    topic_number = models.TextField()
    answer_A = models.TextField()
    answer_B = models.TextField()
    answer_C = models.TextField()
    answer_D = models.TextField()
    answer = models.CharField(max_length=255)
    year = models.IntegerField()

class EnglishOptionalNumber3(models.Model):
    topic_number = models.TextField()
    answer_A = models.TextField()
    answer_B = models.TextField()
    answer_C = models.TextField()
    answer_D = models.TextField()
    answer_E = models.TextField()
    answer_F = models.TextField()
    answer_G = models.TextField()
    answer_H = models.TextField()
    answer_I = models.TextField()
    answer_J = models.TextField()
    answer = models.CharField(max_length=255)
    year = models.IntegerField()

class EnglishOptionalNumber4(models.Model):
    topic_number = models.TextField()
    topic = models.TextField()
    answer_A = models.TextField()
    answer_B = models.TextField()
    answer_C = models.TextField()
    answer_D = models.TextField()
    answer = models.CharField(max_length=255)
    year = models.IntegerField()

class EnglishOptionalNumber5(models.Model):
    topic_number = models.TextField()
    topic = models.TextField()
    answer_A = models.TextField()
    answer_B = models.TextField()
    answer_C = models.TextField()
    answer_D = models.TextField()
    answer = models.CharField(max_length=255)
    year = models.IntegerField()

class EnglishTopic(models.Model):
    topic_number = models.TextField()
    topic = models.TextField()
    answer_A = models.TextField()
    answer_B = models.TextField()
    answer_C = models.TextField()
    answer_D = models.TextField()
    answer = models.CharField(max_length=255)
    year = models.IntegerField()

class EnglishWord(models.Model):
    word = models.TextField()
    phonetic_symbols = models.TextField()
    part_of_speech = models.TextField()
    explain = models.TextField()

class OptionalTopic(models.Model):
    topic_number = models.TextField()
    topic = models.TextField()
    year = models.IntegerField()

class OptionalTopicNumber4(models.Model):
    topic_number = models.TextField()
    topic = models.TextField()
    year = models.IntegerField()