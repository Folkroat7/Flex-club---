from django.db import models
from django.contrib.auth.models import User

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialization= models.CharField(max_length=100)
    descr = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Workout(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Sched(models.Model):
    workout= models.ForeignKey(Workout, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    trainId= models.TextField(blank=True)
    capacity = models.PositiveIntegerField(default=10)

    @property
    def free_slots(self):
        booked= self.bookings.count()
        return self.capacity - booked
    
class Booker(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="my_bookings")
    sched = models.ForeignKey(Sched, on_delete=models.CASCADE, related_name= "bookings")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'sched')

    def __str__(self):
        return f"{self.user.username} -> {self.sched}"

# Create your models here.
