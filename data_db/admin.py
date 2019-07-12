from django.contrib import admin
from .models import Sample, Experiment, Project

admin.site.register(Sample)
admin.site.register(Experiment)
admin.site.register(Project)
