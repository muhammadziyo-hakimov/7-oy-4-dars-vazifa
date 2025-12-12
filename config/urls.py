
from django.contrib import admin
from django.urls import path
from main.views import (home, categories, add_cat, edit_cat, del_prod, 
                        edit_prod, del_cat, courses, students, add_course, add_student, 
                        edit_course, del_course, edit_student, del_student)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('edit-prod/<int:pk>/', edit_prod),
    path('delete-prod/<int:pk>/', del_prod),
    path('categories/', categories),
    path('edit-cat/<int:pk>/', edit_cat),
    path('add-cat/', add_cat),
    path('del-cat/<int:pk>/', del_cat),
    path('courses/', courses),
    path('students/', students),
    path('add-course/', add_course),
    path('add-student/', add_student),
    path('edit-course/<int:pk>/', edit_course),
    path('del-course/<int:pk>/', del_course),
    path('edit-student/<int:pk>/', edit_student),
    path('del-student/<int:pk>/', del_student)
]
