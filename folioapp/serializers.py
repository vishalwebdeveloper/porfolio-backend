from rest_framework import serializers
from .models import Portfolio

class PortfolioSerializer(serializers.ModelSerializer):
    technologies = serializers.ListField(
        child=serializers.CharField(),
        source='get_technologies_list',
        write_only=True
    )
    technologies = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Portfolio
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        extra_fields = ['technologies']
    
    def get_technologies(self, obj):
        return obj.technologies.split(',') if obj.technologies else []

    def create(self, validated_data):
        tech_list = validated_data.pop('get_technologies_list', [])
        validated_data['technologies'] = ','.join(tech_list)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        tech_list = validated_data.pop('get_technologies_list', None)
        if tech_list is not None:
            validated_data['technologies'] = ','.join(tech_list)
        return super().update(instance, validated_data)