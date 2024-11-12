# Serializers are used for a restful API so we can communicate with backend to front end from json/sql to html and back.

from rest_framework import serializers
from .models import Cat, Feeding

class CatSerializer(serializers.ModelSerializer):
    # Meta is a pseudocalss to add the Model with the fields.
    fed_for_today = serializers.SerializerMethodField() # add this line

    class Meta:
        model = Cat
        # Can also select specific fields.
        fields = '__all__'

    def get_fed_for_today(self, obj):
        return obj.fed_for_today()

class FeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding
        fields = '__all__'
        read_only_fields = ('cat',)