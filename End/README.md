# ishareblog

#### 介绍
>**ishareblog** 是Python django开发的博客后台及接口程序
> 
>适配Gblog前端模板[码云]https://gitee.com/xiejava/Gblog


#### 软件架构
软件架构说明<br>
Python django框架开发<br>
数据库默认mysql


#### 主要功能

- [x] 提供适配Gblog博客模板的后台接口
- [x] 博客内容管理包括分类、站点配置、博客文章
- [x] 博客文章支持markdown编辑器
- [x] 支持hexo的.md博客文件迁移
- [ ] 支持生成hexo的.md博客文件并导出

#### 安装教程
python3.8及以上
1. 获取代码<br>
```
clone https://gitee.com/xiejava/ishareblog.git
```
2. 安装依赖库<br>
```
pip install -r requirements.txt
```
3. 迁移数据库<br>
数据库配置在ishareblog目录的settings.py中，根据自己实际情况配置修改<br>
新建mysql数据库ishareblog<br>
```
python manage.py makemigrations
python manage.py migrate
```
4. 启动ishareblog应用<br>
```
python manage.py runserver
```

#### 使用说明

1. 迁移hexo的.md博客<br>
ishareblog支持hexo的.md博客目录或单个博客文件的迁移<br>
执行`python manage.py transblog -h`获得迁移命令的说明和帮助<br>
会提示命令的参数和用法：
![管理命令帮助](https://xiejava1018.github.io/xiejavaimagesrc/images/2022/20220727/Django%E8%87%AA%E5%AE%9A%E4%B9%89manage.py%E5%91%BD%E4%BB%A4%E5%AE%9E%E7%8E%B0hexo%E5%8D%9A%E5%AE%A2%E8%BF%81%E7%A7%BB/%E7%AE%A1%E7%90%86%E5%91%BD%E4%BB%A4%E5%B8%AE%E5%8A%A9.png)
执行`python manage.py transblog`根据命令行提示输入指定要迁移的hexo的.md文件路径或目录。一般在hexo的source\_posts\目录下。<br>
输入需要迁移的.md文件或路径<br>
不出意外的情况下控制台会打印“XXXX.md读取解析入库成功！”的信息
![执行效果](https://xiejava1018.github.io/xiejavaimagesrc/images/2022/20220727/Django%E8%87%AA%E5%AE%9A%E4%B9%89manage.py%E5%91%BD%E4%BB%A4%E5%AE%9E%E7%8E%B0hexo%E5%8D%9A%E5%AE%A2%E8%BF%81%E7%A7%BB/%E6%89%A7%E8%A1%8C%E6%95%88%E6%9E%9C1.png)
访问博客，可以看到文章已经迁移过来了
![执行效果](https://xiejava1018.github.io/xiejavaimagesrc/images/2022/20220727/Django%E8%87%AA%E5%AE%9A%E4%B9%89manage.py%E5%91%BD%E4%BB%A4%E5%AE%9E%E7%8E%B0hexo%E5%8D%9A%E5%AE%A2%E8%BF%81%E7%A7%BB/%E6%89%A7%E8%A1%8C%E6%95%88%E6%9E%9C2.png)


#### 效果

##### 1、后台管理
管理界面
![管理界面](https://xiejava1018.github.io/xiejavaimagesrc/images/2022/20220726/%E5%90%8E%E5%8F%B0%E7%AE%A1%E7%90%86.png)
博客文章列表
![博客文章列表](https://xiejava1018.github.io/xiejavaimagesrc/images/2022/20220726/%E5%8D%9A%E5%AE%A2%E6%96%87%E7%AB%A0%E5%88%97%E8%A1%A8.png)
文章内容编辑，支持markdown
![文章内容编辑，支持markdown](https://xiejava1018.github.io/xiejavaimagesrc/images/2022/20220726/%E6%96%87%E7%AB%A0%E5%86%85%E5%AE%B9markdown%E7%BC%96%E8%BE%91.png)
分类管理
![文章分类](https://xiejava1018.github.io/xiejavaimagesrc/images/2022/20220726/%E5%88%86%E7%B1%BB%E7%AE%A1%E7%90%86.png)
标签管理
![标签管理](https://xiejava1018.github.io/xiejavaimagesrc/images/2022/20220726/%E6%A0%87%E7%AD%BE%E7%AE%A1%E7%90%86.png)
社交信息
![社交信息](https://xiejava1018.github.io/xiejavaimagesrc/images/2022/20220726/%E7%A4%BE%E4%BA%A4%E4%BF%A1%E6%81%AF.png)
##### 2、接口
接口清单
![接口清单](https://xiejava1018.github.io/xiejavaimagesrc/images/2022/20220726/%E6%8E%A5%E5%8F%A3%E6%B8%85%E5%8D%95.png)
文章列表接口，支持翻页
![文章列表接口](https://xiejava1018.github.io/xiejavaimagesrc/images/2022/20220726/%E6%96%87%E7%AB%A0%E5%88%97%E8%A1%A8%E6%8E%A5%E5%8F%A3.png)

文章详情接口
![文章详情接口](https://xiejava1018.github.io/xiejavaimagesrc/images/2022/20220726/%E6%96%87%E7%AB%A0%E8%AF%A6%E6%83%85%E6%8E%A5%E5%8F%A3.png)

##### 3、前台展现
![前台展现](https://xiejava1018.github.io/xiejavaimagesrc/images/2022/20220726/%E5%89%8D%E5%8F%B0%E5%B1%95%E7%8E%B0.png)

文章列表
![文章列表](https://xiejava1018.github.io/xiejavaimagesrc/images/2022/20220726/%E6%96%87%E7%AB%A0%E5%88%97%E8%A1%A8.png)
文章详情，支持markdown显示及目录
![文章详情](https://xiejava1018.github.io/xiejavaimagesrc/images/2022/20220726/%E6%96%87%E7%AB%A0%E8%AF%A6%E6%83%85.png)

社交信息
![社交信息](https://xiejava1018.github.io/xiejavaimagesrc/images/2022/20220726/%E7%A4%BE%E4%BA%A4%E4%BF%A1%E6%81%AF-%E5%89%8D%E5%8F%B0.png)

博客效果地址：[http://blog.ishareread.com](http://blog.ishareread.com)

后续考虑:<br>
1、django原生admin的管理界面还是简陋了一点，后续可能会用其他管理界面的UI给换掉<br>
2、现在有了一个hexo的博客了，后续可能会考虑实现hexo生成的博客内容直接同步到django的博客，或者django博客编辑的内容直接生成hexo的.md文件<br>
有兴趣的话可以关注本博客


#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 其他
