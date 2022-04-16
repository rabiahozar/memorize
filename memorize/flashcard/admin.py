from django.contrib import admin

from .models import Flashcard, StudyDeck

admin.site.register(Flashcard)
admin.site.register(StudyDeck)