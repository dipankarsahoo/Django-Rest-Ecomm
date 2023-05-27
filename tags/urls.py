from django.urls import path
from tags import views

urlpatterns = [
    path('/create/', views.index, name='tag_create')
    # path('/list/', views.signup, name='tag_list')
    # path('/details/<str: >', views.details, name='tag_detail')
]
