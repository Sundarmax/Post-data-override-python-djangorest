from rest_framework import serializers
from .models import Sections,Ratings

class sectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = '__all__'
class ratingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['rating_level'] = ret['rating_level'].upper()
        return ret