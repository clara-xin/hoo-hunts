from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.login, name="login"),
    path("home/", views.home, name="home"),
    path("logout", views.logout_view, name="logout"),
    path('base/', TemplateView.as_view(template_name="base.html")),
    path('profile/', TemplateView.as_view(template_name="profile.html"), name="profile"),
    #path('map/', TemplateView.as_view(template_name="map.html"), name = "map"),
    path('map/<int:submission_id>/', views.map_with_hunt, name="map"),
    path('create/', views.create_hunt, name = "create"),
    path('view_submissions/', views.view_submissions, name="view_submissions"),
    path('accept_submission/<int:submission_id>/', views.accept_submission, name='accept_submission'),
    path('decline_submission/<int:submission_id>/', views.decline_submission, name='decline_submission'),
    path('personal_hunts/', TemplateView.as_view(template_name="personal_hunts.html"), name="personal_hunts"),
    path('pending_submissions/', views.pending_submissions, name = "pending_submissions"),
    path('declined_submissions/', views.declined_submissions, name = "declined_submissions"),
    path('accepted_submissions/', views.accepted_submissions, name = "accepted_submissions"),
    path('choose_hunt/', views.choose_hunt, name = "choose_hunt"),
    path('activate_hunt/<int:submission_id>/', views.activate_hunt, name='activate_hunt'),
    path('deactivate_hunt/<int:submission_id>/', views.deactivate_hunt, name='deactivate_hunt'),
]