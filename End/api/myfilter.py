# -*- coding: utf-8 -*-
"""
    :author: XieJava
    :url: http://ishareread.com
    :copyright: © 2021 XieJava <xiejava@ishareread.com>
    :license: MIT, see LICENSE for more details.
"""
from django_filters import rest_framework as filters
from blog.models import *

class BlogPostFilter(filters.FilterSet):
    #根据文章标题模糊匹配
    words=filters.CharFilter(field_name='title',lookup_expr='icontains')
    #根据文章分类id过滤
    cateid=filters.CharFilter(field_name='category')
    #根据文章分类title过滤
    cate=filters.CharFilter(method="get_post_by_catetitle")
    #根据文章标签tag过滤
    tag=filters.CharFilter(method="get_post_by_tag")

    def get_post_by_catetitle(self,queryset, *arg):
        cate_title=arg[1]
        blogcate=BlogCategory.objects.filter(title=cate_title).values('id')
        if len(blogcate)>0:
            cate_id=str(blogcate[0]['id'])
            queryset = queryset.filter(category=cate_id)
        return queryset

    def get_post_by_tag(self,queryset, *arg):
        tag=arg[1]
        blogtag=Tag.objects.filter(tag=tag).values('id')
        if len(blogtag)>0:
            tag_id=str(blogtag[0]['id'])
            queryset = queryset.filter(tags=tag_id)
        return queryset

    class Meta:
        model=BlogPost
        fields=('words','cateid','cate','tag')