from django.contrib import admin
from .models import Item, Category, Comments, Post, UserProfile, Order

# Register your models here.
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Order)
