# -*- coding: utf-8 -*-
"""
    :author: XieJava
    :url: http://ishareread.com
    :copyright: © 2021 XieJava <xiejava@ishareread.com>
    :license: MIT, see LICENSE for more details.
"""
from api import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter
blogcategory_list=views.BlogCategoryViewset.as_view({'get':'list',})
blogcategory_detail=views.BlogCategoryViewset.as_view({ 'get': 'retrieve',})
blog_list=views.BlogsView.as_view({'get':'list',})
blog_detail=views.BlogsView.as_view({ 'get': 'retrieve',})
site_list=views.SiteView.as_view({'get':'list',})
site_detail=views.SiteView.as_view({'get':'retrieve',})
social_list=views.SocialView.as_view({'get':'list',})
social_detail=views.SocialView.as_view({'get':'retrieve',})
focus_list=views.FocusView.as_view({'get':'list',})
focus_detail=views.FocusView.as_view({'get':'retrieve'})
friend_list=views.FriendView.as_view({'get':'list',})
friend_detail=views.FriendView.as_view({'get':'retrieve'})
tags_list=views.TagView.as_view({'get':'list',})
# router=DefaultRouter()
# router.register('blogs',views.BlogsView)
urlpatterns = [
    path('category/',blogcategory_list),
    path('category/<pk>/',blogcategory_detail),
    path('post/list',blog_list),
    path('post/<pk>',blog_detail),
    path('social/',social_list),
    path('site/<pk>',site_detail),
    path('focus/list',focus_list),
    path('comment/',blog_list),
    path('friend/',friend_list),
    path('tags/',tags_list),
]
