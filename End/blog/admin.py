from django.contrib import admin
from blog.models import *
from django import forms
# Register your models here.
@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    admin.site.site_title="ishareblog后台"
    admin.site.site_header="ishareblog后台"
    admin.site.index_title="ishareblog管理"

    list_display = ['id', 'title', 'href']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    fields = ('title','category','summary','banner','content','tags',('viewsCount','commentsCount'),('isShow', 'isTop','isHot'),'pubTime')
    list_display = ['title','category','isShow','isTop','isHot','show_tags','pubTime']
    @admin.display(description='标签')
    def show_tags(self,obj):
        return obj.tag_list
    #show_tags.short_description='标签'
    readonly_fields = ('viewsCount','commentsCount') #定义自读列
    search_fields = ['title']
    list_filter = ['pubTime','category','tags']
    #list_editable = ['isShow','isTop','isHot']
    list_per_page=20 #每页显示20条记录
    filter_horizontal=['tags'] #多对多的标签选择采取横向选择框排练
    date_hierarchy = 'pubTime' #根据pubTime发布日期显示日期级别过滤



    # def formfield_for_dbfield(self, db_field, request, **kwargs):
    #     formfield=super(BlogPostAdmin,self).formfield_for_dbfield(db_field,request,**kwargs)
    #     if db_field.name in ['summary']:
    #         formfield.widget=forms.Textarea(attrs=formfield.widget.attrs)
    #     return formfield

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['name','slogan','domain','desc']

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['title','href']

@admin.register(Focus)
class FoucusAdmin(admin.ModelAdmin):
    list_display = ['title','img']

@admin.register(Friend)
class FoucusAdmin(admin.ModelAdmin):
    list_display = ['siteName','path','desc']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id','tag']