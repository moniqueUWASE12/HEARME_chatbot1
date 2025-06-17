from django.contrib import admin
from .models import Therapist, Video
from .models import Hospital

admin.site.register(Hospital)
admin.site.register(Therapist)
admin.site.register(Video)

