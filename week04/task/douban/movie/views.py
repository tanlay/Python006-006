from django.shortcuts import render, redirect
from .models import Movie1292722 as Movie
from django.db.models import Avg, Q

# Create your views here.


def get_movie(request):
    # 从models获取数据传给template

    # 查询
    searchkw = request.GET.get('q', '')
    if searchkw:
        # 通过用户名和评论内容查询
        items = Movie.objects.filter(Q(user__contains=searchkw)| Q(comment__contains=searchkw))
    else:
        # 如果不查询则返回star>3的记录
        items = Movie.objects.all().filter(star__gt=3)
        # items = Movie.objects.values("user","star", "comment","ctime").filter(star__gt=3)

    ## 获取函数内所有本地变量
    return render(request, 'result.html', locals())
