from django.urls import path
from .views import ShortcodeClassListView, post_crate_view, load_shortcode_data_view, GetFaviconView, post_detaile_data_view, archive_post, update_post, ShortcodeArchiveListView, shortcode_view
from django.contrib.auth.decorators import login_required

app_name = 'shortcode'

urlpatterns = [
    path('', login_required(ShortcodeClassListView.as_view()), name='dashboard-view'),
    path('create/', post_crate_view, name='dashboard-create'),
    path('archive/', login_required(ShortcodeArchiveListView.as_view()), name='archive-view'),
    path('update/archive/', archive_post, name='dashboard-archive'),
    path('list/', shortcode_view, name='shortcode-view'),
    path('json-list/', load_shortcode_data_view, name='load_shortcode_data'),
    path('update/<pk>/', update_post, name='dashboard-update'),
    path('update/<pk>/view/', post_detaile_data_view, name='dashboard-update-view'),
    path('get_favicon/', GetFaviconView.as_view(), name='get_favicon'),
]