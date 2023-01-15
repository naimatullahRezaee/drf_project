from rest_framework import serializers
from watchlist.models import Watch , Review, StreamPlatform




class WatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Watch
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    writer = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = "__all__"

class StreamSerializer(serializers.ModelSerializer):
    watch = WatchSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"

    






    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField()
    # description = serializers.CharField()
    # active = serializers.BooleanField()

    # def create(self, validated_data):
    #     return Watch.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance