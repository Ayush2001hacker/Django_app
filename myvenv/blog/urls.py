from django.urls import path 
from .views import home ,detail,create_task,delete_task,mark_completed,update_task
urlpatterns = [
    path('',home,name="home"),
    path('detail/<int:id>',detail ,name="detail"),
    path('create/',create_task,name="create_task"),
    path('delete/<int:pk>',delete_task,name="delete_task"),
    path('mark_completed/<int:todo_id>/', mark_completed, name='mark_completed'),
    path('update/<int:id>/', update_task, name='update_task'),
]
