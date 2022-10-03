from django.contrib import admin

# Register your models here.
from .models import Pets

@admin.register(Pets)
class PetsAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'year')

    def species(self, obj):
        if obj.species == str(1):
            return 'dog'
        elif obj.species == str(2):
            return 'cat'
        else:
            return 'hamster'
        