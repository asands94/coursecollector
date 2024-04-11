from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.home, name='home'),

    path('courses/', views.CourseList.as_view(), name='course_index'),
    path('course/<int:pk>/', views.CourseDetail.as_view(), name='course_detail'),
    path('course/create', views.CourseCreate.as_view(), name='course_create'),
    path('course/<int:pk>/update/', views.CourseUpdate.as_view(), name='course_update'),
    path('course/<int:pk>/delete/', views.CourseDelete.as_view(), name='course_delete'),

    path('categories/', views.CategoryList.as_view(), name='category_index'),
    path('category/create', views.CategoryCreate.as_view(), name='category_create'),
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),

    path('profile/', views.ProfileDetail.as_view(), name='profile'),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),

    path('course/<int:pk>/add-note', views.CourseDetail.as_view(), name='add_note'),
    path('note/<int:pk>/update/', views.NoteUpdate.as_view(), name='note_update'),
    path('note/<int:pk>/delete/', views.NoteDelete.as_view(), name='note_delete'),

    path('accounts/signup/', views.signup, name='signup'),

    path("change-password/", auth_views.PasswordChangeView.as_view(template_name="profile/change_password.html", success_url=reverse_lazy('profile')), name='change_password'),
]
