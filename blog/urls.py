from django.urls import path, include
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, AddCommentView
from .views import register
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('post/reset_password/', auth_views.PasswordResetView.as_view(template_name="password/password_reset.html"), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_sent.html"), name='password_reset_sent'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_form.html"), name='password_reset_confirm' ),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_done.html"), name='password_reset_complete'),
    path('post/register/', register, name='post_register'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='post_comment'),
    path('', include('django.contrib.auth.urls'))



]