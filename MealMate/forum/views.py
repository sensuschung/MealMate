from django.shortcuts import render, get_object_or_404, redirect
import requests
from datetime import datetime
from forum.models import GroupPost,Post,Forum,Tag,PostImage
from django.core.paginator import Paginator
import random
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from markdown import markdown 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

def group_post_view(request):
    forums = Forum.objects.all()
    group_posts = GroupPost.objects.order_by('-create_at')

    paginator = Paginator(group_posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'group_post_list.html',{'forums':forums,'group_posts':page_obj})


def post_detail(request, uuid):
    forums = Forum.objects.all()
    post = get_object_or_404(Post, id=uuid)
    post.click += 1
    post.save(update_fields=['click'])
    return render(request, 'post_detail.html', {'forums':forums,'post': post,})

def group_detail(request, uuid):
    forums = Forum.objects.all()
    current_time = timezone.now()
    group_post = get_object_or_404(GroupPost, id=uuid)
    return render(request, 'group_post_detail.html', {'forums':forums,'group_post': group_post,'current_time':current_time,})

@csrf_exempt
def create_tag(request):
    if request.method == 'POST':
        tag_name = request.POST.get('name')
        if tag_name and not Tag.objects.filter(name=tag_name).exists():
            new_tag = Tag.objects.create(name=tag_name)
            return JsonResponse({'status': 'success', 'name': new_tag.name})
        else:
            return JsonResponse({'status': 'error', 'message': 'Tag already exists or invalid name.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


@login_required 
def post_create_view(request):
    current_user = request.user
    if current_user.is_authenticated:
        username = current_user.username
    else:
        username = "Guest"

    forums = Forum.objects.all()
    tags = Tag.objects.all()
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            forum_id = request.POST.get('forum_name')
            content = request.POST.get('content')
            tags_string = request.POST.get('tags')
            tags = [tag.strip() for tag in tags_string.split(',')] if tags_string else []
            forum = Forum.objects.get(id=forum_id)
            author = request.user
            post_type = request.POST.get('type')
            if (post_type):
                post_type = "normal"
            
            content_markdown = markdown(content)
            
            post = Post.objects.create(
                title=title,
                author=author,
                forum=forum,
                content=content_markdown
            )
            
            if request.FILES.getlist('images'):
                for image_file in request.FILES.getlist('images'):
                    post_image = PostImage.objects.create(image=image_file)
                    post.images.add(post_image)
            
            for tag_name in tags:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tag.add(tag)
            
            messages.success(request, 'Post created successfully!')

            return JsonResponse({'status': 'success', 'message': 'Post created successfully!'})
        
        except Exception as e:
            context = {
                'username': request.user.username,
                'forums': Forum.objects.all(),
                'tags': Tag.objects.all(),
                'post_type': post_type,
                'title': title,
                'forum_id': forum_id,
                'content': content,
                'selected_tags': tags,
                'error_message': str(e)
            }
            print(e)
            return render(request, 'post_add.html', context)
    
    return render(request,'post_add.html', {'forums':forums,'username': username,'tags':tags})