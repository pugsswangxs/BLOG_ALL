# -*- coding: utf-8 -*-
"""
    :author: XieJava
    :url: http://ishareread.com
    :copyright: © 2021 XieJava <xiejava@ishareread.com>
    :license: MIT, see LICENSE for more details.
"""
from blog.models import *
from rest_framework import serializers
class BlogCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogCategory
        fields = "__all__"

class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class BlogPostModelSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    pubTime=serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    #category_id = serializers.CharField(max_length=32, source='category.id')
    category=BlogCategoryModelSerializer()
    tags=serializers.SerializerMethodField()

    # 多对多，钩子函数序列化,必须是以get_开头的
    def get_tags(self, obj):
        tags = obj.tags.all()
        tag = TagModelSerializer(tags, many=True)
        return tag.data

    class Meta:
        model=BlogPost
        fields="__all__"

class SiteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = "__all__"

class SocialModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = "__all__"

class FocusModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Focus
        fields = "__all__"

class FriendModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = "__all__"

