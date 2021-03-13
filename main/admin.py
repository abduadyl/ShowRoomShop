from django.contrib import admin
from .models import *

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    max_num = 10
    min_num = 1


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]


admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Like)
