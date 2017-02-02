from rest_framework import serializers
from logbook.models import Climb

# class ClimbSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    colour = serializers.CharField(required = False, max_length = 50)
#    grade = serializers.CharField(required = False,max_length=6)

#    def create(self, validated_data):
#        #Create and return a new Climb with the validated data
#    
#        return Climb.objects.create(**validated_data)

 #   def update(self, instance, validated_data):       
          #  Update and return an existing Climb with the validated data

#          instance.colour = validated_data.get('colour', instance.colour)
#          instance.grade = validated_data.get('grade', instance.grade)
#          instance.save()
#          return instance

class ClimbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climb
        fields = ('id', 'colour', 'grade', 'centre', 'created')