from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin


from shops.models import Shop


class ShopSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = (
            "name",
            "photo",
            "address",
            "geolocation",
            "is_open_now",
            "is_closed_temporarily",
            "rating",
            "city",
            "countries",
        )
