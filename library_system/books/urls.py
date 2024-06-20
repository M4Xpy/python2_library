from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(
        r"^loans/$",
        views.LoanListView.as_view(),
        name="loan-list",
    ),
    url(
        r"^authors/$",
        views.AuthorListView.as_view(),
        name="author-list",
    ),
    url(
        r"^authors/create/$",
        views.AuthorCreateView.as_view(),
        name="author-create",
    ),
    url(
        r"^authors/(?P<pk>\d+)/update/$",
        views.AuthorUpdateView.as_view(),
        name="author-update",
    ),
    url(
        r"^authors/(?P<pk>\d+)/delete/$",
        views.AuthorDeleteView.as_view(),
        name="author-delete",
    ),
    url(
        r"^books/$",
        views.BookListView.as_view(),
        name="book-list",
    ),
    url(
        r"^books/create/$",
        views.BookCreateView.as_view(),
        name="book-create",
    ),
    url(
        r"^books/(?P<pk>\d+)/update/$",
        views.BookUpdateView.as_view(),
        name="book-update",
    ),
    url(
        r"^books/(?P<pk>\d+)/delete/$",
        views.BookDeleteView.as_view(),
        name="book-delete",
    ),
]

app_name = "books"
