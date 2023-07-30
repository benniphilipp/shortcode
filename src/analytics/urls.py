from django.urls import path
from .views import AnalyticsView
from django.contrib.auth.decorators import login_required

app_name = 'analytics'

urlpatterns = [
    path('', login_required(AnalyticsView.as_view()), name='analytics-view'),
    # path('create/', post_crate_view, name='dashboard-create'),
    # path('update/<pk>/', update_post, name='dashboard-update'),
    # path('update/archive/', archive_post, name='dashboard-archive'),
    # path('update/<pk>/view/', post_detaile_data_view, name='dashboard-update-view'),
    
    # path('create/', CrateShortCodeCreateView.as_view(), name='dashboard-create'),
]