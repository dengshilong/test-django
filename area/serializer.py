from rest_framework import serializers
from .models import Area
class AreaWithParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id','name','level','parent')