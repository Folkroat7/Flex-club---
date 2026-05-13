from rest_framework import serializers
from .models import Sched, Workout, Trainer, Booker

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['name', 'specialization']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['title', 'description']

class SchedSerializer(serializers.ModelSerializer):
    workout = WorkoutSerializer()
    trainer = TrainerSerializer()
    trainId= Sched.trainId

    class Meta:
        model = Sched
        fields = ['id', 'workout', 'trainer', 'start_time', 'trainId','free_slots']

class BookerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booker
        fields = ['id', 'sched']

    def validate_sched(self, value):
        if value.free_slots <= 0:
            raise serializers.ValidationError('Нет свободных мест!')
        return value