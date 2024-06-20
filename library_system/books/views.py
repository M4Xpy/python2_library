from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import generic

from .forms import BookSearchForm, AuthorSearchForm, LoanSearchForm
from .models import Book, Loan, Author


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = "author_list"
    template_name = "authors/author_list.html"
    paginate_by = 5

    def get_context_data(self, object_list=None, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context["search_form"] = AuthorSearchForm(
            initial={"name": self.request.GET.get("name", "")}
        )
        return context

    def get_queryset(self):
        queryset = Author.objects.all()

        name = self.request.GET.get("name")
        if name:
            return queryset.filter(name__icontains=name)

        return queryset


class AuthorCreateView(generic.CreateView):
    model = Author
    template_name = "authors/author_form.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("authors:author-list")


class AuthorUpdateView(generic.UpdateView):
    model = Author
    template_name = "authors/author_form.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("authors:author-list")


class AuthorDeleteView(generic.DeleteView):
    model = Author
    template_name = "authors/author_confirm_delete.html"

    def get_success_url(self):
        return reverse("authors:author-list")


def index(request):
    return render(
        request,
        "books/index.html",
        {
            "authors": Author.objects.all(),
            "books": Book.objects.all(),
            "loans": Loan.objects.all(),
        },
    )


class BookListView(generic.ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    paginate_by = 5

    def get_context_data(self, object_list=None, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context["search_form"] = BookSearchForm(
            initial={"title": self.request.GET.get("title", "")}
        )
        return context

    def get_queryset(self):
        queryset = Book.objects.all()

        title = self.request.GET.get("title")
        author = self.request.GET.get("author")
        if title:
            return queryset.filter(title__icontains=title)
        if author:
            return queryset.filter(author__name__icontains=author)

        return queryset


class BookCreateView(generic.CreateView):
    model = Book
    fields = "__all__"

    def get_success_url(self):
        return reverse("books:book-list")


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = "__all__"

    def get_success_url(self):
        return reverse("books:book-list")


class BookDeleteView(generic.DeleteView):
    model = Book

    def get_success_url(self):
        return reverse("books:book-list")


class LoanListView(generic.ListView):
    model = Loan
    context_object_name = "loan_list"
    template_name = "loans/loan_list.html"
    paginate_by = 5

    def get_context_data(self, object_list=None, **kwargs):
        context = super(LoanListView, self).get_context_data(**kwargs)
        context["search_form"] = LoanSearchForm(
            initial={"client_name": self.request.GET.get("client_name", "")}
        )
        return context

    def get_queryset(self):
        queryset = Loan.objects.select_related('book', 'client')

        client_name = self.request.GET.get("client_name")
        book_title = self.request.GET.get("book_title")
        if client_name:
            return queryset.filter(client__name__icontains=client_name)
        if book_title:
            return queryset.filter(book__title__icontains=book_title)

        return queryset
