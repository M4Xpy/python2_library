from django.contrib import admin

from . import models

for model in (
    models.Author,
    models.Book,
    models.Client,
    models.Loan,
):
    admin.site.register(model)
