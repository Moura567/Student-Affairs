from django.urls import path
from . import views
urlpatterns = [
    path('department',views.department,name='department'),
    path('add',views.add,name='add'),
    path('edit/<id>', views.edit, name='edit'),
    path('change/<id>', views.change, name='change'),    
    path('all',views.allStudents,name="all"),

]
