from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
   path('', views.TodoListView.as_view(), name='list'),
   path('create/', views.TaskFormViews.as_view(), name='create'),
   path('<int:pk>/', views.CompleteView.as_view(), name='complete'),
   path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete')
]