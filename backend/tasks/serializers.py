from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Job, JobApplication, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class JobSerializer(GeoFeatureModelSerializer):
    distance = serializers.SerializerMethodField()
    
    class Meta:
        model = Job
        geo_field = 'location'
        fields = '__all__'
        read_only_fields = ('client', 'status', 'created_at', 'updated_at')
    
    def get_distance(self, obj):
        user_location = self.context['request'].user.location
        if user_location:
            return user_location.distance(obj.location)
        return None

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'
        read_only_fields = ('worker', 'status', 'created_at', 'updated_at')