from django.urls import path
from . import views

app_name = "ads"
urlpatterns = [
    path('ad_list/', views.AdListView.as_view()),
    path('ad_detail/<int:ad_id>/', views.AdDetailView.as_view()),
    path('ad_create/', views.AdCreateView.as_view()),
    path('ad_update/<int:ad_id>/', views.AdUpdateView.as_view()),
    path('ad_delete/<int:ad_id>/', views.AddDeleteView.as_view()),
    path('search/', views.AdSearchView.as_view()),
]
