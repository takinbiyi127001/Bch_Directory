import json
from django.contrib import admin

from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

# Register your models here.
from .models import Category, Shop, Review


class ReviewInline(admin.TabularInline):
    model = Review


class CategoryInline(admin.TabularInline):
    model = Category
    verbose_name = "Categorie"


class ShopAdmin(admin.ModelAdmin):
    # TabularInline
    inlines = [
        CategoryInline,
        ReviewInline,
    ]
    list_display = (
        "name",
        "address",
        "geolocation",
        "city",
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
