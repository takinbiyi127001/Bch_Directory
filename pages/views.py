from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

# Create your views here.
from .forms import SearchForm
from shops.models import Shop


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


def item_search(request):
    form = SearchForm()
    query = None
    results = []
    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            # results = Post.published.annotate(
            #     search=SearchVector("title", "body"),
            # ).filter(search=query)
            search_vector = SearchVector("name", "address")
            search_query = SearchQuery(query)
            results = (
                Shop.annotate(
                    search=search_vector, rank=SearchRank(search_vector, search_query)
                )
                .filter(search=search_query)
                .order_by("-rank")
            )
    context = {"form": form, "query": query, "results": results}
    return render(request, "shops/search.html", context=context)
