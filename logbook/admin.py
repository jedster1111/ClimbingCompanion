from django.contrib import admin
from . models import Coder, Centre, Climb

class ClimbInline(admin.StackedInline):
    model = Climb

class CentreAdmin(admin.ModelAdmin):
    inlines = [ClimbInline,]

admin.site.register(Coder)
admin.site.register(Centre, CentreAdmin)
admin.site.register(Climb)

