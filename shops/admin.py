import json
from django.contrib import admin

from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

# Register your models here.
from .models import Category, Shop, Review, Tag


class ReviewInline(admin.TabularInline):
    model = Review


class TagInline(admin.TabularInline):
    model = Tag
    verbose_name = "Tags"


class CategoryInline(admin.TabularInline):
    model = Category
    verbose_name = "Categorie"


class ShopAdmin(admin.ModelAdmin):
    # TabularInline
    inlines = [
        CategoryInline,
        ReviewInline,
        TagInline,
    ]
    list_display = (
        "name",
        "address",
        "geolocation",
        "city",
        "is_open_now",
        "is_closed_temporarily",
        "rating",
        "city",
        "countries",
    )

    formfield_overrides = {
        map_fields.AddressField: {
            "widget": map_widgets.GoogleMapsAddressWidget(
                attrs={"data-map-type": "roadmap"}
            )
        },
    }

    # formfield_overrides = {
    #     map_fields.AddressField: {
    #         "widget": map_widgets.GoogleMapsAddressWidget(
    #             attrs={
    #                 "data-map-type": "roadmap",
    #                 "data-autocomplete-options": json.dumps(
    #                     {
    #                         "types": ["geocode", "establishment"],
    #                         "componentRestrictions": {"country": "aus"},
    #                     }
    #                 ),
    #             }
    #         )
    #     },
    # }


# class CategoryAdmin(admin.ModelAdmin):
#     model = Category
#     list_display = (
#         "name",
#         "last_updated",
#     )


admin.site.register(Shop, ShopAdmin)
