


from django.conf.urls import url

from products.views import (ProductListView,
                            #product_list_view,
                            #product_detail_view,
                            ProductDetailView,
                            ProductDetailSlugView,
                            #ProductFeaturedListView,
                            #ProductFeaturedDetailView
                            )



urlpatterns = [


    #url('(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    url('$', ProductListView.as_view(), name='list'),

    url('(?P<pk>\d+)/$', ProductDetailView.as_view(),name='detail'),



]

