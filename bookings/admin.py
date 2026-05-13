from django.contrib import admin
from .models import Trainer, Workout, Sched, Booker

admin.site.register(Trainer)
admin.site.register(Workout)
admin.site.register(Sched)
admin.site.register(Booker) 

# Register your models here.
