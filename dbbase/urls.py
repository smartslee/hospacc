from django.urls import path
from . import views
from .views import (HdbUpdateView,IndexView, SearchFormView,HdbCreateView,HdbDeleteView, HdbprintView)

urlpatterns = [
    
    path('list/', views.index, name ='list'),
   # url(r'^dbedit/', views.hospdb_list, name ='edit'),
    path('input/', views.inputdb, name ='inputdbn'),
    path('', views.homep, name ='home'),
    path('dblistView/', views.IndexView.as_view(), name ='indexview'),
    path('<int:pk>/', views.HdbdetailView.as_view(), name="detail"),
    path('print(<int:pk>)/', views.HdbprintView.as_view(), name="print"),
    path('hdb/add/', views.HdbCreateView.as_view(), name="hdb_add"),
    path('update/<int:pk>/', HdbUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', HdbDeleteView.as_view(), name='delete'),
    #url(r'^list$',ProductListView.as_view(), name="ProductListView"),
    # url(r'^list/(?P<pk>\d+)/$',ProductDetailView.as_view(), name="ProductDetailview"),
    path('search',SearchFormView.as_view(),name='search'),
    path('login/', views.signin, name='login'),
    path('logout/', views.logout, name='logout'),
]