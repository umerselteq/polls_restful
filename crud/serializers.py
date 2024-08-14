from rest_framework import serializers
from . models import question, choice

class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model = question
        fields = '__all__'

class choiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = choice
        fields = '__all__'


# def create(self, validated_data):
#     return question.objects.create(**validated_data)
#
#
# def update(self, instance, validated_data):
#     instance.question_text = validated_data.get('question_text', instance.question_text)
#     instance.pub_date = validated_data.get('pub_date', instance.pub_date)
#     return instance