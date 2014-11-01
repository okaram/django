from django.contrib import admin
from abads.models import ABExperiment, ExperimentAd


class ExperimentAdInline(admin.TabularInline):
    model = ExperimentAd
    extra = 4
    read_only_fields=('visits','clicks')


class ABExperimentAdmin(admin.ModelAdmin):
    inlines = [ExperimentAdInline]

admin.site.register(ABExperiment, ABExperimentAdmin)