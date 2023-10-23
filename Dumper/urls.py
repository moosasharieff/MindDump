from Dumper import views
from django.urls import path

app_name = "dumper"

urlpatterns = {
    path('about/', views.AboutView.as_view(), name='about_view')
}