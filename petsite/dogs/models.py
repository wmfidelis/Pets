from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

def year_choices():
    # for r in range(1950, datetime.date.today())
    return [(r,r) for r in range(1950, datetime.date.today().year + 1)]

class Pets(models.Model):
    speciesChoices = (
    ('1', 'dog'),
    ('2', 'cat'),
    ('3', 'hamster'),
)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=1, choices=speciesChoices)
    year = models.IntegerField(('year'), validators=[MinValueValidator(1950), max_value_current_year])

    def __str__(self):
        return '%s - %s' % (self.name, self.species)
