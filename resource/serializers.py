from rest_framework import serializers
from .models import CommonFunction

class CommonFunctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommonFunction
        fields = '__all__'