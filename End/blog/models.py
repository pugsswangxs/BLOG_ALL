from django.db import models
from common.basemodel import BaseModel
from mdeditor.fields import MDTextField
# Create your models here.
'''文章分类'''
class BlogCategory(BaseModel):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,verbose_name='分类名称',default='')
    href=models.CharField(max_length=100,verbose_name='分类路径',default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='文章分类'
        verbose_name_plural='文章分类'


'''文章标签'''
class Tag(BaseModel):
    id=models.AutoField(primary_key=True)
    tag=models.CharField(max_length=20, verbose_name='标签')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name='标签'
        verbose_name_plural='标签'


'''博客文章'''
class BlogPost(BaseModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='文章标题', unique = True)
    category = models.ForeignKey(BlogCategory, blank=True,null=True,verbose_name='文章分类', on_delete=models.DO_NOTHING)
    isTop=models.BooleanField(default=False,verbose_name='是否置顶')
    isHot=models.BooleanField(default=False,verbose_name='是否热门')
    isShow=models.BooleanField(default=False,verbose_name='是否显示')
    banner=models.CharField(max_length=200,verbose_name='文章图标',default='')
    summary=models.TextField(max_length=500,verbose_name='内容摘要',default='')
    content=MDTextField(verbose_name='内容')
    viewsCount= models.IntegerField(default=0, verbose_name="查看数")
    commentsCount=models.IntegerField(default=0, verbose_name="评论数")
    tags=models.ManyToManyField(to=Tag, related_name="tag_post", blank=True, default=None,verbose_name="标签")
    blogSource=models.CharField(max_length=200,blank=True, null=True, default='',verbose_name='文章来源')
    pubTime=models.DateTimeField(blank=True, null=True,verbose_name='发布日期')

    @property
    def tag_list(self):
        return ','.join([i.tag for i in self.tags.all()])

    def __str__(self):
            return self.title

    class Meta:
        verbose_name = '博客文章'
        verbose_name_plural = '博客文章'


'''站点信息'''
class Site(BaseModel):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50, verbose_name='站点名称', unique = True)
    avatar=models.CharField(max_length=200, verbose_name='站点图标')
    slogan=models.CharField(max_length=200, verbose_name='站点标语')
    domain=models.CharField(max_length=200, verbose_name='站点域名')
    notice=models.CharField(max_length=200, verbose_name='站点备注')
    desc=models.CharField(max_length=200, verbose_name='站点描述')

    def __str__(self):
            return self.name

    class Meta:
        verbose_name = '站点信息'
        verbose_name_plural = '站点信息'


'''社交信息'''
class Social(BaseModel):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=20, verbose_name='标题')
    icon=models.CharField(max_length=200, verbose_name='图标')
    color=models.CharField(max_length=20, verbose_name='颜色')
    href=models.CharField(max_length=100, verbose_name='路径')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '社交信息'
        verbose_name_plural = '社交信息'

'''聚焦'''
class Focus(BaseModel):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=20, verbose_name='标题')
    img=models.CharField(max_length=100, verbose_name='路径')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='聚焦'
        verbose_name_plural='聚焦'

'''友链'''
class Friend(BaseModel):
    id=models.AutoField(primary_key=True)
    siteName=models.CharField(max_length=20, verbose_name='友链站点名称')
    path=models.CharField(max_length=100, verbose_name='地址路径')
    desc=models.CharField(max_length=200, verbose_name='描述')

    def __str__(self):
        return self.siteName

    class Meta:
        verbose_name='友链'
        verbose_name_plural='友链'

