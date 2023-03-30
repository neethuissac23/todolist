from . import views
from django.urls import path

app_name = 'todoapp'

urlpatterns = [
    path('view/',views.Tasklistview.as_view(), name='view'),
    path('cddetail/<int:pk>/', views.Taskdetailview.as_view(), name='detailtask'),
    path('cdupdate/<int:pk>/', views.Taskupdateview.as_view(), name='update'),
    path('cddelete/<int:pk>/', views.Taskdeleteview.as_view(), name='delete'),
    path('', views.index, name="index"),
    path('delete/<int:id>/', views.deletelist, name="deletelist"),
    path('update/<int:id>/', views.updatelist, name="updatelist"),
]
