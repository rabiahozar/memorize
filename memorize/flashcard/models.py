from django.db import models

# Create your models here.

class Flashcard(models.Model):
    front_text = models.CharField(max_length=500)
    back_text = models.CharField(max_length=500)
    example_text = models.CharField(max_length=500)
    last_revisited_date = models.DateTimeField('data_revisited')

class StudyDeck(models.Model):
    name = models.CharField(max_length=200)
    flashcards = models.ManyToManyField(Flashcard)
