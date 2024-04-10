from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.CourseList.as_view(), name='course_index'),
    path('course/<int:pk>/', views.CourseDetail.as_view(), name='course_detail'),
    path('course/create', views.CourseCreate.as_view(), name='course_create'),
    path('course/<int:pk>/update/', views.CourseUpdate.as_view(), name='course_update'),
    path('course/<int:pk>/delete/', views.CourseDelete.as_view(), name='course_delete'),

    path('categories/', views.CategoryList.as_view(), name='category_index'),
    path('category/create', views.CategoryCreate.as_view(), name='category_create'),
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),

    path('accounts/signup/', views.signup, name='signup'),
]
