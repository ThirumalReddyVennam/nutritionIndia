# from django.urls import path
from django.conf.urls import url
from map_dashboard import views
from map_dashboard.views import (DashboardView,DashboardViewTab2,DashboardViewTab3,DashboardViewTab4)


urlpatterns = [
    # path('', DashboardView.as_view(), name='map')
    url(r'^$', DashboardView.as_view(), name='map'),
    url(r'^tab1$', DashboardView.as_view(), name='tab1'),
    url(r'^tab2$', DashboardViewTab2.as_view(), name='tab2'),
    url(r'^tab3$', DashboardViewTab3.as_view(), name='tab3'),
    url(r'^tab4$', DashboardViewTab4.as_view(), name='tab4'),
    url(r'^ajax/tab1AreaChange/$', views.create_post_area, name='ajaxAreaTab1'),
    url(r'^ajax/tab1IndicatorChange/$', views.create_post, name='ajaxIndicatorTab1'),
    url(r'^ajax/tab1SubgroupChange/$', views.create_post_sub, name='ajaxSubgroupTab1'),
    url(r'^ajax/tab1TimeperiodChange/$', views.create_post_timeperiod, name='ajaxTimeperiodTab1'),
    url(r'^tab2/ajax/tab2AreaChange/$', views.create_post_area, name='ajaxAreaTab2'),
    url(r'^tab2/ajax/tab2IndicatorChange/$', views.create_post, name='ajaxIndicatorTab2'),
    url(r'^tab2/ajax/tab2SubgroupChange/$', views.create_post_sub, name='ajaxSubgroupTab2'),
    url(r'^tab2/ajax/tab2TimeperiodChange/$', views.create_post_timeperiod, name='ajaxTimeperiodTab2'),
    url(r'^tab3/ajax/tab3AreaChange/$', views.create_post_area, name='ajaxAreaTab3'),
    url(r'^tab3/ajax/tab3IndicatorChange/$', views.create_post, name='ajaxIndicatorTab3'),
    url(r'^tab3/ajax/tab3SubgroupChange/$', views.create_post_sub, name='ajaxSubgroupTab3'),
    url(r'^tab3/ajax/tab3TimeperiodChange/$', views.create_post_timeperiod, name='ajaxTimeperiodTab3'),
    url(r'^tab4/ajax/tab4AreaChange/$', views.create_post_area, name='ajaxAreaTab4'),
    url(r'^tab4/ajax/tab4IndicatorChange/$', views.create_post, name='ajaxIndicatorTab4'),
    url(r'^tab4/ajax/tab4SubgroupChange/$', views.create_post_sub, name='ajaxSubgroupTab4'),
    url(r'^tab4/ajax/tab4TimeperiodChange/$', views.create_post_timeperiod, name='ajaxTimeperiodTab4'),

]
