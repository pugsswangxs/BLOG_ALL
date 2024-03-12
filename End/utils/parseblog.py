# -*- coding: utf-8 -*-
"""
    :author: XieJava
    :url: http://ishareread.com
    :copyright: © 2021 XieJava <xiejava@ishareread.com>
    :license: MIT, see LICENSE for more details.
"""
import yaml

'''将md文件转成blog对象'''
def parseblog(blog_md_file):
    #读md文件
    md_f = open(blog_md_file, "r",encoding='utf-8')
    md_f_str=md_f.read()
    #解析两个---之间的内容
    pattern='---'
    blog_data={}
    pattern_list=list(pattern_search(md_f_str, pattern))
    if len(pattern_list)>=2:
        blog_info_str=md_f_str[pattern_list[0]+len(pattern):pattern_list[1]]
        blog_data=yaml.load(blog_info_str,Loader=yaml.SafeLoader)
        blog_data['content']=md_f_str[pattern_list[1]+len(pattern):]
    md_f.close()
    return blog_data

'''分割符号匹配检索'''
def pattern_search(string,pattern):
    index=0
    while index<len(string)-len(pattern):
        index=string.find(pattern,index,len(string))
        if index==-1:
            break
        yield index
        index+=len(pattern)-1

if __name__ == '__main__':
    blog_data=parseblog('E:\\CloudStation\\personal\\xiejavablog\\myhexo\\myblog\\source\\_posts\\2022-07-16-Python安装mysqlclient报错避坑.md')
    print(blog_data)
