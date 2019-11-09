from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Comment, Person, Musician, Album, Membership, Group, Woman, Place, Waiter, Restaurant

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Woman)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Person)
admin.site.register(Membership)
admin.site.register(Group)

admin.site.register(Place)
admin.site.register(Waiter)
admin.site.register(Restaurant)
