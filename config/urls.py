
from django.contrib import admin
from django.urls import path
from main.views import home, categories, add_cat, edit_cat, del_prod, edit_prod, del_cat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('edit-prod/<int:pk>/', edit_prod),
    path('delete-prod/<int:pk>/', del_prod),
    path('categories/', categories),
    path('edit-cat/<int:pk>/', edit_cat),
    path('add-cat/', add_cat),
    path('del-cat/<int:pk>/', del_cat),
]
