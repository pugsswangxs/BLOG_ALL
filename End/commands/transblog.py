# -*- coding: utf-8 -*-
"""
    :author: XieJava
    :url: http://ishareread.com
    :copyright: © 2021 XieJava <xiejava@ishareread.com>
    :license: MIT, see LICENSE for more details.
"""
import os
import sys

from blog.models import BlogPost,BlogCategory,Tag
from utils.parseblog import parseblog
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help='读取指定目录的.md文件解析至ishareblog'

    def add_arguments(self, parser):
        parser.add_argument('--path',help='输入.md文件的目录')
        parser.add_argument('--file',help='输入.md文件的路径')

    def handle(self, *args, **options):
        inputfile = input('请输入指定的目录路径或.md文件路径:')
        if inputfile.find('.md') > 0:
            self.transblogbyfile(inputfile)
        else:
            self.transblogbypath(inputfile)
        if options['path']:
            self.transblogbypath(options['path'])
        if options['file']:
            self.transblogbyfile(options['file'])

    '''读取目录解析md文件并写入数据库'''
    def transblogbypath(self,filepath='',):
        try:
            files = os.listdir(filepath)
            for file in files:
                if file.find('.md') > 0:
                    blog_file = os.path.join(filepath, file)
                    self.transblogbyfile(blog_file)
        except FileNotFoundError as e:
            print('请确认输入是否正确。',e)

    '''读取md文件入库'''
    def transblogbyfile(self,blogfile=''):
        print('开始读取'+blogfile + '文件')
        blog_info = parseblog(blogfile)
        filename=os.path.basename(blogfile)
        #判断是否存在相同的title
        qs=BlogPost.objects.filter(title=blog_info['title'])
        if len(qs)==0:
            category = None
            tag_objs = []
            if 'categories' in blog_info:
                categories=blog_info['categories']
                if categories and len(categories)>0:
                    category_title = categories[0]
                    category_qs=BlogCategory.objects.filter(title=category_title)
                    if len(category_qs)>0:
                        category=category_qs[0]
            if 'tags' in blog_info:
                tags=blog_info['tags']
                for tag in tags:
                    tag_obj,b=Tag.objects.get_or_create(tag=tag)
                    tag_objs.append(tag_obj)
            blog = BlogPost()
            blog.title = blog_info['title']
            blog.content = blog_info['content']
            blog.isShow = 1 #默认显示
            blog.summary=blog.content[0:200] #默认提取内容的前200个字作为摘要
            blog.category=category
            blog.blogSource = filename
            blog.pubTime=blog_info['date']
            blog.save()
            if len(tag_objs)>0:
                blog.tags.add(*tag_objs)
            print(filename + '读取解析入库成功！')
        else:
            print(blog_info['title']+'已经存在！')