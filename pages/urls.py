from django.urls import path

from .views import HomePageView, AboutPageView, item_search


urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    path("search/", item_search, name="item_search"),
]
