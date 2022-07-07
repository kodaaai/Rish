from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('', views.ReviewListView.as_view(), name='home'),
    path('new/', views.ReviewCreateView.as_view(), name='review-create'),
    path('new/review/class_info_create', views.ClassCreateView.as_view(), name='class_name-create'),
    path('new/review/teacher_create', views.TeacherCreateView.as_view(), name='teacher-create'),
    path('new/review/tag_create', views.TagCreateView.as_view(), name='tag-create'),
]
