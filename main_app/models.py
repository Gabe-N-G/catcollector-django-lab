from django.db import models

# Create your models here.
# imagine models/schema

# Allows the 3 letter options of Feeding.meal
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
# Serializers part 4.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    # lives within cat class

    def __str__(self):
        return self.name
    
class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
    )

    # Create a cat_id FK
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    # get_x_display() is a built in python method. It generates the actual name of the thing.
    # This is only if you have choices that are different displayed than whats stored in database.
        return f"{self.get_meal_display()} on {self.date}"
    
    # changing ordering (latest date (closest to present) on top)
    class Meta:
        ordering = ['-date']