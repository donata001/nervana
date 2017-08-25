from django.conf.urls import url

from .views import Login, Logout, TableView, ChartView

urlpatterns = [
    url(r'^login$', Login.as_view(), name='user_login'),
    url(r'^logout$', Logout.as_view(), name='user_logout'),
    url(r'^table_view', TableView.as_view(), name='table_view'),
    url(r'^chart_view', ChartView.as_view(), name='chart_view'),
    
]