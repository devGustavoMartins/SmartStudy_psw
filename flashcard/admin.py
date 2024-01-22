from django.contrib import admin
from .models import Categoria, Desafio, Flashcard, FlashcardDesafio

admin.site.register(Categoria)
admin.site.register(Flashcard)
admin.site.register(FlashcardDesafio)
admin.site.register(Desafio)