from __future__ import annotations

from django.contrib import admin

# Register your models here.
from core.models import *

admin.site.register(Patient)
admin.site.register(Sample)
admin.site.register(Location)
admin.site.register(Laboratory)
admin.site.register(Pathologist)
