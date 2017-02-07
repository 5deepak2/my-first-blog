from django.contrib import admin
from .models import JobPost,Category,Company

# Register your models here.

admin.site.register([JobPost,Category,Company],)

