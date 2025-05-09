from django.contrib import admin
from .models import Region, Prices, Neighbourhood, ZipCode, Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'region', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user__username', 'region__region_name', 'content')

admin.site.register(Review, ReviewAdmin)
admin.site.register(Region)
admin.site.register(Prices)
admin.site.register(Neighbourhood)
admin.site.register(ZipCode)

# Register your models here.
