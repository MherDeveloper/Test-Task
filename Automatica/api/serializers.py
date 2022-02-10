from django.core.exceptions import ValidationError
from rest_framework import serializers
from api.models import Store, Visit


class VisitModelSerializer(serializers.ModelSerializer):
    """ Model serializer for visits, and phone_number field for auth """

    phone_number = serializers.CharField(max_length=255, required=True, write_only=True)
    longitude = serializers.CharField(required=True, write_only=True)
    latitude = serializers.CharField(required=True, write_only=True)
    store = serializers.PrimaryKeyRelatedField(required=True, write_only=True, queryset=Store.objects.all())

    class Meta:
        model = Visit
        fields = ['id', 'store', 'latitude', 'longitude', 'phone_number', 'date']

    def validate(self, attrs):
        store = attrs['store']
        if store.worker.phone_number != attrs['phone_number']:
            raise ValidationError({'detail': 'Please fill the correct number'})
        return attrs

    def create(self, validated_data):
        if 'phone_number' in validated_data:
            validated_data.pop('phone_number')
        return super().create(validated_data)


class StoreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'title']