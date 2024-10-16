from django.shortcuts import render
import requests
from datetime import datetime
from forum.models import GroupPost,Post

def forum_home_view(request):
    response = requests.get("https://canteen.sjtu.edu.cn/CARD/Ajax/Place")
    canteen_data = response.json()
    group_posts = GroupPost.objects.order_by('-create_at')[:3]
    posts = Post.objects.order_by('-last_modified')[:5]
    return render(request,'forum.html', {'canteen_data': canteen_data,'group_posts': group_posts,'posts':posts})
