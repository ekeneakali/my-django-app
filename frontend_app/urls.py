from django.urls import path
from frontend_app import views

app_name = 'frontend'

urlpatterns = [
    
    path('register', views.register, name='register'),
    path('log-in', views.log_in, name='log_in'),
    path('get-one/<int:pst_id>/', views.get_one, name='get_one'),
    path('view-user', views.view_user, name='view_user'),
    path('view/<int:get_id>/', views.view, name='view'),
    path('add-post', views.add_post, name='add_post'),
    path('view-post', views.view_post, name='view_post'),
    path('delete-post/<int:pst_id>/', views.delete_post, name='delete_post'),
    path('edit-post/<int:pst_id>/', views.edit_post, name='edit_post'),
    path('confirm-logout', views.confirm_logout, name='confirm_logout'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('contact-us', views.contact_us, name='contact_us'),
    path('advertisement', views.advertisement, name='advertisement'),
    path('about', views.about, name='about'),
    path('privacy', views.privacy, name='privacy'),
    path('edit-profile', views.edit_profile, name='edit_profile'),
    path('view-profile', views.view_profile, name='view_profile'),
    path('advert', views.advert, name='advert'),
    path('search', views.search, name='search'),
    path('change_password', views.change_password, name='change_password'),
    path('application', views.application, name='application'),
    path('web-services', views.web_services, name='web_services'),
    path('forget_password', views.forget_password, name='forget_password'),
    path('video', views.video, name='video'),
    path('view_video', views.view_video, name='view_video'),
    path('get_video/<int:pst_id>/', views.get_video, name='get_video'),
    path('user_video', views.user_video, name='user_video'),
    path('delete_video/<int:pst_id>/', views.delete_video, name='delete_video'),
    path('edit_video/<int:pst_id>/', views.edit_video, name='edit_video'),
    path('term_condition', views.term_condition, name='term_condition'),
    path('get_search', views.get_search, name='get_search'),
    
]
