from django.urls import path
from restapi import views

urlpatterns = [
    path("expenses/", views.ExpenselistCreate.as_view(), name="expense-list-create"),
    path(
        "expenses/<pk>",
        views.ExpenseRetriveDelete.as_view(),
        name="expense-retrieve-delete",
    ),
]
