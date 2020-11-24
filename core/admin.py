from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from django.contrib.auth.models import User as Staff, Group

from .models import User, Category, Product

admin.site.site_header = "Boshqaruv paneli"
admin.site.index_title = "Notifier"
admin.site.site_title = "Boshqaruv paneli"
admin.site.empty_value_display = "Biriktirilmagan"

admin.site.unregister(Staff)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'email',
        'favorite_categories'
    ]

    def favorite_categories(self, obj: User):
        categories = []
        for category in obj.categories.all():
            categories.append(
                f"<a href='{reverse('admin:core_category_change', args=[category.id])}'>{category.name}</a>,"
            )
        return format_html("<br/>".join(categories))

    favorite_categories.short_description = "Yoqtirgan bo'limlari"

    search_fields = [
        'first_name',
        'last_name',
        'email'
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'count_of_products'
    ]

    def count_of_products(self, obj: Category):
        return f"{obj.products.count()} ta"

    count_of_products.short_description = "Biriktirilgan maxsulotlar soni"

    search_fields = [
        'name'
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'category',
        'name',
        'description',
        'price'
    ]

    search_fields = [
        'category__name',
        'name',
        'description'
    ]

    list_filter = [
        'category'
    ]

