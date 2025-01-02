from django.contrib import admin
from .models import Movie, Review 
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ('name',)
    list_display = ('id', 'name', 'price')
    list_filter = ('price',)
    
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)


