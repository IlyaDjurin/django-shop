from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^log1/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^info/$', views.info, name='info'),
    url(r'^smart/$', views.ProductList, name='ProductList'),
    url(r'^smart/(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    url(r'^harak/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
    url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
    url(r'^contact/$', views.contactform, name='contact'),
    url(r'^thanks/$', views.thanks, name='thanks'),

]