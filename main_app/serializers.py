from rest_framework import serializers
from .models import Cat

class CatSerializer(serializers.ModelSerializer):
    # Meta is a pseudocalss to add the Model with the fields.
    class Meta:
        model = Cat
        # Can also select specific fields.
        fields = '__all__'
