from django.urls import path
from restapi import views

urlpatterns = [
    path("expenses/", views.ExpenselistCreate.as_view(), name="expense-list-create")
]
