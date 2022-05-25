from django.contrib import admin

# Register your models here.
from ESapp.models import ElasticSearchModel

admin.site.register(ElasticSearchModel)