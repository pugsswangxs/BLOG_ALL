from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from common.customresponse import CustomResponse

class MyPage(PageNumberPagination):
    page_size = 8 #每页显示数量
    max_page_size = 50 #每页最大显示数量。
    page_size_query_param = 'size' #每页数量的参数名称
    page_query_param = 'page'  #页码的参数名称

    #自定义分页器的返回参数
    def get_paginated_response(self, data):
        ret_data = dict()
        ret_data['items'] = data
        # 加入自定义分页信息
        ret_data['total'] = self.page.paginator.count
        ret_data['hasNextPage'] = self.get_next_link()
        ret_data['size'] = self.page_size
        ret_data['page'] = self.page.number
        return CustomResponse(data=ret_data,code=200,msg="OK",status=status.HTTP_200_OK)