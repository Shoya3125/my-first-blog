from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import post

# Create your views here.
def post_list(request):
    posts=post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    """クエリセット（DB情報を抽出）"""
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
    posts=get_object_or_404(post,pk=pk)
    """クエリセット（DB情報を抽出）"""
    return render(request,'blog/post_detail.html',{'posts':posts})
