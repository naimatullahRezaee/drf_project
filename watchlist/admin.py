from django.contrib import admin
from watchlist.models import Watch, Review, StreamPlatform
# Register your models here.
admin.site.register(Watch)
admin.site.register(Review)
admin.site.register(StreamPlatform)