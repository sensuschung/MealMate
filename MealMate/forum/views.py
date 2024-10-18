from django.shortcuts import render, get_object_or_404
import requests
from datetime import datetime
from forum.models import GroupPost,Post,Forum
from django.core.paginator import Paginator
import random

def forum_home_view(request):
    response = requests.get("https://canteen.sjtu.edu.cn/CARD/Ajax/Place")
    canteen_data = response.json()
    group_posts = GroupPost.objects.order_by('-create_at')[:3]
    posts = Post.objects.order_by('-click')[:5]
    return render(request,'forum.html', {'canteen_data': canteen_data,'group_posts': group_posts,'posts':posts})

def forum_post_view(request, forum_id):
    forums = Forum.objects.all()
    forum_target = get_object_or_404(Forum, id=forum_id)
    posts = Post.objects.filter(forum=forum_target).order_by('-last_modified')
    
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'forum_post.html',{'forums':forums,'posts':page_obj,'selected_forum_id': forum_target.id,'forum_target':forum_target})

def post_detail(request, uuid):
    forums = Forum.objects.all()
    post = get_object_or_404(Post, id=uuid)
    post.click += 1
    post.save(update_fields=['click'])
    images = ['cat1.png', 'cat2.png', 'cat3.png', 'cat4.png']
    selected_image = random.choice(images)
    return render(request, 'post_detail.html', {'forums':forums,'post': post,'selected_image': selected_image,})