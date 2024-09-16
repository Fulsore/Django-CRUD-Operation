from django.urls import path
from .views import Home, Add_Student_Data,Delete,EditStudent

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('add-student/', Add_Student_Data.as_view( ), name='add-student'),
    path('delete-student/', Delete.as_view(), name='delete-student'),
    path('edit-student/<int:id>/', EditStudent.as_view(), name='edit-student'),  # Note the trailing slash
]