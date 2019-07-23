from django.contrib import admin
from newspage.models import FeedList, UserPreferences

# Register your models here.

@admin.register(FeedList)
class FeedListAdmin(admin.ModelAdmin):
    list_display=['__str__','url','last_update']
    readonly_fields=['last_update']

@admin.register(UserPreferences)
class UserPreferencesAdmin(admin.ModelAdmin):
    list_display=['__str__','display_sites']
