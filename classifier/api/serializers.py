from rest_framework import serializers
from classifier.models import DogImage

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = DogImage
        fields = ['image']

        