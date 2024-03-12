# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework import filters
from api.myfilter import BlogPostFilter
from api.serializers import *
from blog.models import BlogCategory, BlogPost,Site,Social,Focus,Friend,Tag
from api.mypage import MyPage
from common.custommodelviewset import CustomModelViewSet
from common.customresponse import CustomResponse

class BlogCategoryViewset(CustomModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategoryModelSerializer

class BlogsView(CustomModelViewSet):
    queryset = BlogPost.objects.filter(isShow=True).order_by('-isTop','-pubTime','-update_time')
    serializer_class = BlogPostModelSerializer
    pagination_class = MyPage
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = BlogPostFilter
    #搜索
    search_fields=('title',)
    #排序
    ordering_fields = ('isTop', 'update_time')
    #自定义获取详情接口
    def retrieve(self,request,*args, **kwargs):
        instance=self.get_object()
        instance.viewsCount+=1
        instance.save()
        serializer=self.get_serializer(instance)
        return CustomResponse(data=serializer.data,code=200,msg="success",status=status.HTTP_200_OK)


class SiteView(CustomModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteModelSerializer

class SocialView(CustomModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialModelSerializer

class FocusView(CustomModelViewSet):
    queryset = Focus.objects.all()
    serializer_class = FocusModelSerializer

class FriendView(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendModelSerializer

class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer
