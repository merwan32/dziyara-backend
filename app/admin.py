from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Agent)
admin.site.register(Wilaya)

admin.site.register(SiteEvaluation)
admin.site.register(WorkingDayTime)
admin.site.register(UserComment)
admin.site.register(TransportMean)
admin.site.register(Event)


@admin.register(TouristicSite)
class TouristicSiteAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj: 
            form.base_fields['agent'].initial = request.user.agent
            form.base_fields['wilaya'].initial = request.user.agent.wilaya
        return form
    
    def save_model(self, request, obj, form, change):
        if not change: 
            obj.agent = request.user.agent
        super().save_model(request, obj, form, change)

    