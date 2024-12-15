from django.urls import path
from .views import TaskList, taskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, CustomLogoutView, RegisterPage

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', taskDetail.as_view(), name='tasks'),
    path('task-create/', TaskCreate.as_view(), name='tasks-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='tasks-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='tasks-delete'),
]
