from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from django_google_maps import fields as map_fields
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator
from taggit.managers import TaggableManager

# from phonenumber_field.formfields import PhoneNumberField
# from phonenumber_field.widgets import PhoneNumberPrefixWidget


# Create your models here.


class Shop(models.Model):
    name = models.CharField(_("name"), max_length=100)
    photo = models.ImageField(upload_to="uploads/", blank=True)
    address = map_fields.AddressField(_("address"), max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
    is_open_now = models.BooleanField(null=True)
    is_closed_temporarily = models.BooleanField(null=True)
    rating = models.IntegerField(
        default=0, validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    city = models.CharField(_("city"), max_length=50)
    countries = CountryField(blank=True)
    tags = TaggableManager()

    # phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial="AUS"))


class Review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="reviews")
    review = models.CharField(_("review"), max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.review


class Category(models.Model):
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name="category", null=True
    )
    name = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)


# For forms
# from django_countries.widgets import CountrySelectWidget

# class ShopForm(forms.ModelForm):
#     class Meta:
#         model = models.Shop
#         fields = ('name', 'address', 'geolocation', 'city', 'country')
#         widgets = {'country': CountrySelectWidget()}
