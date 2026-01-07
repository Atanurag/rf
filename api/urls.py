from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.students),
    path('students/single/<int:pk>',views.studentDetailView),
    
    path('employees/',views.Employees.as_view()),

    path('employees/single/<int:pk>',  views.EmployeeDetail.as_view())

]
