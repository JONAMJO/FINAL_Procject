from django.contrib import admin
from .models import Genre, Movie, Review, Hashtag


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'subtitle', 'director', 'actor', 'image', 'link', 'pubDate', 'userRating',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'review', 'score',)


class HashtagAdmin(admin.ModelAdmin):
    list_display = ('content',)


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)    
admin.site.register(Review, ReviewAdmin)
admin.site.register(Hashtag, HashtagAdmin)