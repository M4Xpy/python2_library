from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(
        r"^clients/create/$",
        views.ClientCreateView.as_view(),
        name="client-create",
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
    url(
        r"^loans/$",
        views.LoanListView.as_view(),
        name="loan-list",
    ),
    url(
        r"^loans/create/$",
        views.LoanCreateView.as_view(),
        name="loan-create",
    ),
    url(
        r"^loans/(?P<pk>\d+)/update/$",
        views.LoanUpdateView.as_view(),
        name="loan-update",
    ),
    url(
        r"^loans/(?P<pk>\d+)/delete/$",
        views.LoanDeleteView.as_view(),
        name="loan-delete",
    ),
]

app_name = "books"
